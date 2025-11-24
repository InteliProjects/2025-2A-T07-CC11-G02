import logging
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from ..core.config import CONFIG
from ..repositories.db import init_db
from ..repositories.interactions_repo import (
    InteractionCreate,
    get_recent_interactions,
    log_interaction,
)
from ..repositories.users_repo import UserCreate, create_user, get_user_by_external_id
from ..services.router import route_text
from .users_api import router as users_router

logger = logging.getLogger(__name__)


app = FastAPI(title="Intent Chatbot", version="1.0.0")

# Enable permissive CORS by default (customize as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    text: str = Field(min_length=1, description="User message to route")
    external_id: str | None = Field(
        default=None, description="External user id for personalization"
    )


@app.get("/")
@app.get("/healthz")
async def health() -> dict[str, Any]:
    return {
        "status": "ok",
        "endpoints": {"POST /chat": {"body": {"text": "string"}}},
    }


@app.post("/chat")
async def chat(req: ChatRequest) -> dict[str, Any]:
    original_name = CONFIG.get("user", {}).get("name")
    user = None
    history_payload: list[dict[str, Any]] = []
    user_id: int | None = None
    history_records: list[Any] = []
    try:
        if req.external_id:
            user = get_user_by_external_id(req.external_id)
            if not user:
                try:
                    user = create_user(UserCreate(external_id=req.external_id))
                except Exception as exc:  # pragma: no cover - defensive logging
                    logger.debug(
                        "Could not auto-create user for external_id %s: %s",
                        req.external_id,
                        exc,
                    )
                    user = get_user_by_external_id(req.external_id)
            if user:
                user_id = user.id
                preferred = user.preferred_name or user.name
                if preferred:
                    CONFIG.setdefault("user", {})["name"] = preferred
        if user_id is not None:
            history_records = get_recent_interactions(user_id=user_id, limit=5)
        elif req.external_id:
            history_records = get_recent_interactions(
                external_id=req.external_id, limit=5
            )
        else:
            history_records = []
        history_payload = [
            {
                "intent": record.intent,
                "input_text": record.input_text,
                "response_text": record.response_text,
                "created_at": record.created_at,
            }
            for record in history_records
        ]
        routing_result = route_text(req.text, history=history_payload)
    finally:
        # restore original global config name to avoid cross-request leakage
        if original_name is not None:
            CONFIG.setdefault("user", {})["name"] = original_name
    intent_label: str | None = None
    if isinstance(routing_result, dict):
        response_payload: dict[str, Any] = {
            "response": routing_result.get("response", "")
        }
        intent_label = routing_result.get("intent")
        if intent_label is not None:
            response_payload["intent"] = intent_label
        metadata = routing_result.get("metadata")
        if metadata:
            response_payload["metadata"] = metadata
    else:
        response_payload = {"response": str(routing_result)}

    try:
        log_interaction(
            InteractionCreate(
                user_id=user_id,
                external_id=req.external_id,
                input_text=req.text,
                response_text=response_payload.get("response", ""),
                intent=intent_label,
                metadata=routing_result.get("metadata")
                if isinstance(routing_result, dict)
                else None,
            )
        )
    except Exception as exc:  # pragma: no cover - defensive logging
        logger.warning("Failed to log interaction: %s", exc)
    return response_payload


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)


# FastAPI lifecycle hooks
@app.on_event("startup")
def _startup_init_db() -> None:
    init_db()


# Routers
app.include_router(users_router)
