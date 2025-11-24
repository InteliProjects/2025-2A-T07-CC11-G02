from __future__ import annotations

import csv
import hashlib
import json
import logging
import re
import unicodedata
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple

import faiss
import numpy as np
import torch
from huggingface_hub import snapshot_download
from sentence_transformers import SentenceTransformer
from transformers import AutoModel, AutoModelForCausalLM, AutoTokenizer

from ..core.config import CONFIG

logger = logging.getLogger(__name__)


class _HFEncoder:
    """Minimal HF encoder fallback when SentenceTransformer snapshot is incomplete."""

    def __init__(
        self,
        model_id: str,
        *,
        device: str,
        pooling: str = "mean",
        max_length: int = 128,
        cache_dir: str | None = None,
    ) -> None:
        pooling = (pooling or "mean").lower()
        if pooling not in {"mean", "cls"}:
            pooling = "mean"
        self.pooling = pooling
        self.max_length = max_length
        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_id, cache_dir=cache_dir)
        self.model = (
            AutoModel.from_pretrained(model_id, cache_dir=cache_dir).to(device).eval()
        )

    def encode(
        self,
        sentences: Sequence[str],
        batch_size: int = 32,
        show_progress_bar: bool = False,  # kept for API compatibility
        convert_to_numpy: bool = True,
        normalize_embeddings: bool = False,
    ):
        if not sentences:
            arr = np.zeros((0, self.model.config.hidden_size), dtype="float32")
            return (
                arr
                if convert_to_numpy
                else torch.empty((0, self.model.config.hidden_size))
            )

        embeddings = []
        for start in range(0, len(sentences), batch_size):
            batch = sentences[start : start + batch_size]
            inputs = self.tokenizer(
                batch,
                return_tensors="pt",
                padding=True,
                truncation=True,
                max_length=self.max_length,
            ).to(self.device)
            with torch.no_grad():
                outputs = self.model(**inputs)
            hidden = outputs.last_hidden_state
            if self.pooling == "mean":
                mask = inputs["attention_mask"].unsqueeze(-1)
                summed = (hidden * mask).sum(dim=1)
                counts = mask.sum(dim=1).clamp(min=1)
                pooled = summed / counts
            else:
                pooled = hidden[:, 0, :]
            embeddings.append(pooled.detach().cpu())

        stacked = torch.cat(embeddings, dim=0)
        if convert_to_numpy:
            arr = stacked.numpy().astype("float32")
            if normalize_embeddings:
                arr = _normalize_embeddings(arr)
            return arr

        if normalize_embeddings:
            stacked = torch.nn.functional.normalize(stacked, p=2, dim=1)
        return stacked


def _expand_cache_dir(path: str | None) -> Optional[str]:
    if not path:
        return None
    return str(Path(path).expanduser())


def _pick_device(preferred: Optional[str] = None) -> str:
    if preferred:
        return preferred
    if torch.cuda.is_available():
        return "cuda"
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():  # type: ignore[attr-defined]
        return "mps"
    return "cpu"


def _normalize_embeddings(arr: np.ndarray) -> np.ndarray:
    norms = np.linalg.norm(arr, axis=1, keepdims=True) + 1e-12
    return arr / norms


def _ensure_document(item: Any, idx: int) -> Optional[Dict[str, Any]]:
    if isinstance(item, str):
        return {"id": str(idx), "text": item, "type": "default", "metadata": {}}
    if isinstance(item, dict):
        text = item.get("text") or item.get("content") or item.get("body")
        if not text:
            return None
        doc_id = str(item.get("id", idx))
        doc_type = str(item.get("type") or item.get("category") or "default")
        metadata = item.get("metadata") or {
            k: v
            for k, v in item.items()
            if k not in {"text", "content", "body", "id", "type", "category"}
        }
        return {
            "id": doc_id,
            "text": text,
            "type": doc_type,
            "metadata": metadata,
        }
    return None


def _parse_jsonl_file(path: Path) -> List[Dict[str, Any]]:
    docs: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for idx, line in enumerate(handle):
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except json.JSONDecodeError:
                logger.warning("Ignoring malformed jsonl line in %s", path)
                continue
            doc = _ensure_document(item, idx)
            if doc:
                docs.append(doc)
    return docs


