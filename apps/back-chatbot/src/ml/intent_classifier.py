import json
import os
from pathlib import Path
from typing import Literal

import numpy as np
import torch
from huggingface_hub import snapshot_download

# Optional deps; import lazily inside loaders
# import torch
# from transformers import AutoTokenizer, AutoModelForSequenceClassification


def _read_config_if_any(path: str) -> dict:
    cfg_path = os.path.join(path, "config.json")
    if os.path.isfile(cfg_path):
        with open(cfg_path, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except Exception:
                return {}
    return {}


def _detect_backend(path: str) -> Literal["transformers", "sklearn"]:
    p = Path(path)
    # Transformers artifacts
    tf_markers = [
        p / "pytorch_model.bin",
        p / "model.safetensors",
        p / "tf_model.h5",
    ]
    tok_markers = [
        p / "tokenizer.json",
        p / "vocab.txt",
        p / "merges.txt",
        p / "sentencepiece.bpe.model",
        p / "spiece.model",
    ]
    if any(m.exists() for m in tf_markers) and any(m.exists() for m in tok_markers):
        return "transformers"
    # scikit-learn artifacts
    if list(p.glob("*.pkl")) or list(p.glob("*.joblib")) or list(p.glob("*.skops")):
        return "sklearn"
    # Fallback: if there is only a single large file that ends with .pkl it is very likely sklearn
    return "sklearn"


def _find_sklearn_file(path: str) -> str | None:
    p = Path(path)
    cands = list(p.glob("*.skops")) or list(p.glob("*.pkl")) or list(p.glob("*.joblib"))
    if not cands:
        return None
    # Prefer the file that looks like the intent model
    for name in ("modelo_classificacao_intencoes", "intent", "model"):
        for c in cands:
            if name in c.name:
                return str(c)
    # Else the largest file
    return str(sorted(cands, key=lambda x: x.stat().st_size, reverse=True)[0])


class IntentClassifier:
    """
    Loads an intent model from:
      - a Hugging Face Transformers repo, or
      - a scikit-learn pipeline saved as .pkl/.joblib/.skops

    Unified API: predict(str) and predict_batch(list[str]).
    """

    def __init__(
        self,
        model_path: str | None = None,
        *,
        hf_repo_id: str | None = None,
        revision: str | None = None,
        force_download: bool = False,
        device: str | None = None,  # used only for Transformers
        prefer_backend: Literal["auto", "transformers", "sklearn"] = "auto",
        cache_dir: str | None = None,
    ):
        # Resolve path: local vs HF
        if model_path is None:
            if not hf_repo_id:
                raise ValueError("Provide either model_path or hf_repo_id.")
            # download a local snapshot
            model_path = snapshot_download(
                repo_id=hf_repo_id,
                revision=revision,
                cache_dir=cache_dir or None,
                local_files_only=False,
                ignore_patterns=["*.pt", "*.bin"]
                if prefer_backend == "sklearn"
                else None,  # optional optimization
            )

        self.root = model_path
        self.cfg = _read_config_if_any(self.root)

        # Decide backend
        backend = (
            _detect_backend(self.root) if prefer_backend == "auto" else prefer_backend
        )
        self.backend = backend

        # Load model by backend
        if backend == "transformers":
            # Lazy imports to avoid hard dep when not needed
            import torch
            from transformers import AutoModelForSequenceClassification, AutoTokenizer

            if device is None:
                if torch.cuda.is_available():
                    device = "cuda"
                elif (
                    hasattr(torch.backends, "mps") and torch.backends.mps.is_available()
                ):
                    device = "mps"
                else:
                    device = "cpu"
            self._torch = torch
            self.device = torch.device(device)

            self.tokenizer = AutoTokenizer.from_pretrained(self.root)
            self.model = (
                AutoModelForSequenceClassification.from_pretrained(
                    self.root, trust_remote_code=False
                )
                .to(self.device)
                .eval()
            )

            # label mapping
            id2label = getattr(self.model.config, "id2label", None) or self.cfg.get(
                "id2label"
            )
            if id2label:
                self.id2label = {int(k): v for k, v in id2label.items()}
            else:
                num_labels = int(getattr(self.model.config, "num_labels", 0) or 0)
                self.id2label = {i: f"label_{i}" for i in range(num_labels)}
            self.label2id = {v: k for k, v in self.id2label.items()}

        elif backend == "sklearn":
            model_file = _find_sklearn_file(self.root)
            if not model_file:
                raise FileNotFoundError("No .pkl/.joblib/.skops found in model dir")
            import joblib

            self.pipeline = joblib.load(model_file)

            # --- label mapping ---
            self._classes = None
            if hasattr(self.pipeline, "classes_"):
                self._classes = list(self.pipeline.classes_)

            if self._classes and isinstance(self._classes[0], str):
                self.id2label = {i: c for i, c in enumerate(self._classes)}
            else:
                self.id2label = {
                    int(k): v for k, v in (self.cfg.get("id2label") or {}).items()
                }
            self.label2id = {v: k for k, v in self.id2label.items()}

            # --- embedder (for raw text -> vector) ---
            # read from config, with sensible defaults
            emb_cfg = self.cfg.get("embedding") or {}
            self.embed_model_id = emb_cfg.get(
                "hf_model_id", "neuralmind/bert-base-portuguese-cased"
            )
            self.pooling = emb_cfg.get("pooling", "mean")  # "cls" or "mean"
            self.max_length = int(emb_cfg.get("max_length", 128))

            import torch
            from transformers import AutoModel, AutoTokenizer

            # device
            if device is None:
                if torch.cuda.is_available():
                    device = "cuda"
                elif (
                    hasattr(torch.backends, "mps") and torch.backends.mps.is_available()
                ):
                    device = "mps"
                else:
                    device = "cpu"
            self._torch = torch
            self.device = torch.device(device)

            self.tok = AutoTokenizer.from_pretrained(self.embed_model_id)
            self.enc_model = (
                AutoModel.from_pretrained(self.embed_model_id).to(self.device).eval()
            )

            # keep flags
            self._sk_has_proba = hasattr(self.pipeline, "predict_proba")

    @torch.inference_mode()
    def _embed_texts(self, texts: list[str]) -> np.ndarray:
        torch = self._torch
        enc = self.tok(
            texts,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=self.max_length,
        )
        enc = {k: v.to(self.device) for k, v in enc.items()}
        out = self.enc_model(**enc)
        last_hidden = out.last_hidden_state  # [B, T, H]
        if self.pooling == "mean":
            mask = enc["attention_mask"].unsqueeze(-1)  # [B, T, 1]
            summed = (last_hidden * mask).sum(dim=1)
            counts = mask.sum(dim=1).clamp(min=1)
            pooled = summed / counts
        else:  # "cls"
            pooled = last_hidden[:, 0, :]
        return pooled.detach().cpu().numpy()

    def _idx_to_slug(self, idx: int) -> str:
        # prefer classes_ if they are strings
        if self._classes and isinstance(self._classes[0], str):
            return self._classes[idx]
        if self.id2label:
            return self.id2label[idx]
        return f"label_{idx}"

    # ---------- Public API ----------
    def predict(self, text: str, max_length: int = 256):
        # If someone gave us a numeric feature vector, accept it as-is
        if isinstance(text, (list, tuple, np.ndarray)) and np.array(text).ndim == 1:
            X = np.array([text])
        else:
            X = self._embed_texts([text])

        # optional sanity check on expected feature size
        if hasattr(self.pipeline, "n_features_in_"):
            n_expected = int(self.pipeline.n_features_in_)
            if X.shape[1] != n_expected:
                raise ValueError(
                    f"Embedding dim {X.shape[1]} != classifier expects {n_expected}. "
                    f"Check embedding model/pooling/max_length."
                )

        if self._sk_has_proba:
            p = self.pipeline.predict_proba(X)[0]
            cid = int(np.argmax(p))
            slug = self._idx_to_slug(cid)
            score = float(p[cid])
        else:
            y = self.pipeline.predict(X)[0]
            # y may be an index or a string; normalize to index
            if isinstance(y, str):
                cid = self._classes.index(y) if self._classes else int(self.label2id[y])
            else:
                cid = int(y)
            slug = self._idx_to_slug(cid)
            score = None

        return {
            "text": text if isinstance(text, str) else "<vector>",
            "predicted_class": cid,
            "predicted_label": slug,
            "score": score,
            "original_id": cid + 1,
        }

    def predict_batch(self, texts: list[str], max_length: int = 256):
        # If already vectors, stack; else embed
        if len(texts) and isinstance(texts[0], (list, tuple, np.ndarray)):
            X = np.array(texts)
        else:
            X = self._embed_texts(texts)

        if hasattr(self.pipeline, "n_features_in_"):
            n_expected = int(self.pipeline.n_features_in_)
            if X.shape[1] != n_expected:
                raise ValueError(
                    f"Embedding dim {X.shape[1]} != classifier expects {n_expected}."
                )

        outs = []
        if self._sk_has_proba:
            P = self.pipeline.predict_proba(X)
            for t, p in zip(texts, P):
                cid = int(np.argmax(p))
                outs.append(
                    {
                        "text": t if isinstance(t, str) else "<vector>",
                        "predicted_class": cid,
                        "predicted_label": self._idx_to_slug(cid),
                        "score": float(p[cid]),
                        "original_id": cid + 1,
                    }
                )
        else:
            Y = self.pipeline.predict(X)
            for t, y in zip(texts, Y):
                if isinstance(y, str):
                    cid = (
                        self._classes.index(y)
                        if self._classes
                        else int(self.label2id[y])
                    )
                else:
                    cid = int(y)
                outs.append(
                    {
                        "text": t if isinstance(t, str) else "<vector>",
                        "predicted_class": cid,
                        "predicted_label": self._idx_to_slug(cid),
                        "score": None,
                        "original_id": cid + 1,
                    }
                )
        return outs
