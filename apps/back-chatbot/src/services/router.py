import importlib.util
import logging
import os
import re
import sys
import types
import unicodedata
from typing import Any, Dict, List, Optional, Type

from ..core import config as config_module
from ..ml.intent import (
    Agradecimento,
    Confirmacao,
    DuvidaProduto,
    EventoPresencial,
    Intent,
    InteresseProduto,
    MensagemSistema,
    NaoIdentificado,
    ParceriaComercial,
    ProblemaTecnico,
    RastreamentoPedido,
    ReaçãoEmocional,
    ReposicaoEstoque,
    Saudacao,
    SolicitaçãoInformação,
    SolititacaoContato,
    TrocaDevolucao,
)
from .rag_service import get_rag_service

logger = logging.getLogger(__name__)


_FRIENDLY_LABEL_MAP: Dict[str, str] = {
    "duvida_produto": "suas dúvidas sobre produtos",
}


def _load_intent_classifier_module() -> types.ModuleType:
    """
    Dynamically load the classifier module from `intent-classifier.py`,
    handling the hyphen in the filename and the internal import path
    `my_proj.config` used by that file.
    """
    # Ensure the classifier's internal import "my_proj.config" resolves to our config module
    sys.modules.setdefault("my_proj.config", config_module)

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    classifier_path = os.path.join(base_dir, "ml", "intent_classifier.py")

    spec = importlib.util.spec_from_file_location(
        "intent_classifier_mod", classifier_path
    )
    if spec is None or spec.loader is None:
        raise ImportError(
            f"Unable to create spec for classifier module at: {classifier_path}"
        )

    module = importlib.util.module_from_spec(spec)
    sys.modules["intent_classifier_mod"] = module
    spec.loader.exec_module(module)  # type: ignore[attr-defined]
    return module


def _normalize_label(label: str) -> str:
    """Normalize labels to a comparable, ASCII-only, lowercased form."""
    # Lowercase first
    lowered = label.lower()
    # NFKD decomposition and strip diacritics
    decomposed = unicodedata.normalize("NFKD", lowered)
    ascii_only = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    # Normalize whitespace/joins
    ascii_only = ascii_only.replace(" ", "_")
    return ascii_only