def _parse_json_file(path: Path) -> List[Dict[str, Any]]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if isinstance(data, dict):
        for key in ("documents", "docs", "items", "data"):
            if key in data and isinstance(data[key], list):
                data = data[key]
                break
    if not isinstance(data, list):
        return []
    docs: List[Dict[str, Any]] = []
    for idx, item in enumerate(data):
        doc = _ensure_document(item, idx)
        if doc:
            docs.append(doc)
    return docs


def _clean_csv_value(value: Any) -> Optional[str]:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    lowered = text.lower()
    if lowered in {"nan", "none", "null"}:
        return None
    return text


def _normalize_csv_key(raw_key: str) -> str:
    decoded = unicodedata.normalize("NFKD", raw_key)
    ascii_key = "".join(ch for ch in decoded if not unicodedata.combining(ch))
    ascii_key = re.sub(r"[^0-9A-Za-z]+", "_", ascii_key)
    ascii_key = "_".join(part for part in ascii_key.split("_") if part)
    ascii_key = ascii_key.lower().strip("_")
    return ascii_key or "field"


def _format_price(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    normalized = value.replace("R$", "").replace(" ", "")
    normalized = normalized.replace(".", "").replace(",", ".")
    try:
        amount = float(normalized)
    except ValueError:
        return value.strip()
    formatted = f"R$ {amount:,.2f}"
    formatted = formatted.replace(",", "¤").replace(".", ",").replace("¤", ".")
    return formatted


def _build_product_text(data: Dict[str, str]) -> Optional[str]:
    name = data.get("nome_curadobia") or data.get("nome_marca") or data.get("marca")
    brand = data.get("marca")
    sku = data.get("sku")
    categories = " > ".join(
        filter(
            None,
            (
                data.get("categoria_geral"),
                data.get("categoria"),
                data.get("sub_categoria"),
            ),
        )
    )
    price = _format_price(data.get("preco"))
    description = data.get("descricao_do_site")
    sizes = (
        data.get("tamanhos_disponiveis")
        or data.get("grade")
        or data.get("grade_completo")
    )
    measurements = data.get("medidas_por_tamanho") or data.get("medidas")
    modeling = data.get(
        "observacao_sobre_modelagem_caimento_ex_reto_acinturado_oversized"
    )
    fabric = data.get("tipo_de_tecido_material_principal")
    lining = data.get("forro_sim_nao")
    transparency = data.get("nivel_de_transparencia_ex_leve_media_zero")
    care = data.get(
        "instrucoes_de_cuidado_ex_passa_facil_nao_amassa_pode_lavar_na_maquina_peca_cede_com_uso_tecido_com_elastano"
    )
    color = data.get("cor")
    color_tags = data.get("tags_de_cores_ex_cor_que_alonga_combina_com_tudo")
    seasonality = data.get(
        "sazonalidade_sugerida_ex_ideal_para_meia_estacao_vai_bem_no_verao_com_top_por_baixo"
    )
    body_tips = data.get(
        "sugestoes_de_tamanho_por_tipo_de_corpo_ex_ideal_para_ombros_largos_quadril_estreito"
    )
    occasions = ", ".join(
        filter(
            None,
            (
                data.get("ocasiao_principal"),
                data.get("ocasiao_secundaria"),
                data.get("ocasiao"),
            ),
        )
    )
    replenishment = data.get("tempo_medio_de_reposicao")
    freight_type = data.get("tipo_de_frete")
    sedex = data.get("prazo_medio_de_envio_sedex_para_sul_e_sudeste")
    pac = data.get("prazo_medio_de_envio_pac_para_sul_e_sudeste")
    link = data.get("link_site")

    segments: List[str] = []
    if name:
        headline = name
        if brand and brand.lower() not in headline.lower():
            headline = f"{headline} da marca {brand}"
        segments.append(f"{headline}.")
    elif brand:
        segments.append(f"Produto da marca {brand}.")
    if sku:
        segments.append(f"SKU: {sku}.")
    if categories:
        segments.append(f"Categoria: {categories}.")
    if price:
        segments.append(f"Preço: {price}.")
    if description:
        segments.append(f"Descrição: {description}")
    if sizes:
        segments.append(f"Tamanhos disponíveis: {sizes}.")
    if measurements:
        segments.append(f"Medidas por tamanho: {measurements}.")
    if modeling:
        segments.append(f"Modelagem/caimento: {modeling}.")
    if fabric:
        segments.append(f"Material principal: {fabric}.")
    if lining:
        segments.append(f"Forro: {lining}.")
    if transparency:
        segments.append(f"Transparência: {transparency}.")
    if color:
        segments.append(f"Cor principal: {color}.")
    if color_tags:
        segments.append(f"Tags de cor: {color_tags}.")
    if seasonality:
        segments.append(f"Sazonalidade sugerida: {seasonality}.")
    if body_tips:
        segments.append(f"Sugestões de corpo: {body_tips}.")
    if occasions:
        segments.append(f"Ocasiões indicadas: {occasions}.")
    if replenishment:
        segments.append(f"Tempo médio de reposição: {replenishment}.")
    logistics_parts: List[str] = []
    if freight_type:
        logistics_parts.append(freight_type)
    if sedex:
        logistics_parts.append(f"SEDEX: {sedex}")
    if pac:
        logistics_parts.append(f"PAC: {pac}")
    if logistics_parts:
        segments.append(f"Logística: {' | '.join(logistics_parts)}.")
    if care:
        segments.append(f"Cuidados: {care}.")
    if link:
        segments.append(f"Link oficial: {link}.")

    text = " ".join(part.strip() for part in segments if part.strip())
    return text or None


def _parse_csv_file(path: Path) -> List[Dict[str, Any]]:
    docs: List[Dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for idx, row in enumerate(reader):
            sanitized: Dict[str, Any] = {}
            for raw_key, raw_value in row.items():
                value = _clean_csv_value(raw_value)
                if value is None:
                    continue
                key = _normalize_csv_key(raw_key)
                existing = sanitized.get(key)
                if existing is None:
                    sanitized[key] = value
                elif isinstance(existing, list):
                    if value not in existing:
                        existing.append(value)
                elif existing != value:
                    sanitized[key] = [existing, value]
            if not sanitized:
                continue
            resolved: Dict[str, str] = {}
            metadata: Dict[str, Any] = {}
            for key, stored in sanitized.items():
                if isinstance(stored, list):
                    resolved[key] = stored[0]
                    metadata[key] = ", ".join(stored)
                else:
                    resolved[key] = stored
                    metadata[key] = stored
            text = _build_product_text(resolved)
            if not text:
                continue
            doc_id = (
                resolved.get("sku")
                or resolved.get("nome_curadobia")
                or resolved.get("nome_marca")
                or f"row_{idx}"
            )
            formatted_price = _format_price(resolved.get("preco"))
            metadata["source_file"] = path.name
            if formatted_price:
                metadata["preco_formatado"] = formatted_price
            docs.append(
                {
                    "id": str(doc_id),
                    "type": "produto",
                    "text": text,
                    "metadata": metadata,
                }
            )
    return docs


def _is_product_doc(doc: Dict[str, Any]) -> bool:
    doc_type = (doc.get("type") or "").lower()
    return doc_type == "produto" or "produto" in doc_type


def _extract_highlight(text: Optional[str]) -> Optional[str]:
    if not text:
        return None
    cleaned = text.strip()
    if not cleaned:
        return None
    # Try to grab the first bullet point when available.
    bullet_parts = [part.strip() for part in cleaned.split("- ") if part.strip()]
    for part in bullet_parts:
        if part.lower().startswith("por que") or part.lower().startswith("porque"):
            continue
        sentence = re.split(r"(?<=[.!?])\s+", part)[0].strip()
        if sentence:
            sentence = sentence.rstrip(" .;!?,")
            if sentence:
                return sentence + "."
    # Fallback to the first sentence of the paragraph.
    flat = re.sub(r"\s+", " ", cleaned)
    sentence = re.split(r"(?<=[.!?])\s+", flat)[0].strip()
    if not sentence:
        return None
    sentence = sentence.rstrip(" .;!?,")
    return (sentence + ".") if sentence else None


def _format_token_list(raw: Optional[str]) -> Optional[str]:
    if not raw:
        return None
    tokens = re.split(r"[\|/,]+", raw)
    cleaned_tokens: List[str] = []
    for token in tokens:
        item = token.strip()
        if not item or item == "-":
            continue
        if item not in cleaned_tokens:
            cleaned_tokens.append(item)
    if not cleaned_tokens:
        return None
    return ", ".join(cleaned_tokens)


def _natural_join(phrases: Sequence[str]) -> str:
    items = [phrase.strip() for phrase in phrases if phrase and phrase.strip()]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    if len(items) == 2:
        return f"{items[0]} e {items[1]}"
    head = ", ".join(items[:-1])
    return f"{head} e {items[-1]}"


def _compose_product_summary(
    primary: Dict[str, Any],
    alternatives: Sequence[Dict[str, Any]],
) -> Optional[str]:
    metadata = primary.get("metadata") or {}
    name = (
        metadata.get("nome_curadobia") or primary.get("text", "").split(".")[0].strip()
    )
    brand = metadata.get("marca")
    categories = metadata.get("categoria") or metadata.get("categoria_geral")
    highlight = _extract_highlight(metadata.get("descricao_do_site"))
    price = metadata.get("preco_formatado") or _format_price(metadata.get("preco"))
    sizes = _format_token_list(
        metadata.get("tamanhos_disponiveis") or metadata.get("grade")
    )
    material = metadata.get("tipo_de_tecido_material_principal")
    color = metadata.get("cor")
    occasion = metadata.get("ocasiao_principal") or metadata.get("ocasiao")
    logistics: List[str] = []
    freight = metadata.get("tipo_de_frete")
    sedex = metadata.get("prazo_medio_de_envio_sedex_para_sul_e_sudeste")
    pac = metadata.get("prazo_medio_de_envio_pac_para_sul_e_sudeste")
    if freight:
        logistics.append(freight)
    if sedex:
        logistics.append(f"SEDEX: {sedex}")
    if pac:
        logistics.append(f"PAC: {pac}")
    link = metadata.get("link_site") or metadata.get("link")

    sentences: List[str] = []
    if name:
        headline = name
        if brand and brand.lower() not in headline.lower():
            headline = f"{headline} da marca {brand}"
        elif brand and brand.lower() in headline.lower():
            headline = headline
        if categories:
            headline = f"{headline} ({categories})"
        sentences.append(f"Recomendo {headline}.")
    elif brand:
        sentences.append(f"Encontrei uma opção interessante da marca {brand}.")

    if highlight:
        sentences.append(highlight)

    details: List[str] = []
    if price:
        details.append(f"custa {price}")
    if sizes:
        details.append(f"está disponível nos tamanhos {sizes}")
    if material:
        details.append(f"tem composição principal de {material}")
    if color:
        details.append(f"chega na cor {color}")
    if details:
        joined = _natural_join(details)
        if joined:
            sentences.append(f"Ela {joined}.")

    if occasion:
        sentences.append(f"Ideal para {occasion.lower()}.")

    if logistics:
        sentences.append(f"Envio: {' | '.join(logistics)}.")

    alt_names: List[str] = []
    for doc in alternatives:
        meta = doc.get("metadata") or {}
        alt_name = meta.get("nome_curadobia") or meta.get("nome_marca") or doc.get("id")
        if alt_name and alt_name != name and alt_name not in alt_names:
            alt_names.append(alt_name)
        if len(alt_names) >= 2:
            break
    if alt_names:
        sentences.append("Outras opções relacionadas: " + ", ".join(alt_names) + ".")

    if link:
        sentences.append(f"Veja mais detalhes em {link}.")

    if not sentences:
        return None

    # Cap response to a digestible length while preserving meaning.
    cleaned_sentences: List[str] = []
    total_chars = 0
    for sentence in sentences:
        sentence_clean = re.sub(r"\s+", " ", sentence).strip()
        if not sentence_clean:
            continue
        total_chars += len(sentence_clean)
        cleaned_sentences.append(sentence_clean)
        if len(cleaned_sentences) >= 4 or total_chars > 480:
            break
    return " ".join(cleaned_sentences)


def _render_manual_answer(
    question: str,
    hits: Sequence[Tuple[Dict[str, Any], float]],
) -> Tuple[Optional[str], Optional[str]]:
    if not hits:
        return None, None
    docs = [doc for doc, _ in hits]
    if docs and all(_is_product_doc(doc) for doc in docs):
        primary = docs[0]
        alternatives = docs[1:]
        summary = _compose_product_summary(primary, alternatives)
        if summary:
            return summary, "product_summary"
    return None, None


def _load_document_candidates(path_candidates: Sequence[Path]) -> List[Dict[str, Any]]:
    for path in path_candidates:
        if not path.exists():
            continue
        try:
            suffix = path.suffix.lower()
            if suffix == ".jsonl":
                docs = _parse_jsonl_file(path)
            elif suffix == ".json":
                docs = _parse_json_file(path)
            elif suffix == ".csv":
                docs = _parse_csv_file(path)
            else:
                continue
        except OSError as exc:
            logger.warning("Failed to read %s: %s", path, exc)
            continue
        if docs:
            logger.info("Loaded %d documents from %s", len(docs), path)
            return docs
    raise FileNotFoundError("No document store found in retriever repository")


class RagService:
    def __init__(self, *, config: Dict[str, Any]) -> None:
        self.config = config
        self._query_cache: Dict[str, np.ndarray] = {}
        self._cache_size_limit = 100  # Limitar cache a 100 queries
        cache_dir = _expand_cache_dir(CONFIG["model"].get("hf_cache_dir"))

        retriever_cfg = config.get("retriever", {})
        generator_cfg = config.get("generator", {})

        self.device = _pick_device(generator_cfg.get("device"))
        self.normalize_embeddings = bool(
            retriever_cfg.get("normalize_embeddings", True)
        )
        self.query_prefix = retriever_cfg.get("query_prefix", "")
        self.passage_prefix = retriever_cfg.get("passage_prefix", "")
        self.batch_size = int(retriever_cfg.get("batch_size", 64))
        self.top_k_default = int(retriever_cfg.get("top_k", 5))
        self.min_score = float(retriever_cfg.get("min_score", 0.0))

        self.prompt_cfg = config.get("prompt", {})

        local_assets_dir = retriever_cfg.get("local_assets_dir")
        self.local_retriever_dir: Optional[Path] = None
        if local_assets_dir:
            local_path = Path(local_assets_dir)
            if not local_path.is_absolute():
                project_root = Path(__file__).resolve().parents[2]
                local_path = (project_root / local_assets_dir).resolve()
            if local_path.exists():
                self.local_retriever_dir = local_path
            else:
                logger.warning(
                    "Configured local retriever assets dir %s does not exist",
                    local_path,
                )

        retriever_repo = retriever_cfg.get("hf_repo_id")
        generator_repo = generator_cfg.get("hf_repo_id")
        if not retriever_repo or not generator_repo:
            raise ValueError(
                "Both retriever and generator Hugging Face repos must be configured"
            )

        try:
            retriever_path = snapshot_download(
                repo_id=retriever_repo,
                cache_dir=cache_dir,
                local_files_only=False,
            )
        except Exception as exc:  # pragma: no cover - network failure surface
            raise RuntimeError(
                f"Failed to download retriever repo '{retriever_repo}': {exc}"
            ) from exc
        try:
            generator_path = snapshot_download(
                repo_id=generator_repo,
                cache_dir=cache_dir,
                local_files_only=False,
            )
        except Exception as exc:  # pragma: no cover - network failure surface
            raise RuntimeError(
                f"Failed to download generator repo '{generator_repo}': {exc}"
            ) from exc

        self.retriever_dir = Path(retriever_path)
        self.generator_dir = Path(generator_path)

        logger.info("Retriever assets loaded from %s", self.retriever_dir)
        logger.info("Generator assets loaded from %s", self.generator_dir)

        self.asset_dirs: List[Path] = [self.retriever_dir]
        if self.local_retriever_dir and self.local_retriever_dir not in self.asset_dirs:
            self.asset_dirs.append(self.local_retriever_dir)

        self.embed_model = self._init_embed_model(retriever_cfg, cache_dir)

        self.tokenizer = self._init_tokenizer(generator_cfg, cache_dir)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(
            str(self.generator_dir),
            torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
            device_map="auto" if self.device in {"cuda", "mps"} else None,
            trust_remote_code=True,
        )
        if self.device == "cpu":
            self.model = self.model.to(self.device)
        self.model.eval()

        self.documents = self._load_documents(retriever_cfg)
        self.index = self._load_or_build_index(retriever_cfg)

        self.max_new_tokens = int(generator_cfg.get("max_new_tokens", 256))
        self.temperature = float(generator_cfg.get("temperature", 0.7))
        self.top_p = float(generator_cfg.get("top_p", 0.9))

    def _init_embed_model(self, retriever_cfg: Dict[str, Any], cache_dir: str | None):
        try:
            return SentenceTransformer(str(self.retriever_dir), device=self.device)
        except TypeError as exc:
            if "word_embedding_dimension" not in str(exc):
                raise
            logger.warning(
                "SentenceTransformer snapshot missing word_embedding_dimension; using fallback encoder",
            )
        except Exception as exc:
            logger.warning(
                "Failed to load SentenceTransformer from %s: %s",
                self.retriever_dir,
                exc,
            )

        fallback_model_id = (
            retriever_cfg.get("hf_model_id")
            or retriever_cfg.get("fallback_hf_model_id")
            or CONFIG.get("embedding", {}).get("hf_model_id")
        )
        if not fallback_model_id:
            raise RuntimeError(
                "RAG retriever requires 'hf_model_id' (or fallback_hf_model_id) when SentenceTransformer snapshot is incomplete"
            )
        pooling = retriever_cfg.get("pooling") or CONFIG.get("embedding", {}).get(
            "pooling", "mean"
        )
        max_length = int(
            retriever_cfg.get("max_length")
            or CONFIG.get("embedding", {}).get("max_length", 128)
        )
        logger.info(
            "Using fallback transformer encoder %s (pooling=%s, max_length=%s)",
            fallback_model_id,
            pooling,
            max_length,
        )
        return _HFEncoder(
            fallback_model_id,
            device=self.device,
            pooling=pooling,
            max_length=max_length,
            cache_dir=cache_dir,
        )

    def _init_tokenizer(self, generator_cfg: Dict[str, Any], cache_dir: str | None):
        tokenizer_kwargs: Dict[str, Any] = {"trust_remote_code": True}
        snapshot_path = str(self.generator_dir)
        try:
            return AutoTokenizer.from_pretrained(snapshot_path, **tokenizer_kwargs)
        except Exception as exc:
            logger.warning(
                "Failed to load tokenizer from generator snapshot %s: %s",
                snapshot_path,
                exc,
            )

        tokenizer_json = self.generator_dir / "tokenizer.json"
        if tokenizer_json.exists():
            try:
                logger.info(
                    "Retrying tokenizer load using tokenizer.json from snapshot"
                )
                return AutoTokenizer.from_pretrained(
                    snapshot_path,
                    tokenizer_file=str(tokenizer_json),
                    use_fast=False,
                    **tokenizer_kwargs,
                )
            except Exception as exc:
                logger.warning("Tokenizer retry with tokenizer.json failed: %s", exc)

        fallback_repo = generator_cfg.get("tokenizer_repo_id")
        if not fallback_repo:
            raise RuntimeError(
                "Tokenizer assets missing from generator snapshot and no 'tokenizer_repo_id' configured for fallback"
            )

        logger.info("Falling back to tokenizer repo %s", fallback_repo)
        try:
            return AutoTokenizer.from_pretrained(
                fallback_repo,
                cache_dir=cache_dir,
                **tokenizer_kwargs,
            )
        except Exception as fallback_exc:  # pragma: no cover - configuration error
            raise RuntimeError(
                f"Failed to load tokenizer from both generator snapshot and fallback repo '{fallback_repo}': {fallback_exc}"
            ) from fallback_exc

    def _load_documents(self, retriever_cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
        explicit = retriever_cfg.get("documents_file")
        candidates: List[Path] = []
        default_names = (
            "documents.jsonl",
            "corpus.jsonl",
            "docs.jsonl",
            "documents.json",
            "corpus.json",
            "docs.json",
        )
        for base_dir in self.asset_dirs:
            if explicit:
                cand = base_dir / explicit
                if cand not in candidates:
                    candidates.append(cand)
            for name in default_names:
                cand = base_dir / name
                if cand not in candidates:
                    candidates.append(cand)
        docs = _load_document_candidates(candidates)
        if not docs:
            raise RuntimeError("Document store is empty; cannot build retriever")
        return docs

    def _load_or_build_index(self, retriever_cfg: Dict[str, Any]) -> faiss.Index:
        explicit = retriever_cfg.get("index_file")
        candidates: List[Path] = []
        default_names = ("index.faiss", "faiss.index", "index.bin")
        for base_dir in self.asset_dirs:
            if explicit:
                cand = base_dir / explicit
                if cand not in candidates:
                    candidates.append(cand)
            for name in default_names:
                cand = base_dir / name
                if cand not in candidates:
                    candidates.append(cand)

        for path in candidates:
            if path.exists():
                logger.info("Loading FAISS index from %s", path)
                try:
                    return faiss.read_index(str(path))
                except Exception as exc:
                    logger.warning("Failed to read index %s: %s", path, exc)

        logger.info("No FAISS index found; building in-memory index from documents")
        texts = [self.passage_prefix + doc["text"] for doc in self.documents]
        embeddings = self.embed_model.encode(
            texts,
            batch_size=self.batch_size,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=False,
        )
        if self.normalize_embeddings:
            embeddings = _normalize_embeddings(embeddings)
        embeddings = embeddings.astype("float32")
        index = faiss.IndexFlatIP(embeddings.shape[1])
        index.add(embeddings)
        return index

    def _format_context_block(self, docs: Sequence[Dict[str, Any]]) -> str:
        prefix_map = self.prompt_cfg.get("context_prefixes", {})
        lines = []
        for doc in docs:
            doc_type = doc.get("type", "default")
            prefix = prefix_map.get(doc_type, prefix_map.get("default", "CONTEUDO"))
            lines.append(f"[{prefix}] {doc['text']}")
        return "\n".join(lines)

    def _format_prompt(
        self, question: str, docs: Sequence[Dict[str, Any]], user_name: Optional[str]
    ) -> str:
        system_template = self.prompt_cfg.get(
            "system", "Você é uma consultora de moda."
        )
        default_user = self.prompt_cfg.get("default_user_name", "cliente")
        system_prompt = system_template.format(user_name=user_name or default_user)
        context_instruction = self.prompt_cfg.get(
            "context_instruction", "Responda com base no contexto."
        )

        ambiguity_instruction = (
            "IMPORTANTE: Se a pergunta for vaga, imprecisa ou muito genérica (como 'me ajude', 'preciso de algo', "
            "'quero comprar', 'tem alguma coisa?', 'me recomende'), você deve responder EXATAMENTE assim: "
            "'PERGUNTA_AMBIGUA: Para te ajudar melhor, preciso de mais detalhes. Que tipo de produto você está procurando? "
            "Tem alguma ocasião específica em mente? Qual seu estilo preferido?' "
            "Caso contrário, responda normalmente com base no contexto."
        )

        context_block = self._format_context_block(docs)
        return (
            f"<system>{system_prompt}</system>\n"
            f"<context>{context_block}</context>\n"
            f"<instruction>{context_instruction}</instruction>\n"
            f"<ambiguity>{ambiguity_instruction}</ambiguity>\n"
            f"<question>{question}</question>\n"
            f"<answer>"
        )

    def _extract_answer(
        self, prompt_ids: torch.Tensor, output_ids: torch.Tensor
    ) -> str:
        prompt_len = prompt_ids.shape[-1]
        generated = output_ids[0][prompt_len:]
        if generated.numel() == 0:
            generated = output_ids[0]
        text = self.tokenizer.decode(generated, skip_special_tokens=True)
        return text.strip()

    def _run_generator(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        with torch.no_grad():
            output_ids = self.model.generate(
                **inputs,
                max_new_tokens=self.max_new_tokens,
                do_sample=True,
                temperature=self.temperature,
                top_p=self.top_p,
                pad_token_id=self.tokenizer.eos_token_id,
                eos_token_id=self.tokenizer.eos_token_id,
            )
        raw = self._extract_answer(inputs["input_ids"], output_ids)
        return self._clean_answer(raw)

    def _get_query_hash(self, query: str) -> str:
        """Gera hash para cache de query."""
        return hashlib.md5(query.encode("utf-8")).hexdigest()

    def _get_cached_embedding(self, query: str) -> Optional[np.ndarray]:
        """Recupera embedding do cache se disponível."""
        query_hash = self._get_query_hash(query)
        return self._query_cache.get(query_hash)

    def _cache_embedding(self, query: str, embedding: np.ndarray) -> None:
        """Salva embedding no cache."""
        if len(self._query_cache) >= self._cache_size_limit:
            # Remove item mais antigo (FIFO simples)
            oldest_key = next(iter(self._query_cache))
            del self._query_cache[oldest_key]

        query_hash = self._get_query_hash(query)
        self._query_cache[query_hash] = embedding.copy()

    def _clean_answer(self, text: str) -> str:
        cleaned = text

        # Remove prompt sections that the model might have echoed
        prompt_sections = [
            "<system>",
            "<context>",
            "<instruction>",
            "<question>",
            "<answer>",
            "<ambiguity>",
            "Contexto:",
            "Usuário:",
            "Usúario:",
            "Usúrio:",
            "Usúrio:",
        ]

        for section in prompt_sections:
            if section in cleaned:
                # Remove everything from the section onwards
                cleaned = cleaned.split(section)[0]

        # Remove residual XML-like markers
        replacements = {
            "<answer>": "",
            "</answer>": "",
            "<question>": "",
            "</question>": "",
            "<context>": "",
            "</context>": "",
            "<instruction>": "",
            "</instruction>": "",
            "<system>": "",
            "</system>": "",
            "<ambiguity>": "",
            "</ambiguity>": "",
        }

        for old, new in replacements.items():
            cleaned = cleaned.replace(old, new)

        # Remove common prompt patterns and personalization
        import re

        # Remove ALL personalization patterns aggressively
        personalization_patterns = [
            r"^.*?(Que bom continuar|Vi que na última conversa).*?(?=Contexto:|$)",
            r"Você comentou:.*?(?=Contexto:|$)",
            r"^.*?Contexto:\s*",
            r"^.*?(Contexto:|Usuário:|Usúario:|Usúrio:).*$",
            r"^.*?(Oi! Tudo bem|Aqui é do time Curadobia).*?(?=Contexto:|$)",
            r"Ainda não.*?(?=Contexto:|$)",
        ]

        for pattern in personalization_patterns:
            cleaned = re.sub(pattern, "", cleaned, flags=re.MULTILINE | re.DOTALL)

        # Find the actual answer content after removing all personalization
        # Look for content that starts with "Para" or similar product descriptions
        answer_match = re.search(
            r"(Para.*?|Recomendo.*?|A.*?é.*?|Considerando.*?)(?:\n|$)",
            cleaned,
            flags=re.MULTILINE | re.DOTALL,
        )
        if answer_match:
            cleaned = answer_match.group(1).strip()

        # Strip whitespace and duplicated newlines
        cleaned = "\n".join(line.rstrip() for line in cleaned.splitlines()).strip()

        return cleaned

    def _retrieve(
        self, question: str, top_k: Optional[int] = None
    ) -> List[Tuple[Dict[str, Any], float]]:
        if top_k is None:
            top_k = self.top_k_default
        query = self.query_prefix + question

        # Tentar usar embedding do cache
        query_vec = self._get_cached_embedding(query)

        if query_vec is None:
            # Computar embedding se não estiver no cache
            query_vec = self.embed_model.encode(
                [query],
                batch_size=1,
                show_progress_bar=False,
                convert_to_numpy=True,
                normalize_embeddings=False,
            )
            if self.normalize_embeddings:
                query_vec = _normalize_embeddings(query_vec)

            # Salvar no cache
            self._cache_embedding(query, query_vec)

        query_vec = query_vec.astype("float32")
        distances, indices = self.index.search(query_vec, top_k)
        hits: List[Tuple[Dict[str, Any], float]] = []
        for idx, score in zip(indices[0].tolist(), distances[0].tolist()):
            if idx < 0 or idx >= len(self.documents):
                continue
            doc = dict(self.documents[idx])
            hits.append((doc, float(score)))
        return hits

    def generate(
        self,
        question: str,
        *,
        user_name: Optional[str] = None,
        top_k: Optional[int] = None,
    ) -> Dict[str, Any]:
        hits = self._retrieve(question, top_k)
        docs = [doc for doc, _ in hits]
        prompt = self._format_prompt(question, docs, user_name)
        manual_answer, answer_source = _render_manual_answer(question, hits)
        if manual_answer:
            answer = manual_answer
            answer_source = answer_source or "manual"
        else:
            answer = self._run_generator(prompt)
            answer_source = "generator"
        scores = [score for _, score in hits]
        max_score = max(scores) if scores else None
        sufficient_context = bool(scores) and (
            max_score is None or max_score >= self.min_score
        )
        return {
            "question": question,
            "answer": answer,
            "prompt": prompt,
            "answer_source": answer_source,
            "contexts": [
                {
                    "id": doc.get("id"),
                    "type": doc.get("type"),
                    "text": doc.get("text"),
                    "score": score,
                }
                for doc, score in hits
            ],
            "context_count": len(docs),
            "scores": scores,
            "max_score": max_score,
            "score_threshold": self.min_score,
            "sufficient_context": sufficient_context,
        }


def get_rag_service() -> RagService:
    rag_cfg = CONFIG.get("rag") or {}
    return RagService(config=rag_cfg)