class Router:
    """
    Routes an input text to the correct intent handler based on the
    predicted label returned by the intent classifier.
    """

    def __init__(self, classifier: Optional[object] = None) -> None:
        if classifier is None:
            classifier_mod = _load_intent_classifier_module()
            IntentClassifier = getattr(classifier_mod, "IntentClassifier")
            self.classifier = IntentClassifier(
                hf_repo_id=config_module.CONFIG["model"]["hf_repo_id"]
            )
        else:
            self.classifier = classifier

        # Map normalized labels to intent classes
        self.label_to_intent: Dict[str, Type[Intent]] = {
            _normalize_label("saudação"): Saudacao,
            _normalize_label("saudacao"): Saudacao,  # ASCII fallback
            _normalize_label("duvida_produto"): DuvidaProduto,
            _normalize_label("solicitacao_informacao"): SolicitaçãoInformação,
            _normalize_label("reacao_emocional"): ReaçãoEmocional,
            _normalize_label("interesse_produto"): InteresseProduto,
            _normalize_label("agradecimento"): Agradecimento,
            _normalize_label("rastreamento_pedido"): RastreamentoPedido,
            _normalize_label("solicitacao_contato"): SolititacaoContato,
            _normalize_label("mensagem_sistema"): MensagemSistema,
            _normalize_label("troca_devolucao"): TrocaDevolucao,
            _normalize_label("problema_tecnico"): ProblemaTecnico,
            _normalize_label("nao_identificado"): NaoIdentificado,
            _normalize_label("reposicao_estoque"): ReposicaoEstoque,
            _normalize_label("confirmacao"): Confirmacao,
            _normalize_label("parceria_comercial"): ParceriaComercial,
            _normalize_label("evento_presencial"): EventoPresencial,
        }

    def route(
        self, text: str, history: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, Any]:
        """Predict intent, dispatch handler, and optionally enrich with RAG."""
        history = history or []
        pred = self.classifier.predict(text)
        predicted_label: str = pred.get("predicted_label", "")
        normalized = _normalize_label(predicted_label)

        metadata: Dict[str, Any] = {
            "classifier": {
                "predicted_label": predicted_label,
                "predicted_class": pred.get("predicted_class"),
                "score": pred.get("score"),
            }
        }

        intent_cls = self.label_to_intent.get(normalized)
        if intent_cls is None:
            response_text = (
                "Desculpe, ainda não entendi sua solicitação. Pode reformular ou, se preferir, "
                "posso acionar alguém do time para falar com você."
            )
            metadata["rag"] = {"used": False}
            metadata["fallback"] = {"type": "unknown_intent"}
            return {
                "response": response_text,
                "intent": predicted_label or None,
                "metadata": metadata,
            }

        intent_instance = intent_cls()
        setattr(intent_instance, "history", history)
        response_text = intent_instance.response
        rag_payload: Dict[str, Any] | None = None
        rag_error: str | None = None
        rag_used = False
        fallback_triggered = False
        fallback_reason: str | None = None

        if intent_instance.should_use_rag():
            try:
                rag_service = get_rag_service()
                question = intent_instance.prepare_rag_question(text)
                rag_payload = rag_service.generate(
                    question,
                    user_name=intent_instance.get_name(),
                )
                answer = (rag_payload or {}).get("answer")
                sufficient_context = bool(
                    (rag_payload or {}).get("sufficient_context", True)
                )

                # Verifica se a resposta indica uma pergunta ambígua
                if answer and answer.startswith("PERGUNTA_AMBIGUA:"):
                    # Remove o prefixo e usa como resposta de esclarecimento
                    clarification_response = answer.replace(
                        "PERGUNTA_AMBIGUA:", ""
                    ).strip()
                    response_text = clarification_response
                    rag_used = True
                    # Adiciona metadados específicos para ambiguidade
                    metadata["ambiguity_detection"] = {
                        "detected": True,
                        "original_question": question,
                        "clarification_requested": True,
                    }
                elif answer and sufficient_context:
                    response_text = answer
                    rag_used = True
                    metadata["ambiguity_detection"] = {"detected": False}
                else:
                    fallback_reason = (
                        "no_context" if not sufficient_context else "empty_answer"
                    )
                    response_text = intent_instance.smart_fallback(
                        text, reason=fallback_reason
                    )
                    fallback_triggered = True
                    metadata["ambiguity_detection"] = {"detected": False}
            except Exception as exc:  # pragma: no cover - defensive logging
                rag_error = str(exc)
                logger.exception(
                    "Failed to generate RAG answer for intent '%s': %s",
                    predicted_label,
                    exc,
                )
                fallback_reason = "rag_error"
                response_text = intent_instance.smart_fallback(
                    text, reason=fallback_reason
                )
                fallback_triggered = True
                metadata["ambiguity_detection"] = {"detected": False, "error": str(exc)}

        rag_metadata: Dict[str, Any] = {"used": rag_used}
        if rag_payload:
            rag_metadata["question"] = rag_payload.get("question")
            rag_metadata["contexts"] = rag_payload.get("contexts")
            if rag_payload.get("context_count") is not None:
                rag_metadata["context_count"] = rag_payload.get("context_count")
            if rag_payload.get("max_score") is not None:
                rag_metadata["max_score"] = rag_payload.get("max_score")
            if rag_payload.get("score_threshold") is not None:
                rag_metadata["score_threshold"] = rag_payload.get("score_threshold")
            if rag_payload.get("scores"):
                rag_metadata["scores"] = rag_payload.get("scores")
            if not rag_payload.get("sufficient_context", True):
                rag_metadata["insufficient_context"] = True
        if rag_error:
            rag_metadata["error"] = rag_error
        if not rag_used and fallback_triggered:
            rag_metadata["fallback_reason"] = fallback_reason
        metadata["rag"] = rag_metadata

        # Personalização removida para evitar confusão - apenas resposta limpa do RAG

        if fallback_triggered:
            metadata["fallback"] = {
                "type": "rag",
                "reason": fallback_reason,
            }

        return {
            "response": response_text,
            "intent": predicted_label or intent_instance.__class__.__name__,
            "metadata": metadata,
        }

    def _build_personalization(
        self, history: List[Dict[str, Any]], current_label: Optional[str]
    ) -> str:
        if not history:
            return ""
        last = history[0]
        last_intent = last.get("intent")
        if not last_intent:
            return ""
        friendly_last = self._friendly_intent_name(last_intent)
        if not friendly_last:
            return ""
        note: str
        if current_label and self._normalize_label_safe(
            last_intent
        ) == _normalize_label(current_label):
            note = f"Que bom continuar te ajudando com {friendly_last}."
        else:
            note = f"Vi que na última conversa falamos sobre {friendly_last}."
        last_input = (last.get("input_text") or "").strip()
        if last_input:
            excerpt = self._extract_highlight(last_input)
            if excerpt:
                excerpt = re.sub(
                    r"^você comentou:\s*", "", excerpt, flags=re.IGNORECASE
                ).strip()
                normalized_note = note.lower()
                normalized_excerpt = excerpt.lower()
                if not normalized_excerpt.startswith(normalized_note) and excerpt:
                    note += f" Você comentou: {excerpt}"
        return note.strip()

    @staticmethod
    def _normalize_label_safe(label: str) -> str:
        try:
            return _normalize_label(label)
        except Exception:
            return label.lower()

    @staticmethod
    def _friendly_intent_name(label: str) -> str:
        normalized = label.strip().lower()
        mapped = _FRIENDLY_LABEL_MAP.get(normalized)
        if mapped:
            return mapped.strip()
        cleaned = label.replace("_", " ").strip()
        if not cleaned:
            return ""
        return cleaned.capitalize()

    @staticmethod
    def _strip_personalization_intro(text: str) -> str:
        stripped = text.strip()
        lowered = stripped.lower()
        intro_phrases = (
            "que bom continuar te ajudando",
            "vi que na última conversa",
        )
        for phrase in intro_phrases:
            if lowered.startswith(phrase):
                parts = stripped.split(".", 1)
                if len(parts) == 2:
                    return parts[1].strip()
                return ""
        return stripped

    @staticmethod
    def _extract_highlight(text: str, max_len: int = 120) -> str:
        collapsed = " ".join(text.split())
        if len(collapsed) <= max_len:
            return collapsed
        truncated = collapsed[: max_len - 3].rstrip()
        # avoid cutting mid-word
        if " " in truncated:
            truncated = truncated.rsplit(" ", 1)[0]
        return f"{truncated}..."


# Lazy singleton to avoid heavy model load on import
_router_singleton: Optional[Router] = None


def route_text(
    text: str, history: Optional[List[Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """Route `text` using a shared Router instance and return metadata."""
    global _router_singleton
    if _router_singleton is None:
        _router_singleton = Router()
    return _router_singleton.route(text, history=history)


if __name__ == "__main__":
    # Simple CLI for manual testing
    try:
        while True:
            user_text = input("Você: ").strip()
            if not user_text:
                continue
            if user_text.lower() in {"sair", "quit", "exit"}:
                print("Bot: Até logo!")
                break
            result = route_text(user_text)
            response = result.get("response") if isinstance(result, dict) else result
            print(f"Bot: {response}")
    except (KeyboardInterrupt, EOFError):
        print("\nBot: Até logo!")
