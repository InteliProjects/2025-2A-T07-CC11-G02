from __future__ import annotations

import json
from datetime import datetime
from typing import Any, Optional

from pydantic import BaseModel, Field

from .db import get_connection


class InteractionCreate(BaseModel):
    user_id: Optional[int] = None
    external_id: Optional[str] = None
    input_text: str
    response_text: str
    intent: Optional[str] = None
    metadata: Optional[dict[str, Any]] = None
    created_at: Optional[str] = Field(
        default=None, description="ISO timestamp override"
    )


class InteractionOut(BaseModel):
    id: int
    user_id: Optional[int] = None
    external_id: Optional[str] = None
    input_text: str
    response_text: str
    intent: Optional[str] = None
    metadata: Optional[dict[str, Any]] = None
    created_at: str

    @classmethod
    def from_row(cls, row) -> "InteractionOut":
        metadata_raw = row["metadata"]
        metadata = None
        if metadata_raw:
            try:
                metadata = json.loads(metadata_raw)
            except json.JSONDecodeError:
                metadata = {"raw": metadata_raw}
        return cls(
            id=row["id"],
            user_id=row["user_id"],
            external_id=row["external_id"],
            input_text=row["input_text"],
            response_text=row["response_text"],
            intent=row["intent"],
            metadata=metadata,
            created_at=row["created_at"],
        )


def _now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def log_interaction(payload: InteractionCreate) -> InteractionOut:
    data = payload.model_dump()
    created_at = data.pop("created_at") or _now_iso()
    metadata = data.pop("metadata")
    metadata_json = (
        json.dumps(metadata, ensure_ascii=False) if metadata is not None else None
    )
    fields = [
        "user_id",
        "external_id",
        "input_text",
        "response_text",
        "intent",
        "metadata",
        "created_at",
    ]
    values = [
        data.get("user_id"),
        data.get("external_id"),
        data["input_text"],
        data["response_text"],
        data.get("intent"),
        metadata_json,
        created_at,
    ]
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            f"""
            INSERT INTO interactions ({", ".join(fields)})
            VALUES ({", ".join(["?"] * len(fields))})
            """,
            values,
        )
        conn.commit()
        new_id = cur.lastrowid
        cur.execute("SELECT * FROM interactions WHERE id = ?", (new_id,))
        row = cur.fetchone()
        return InteractionOut.from_row(row)


def get_recent_interactions(
    *, user_id: Optional[int] = None, external_id: Optional[str] = None, limit: int = 5
) -> list[InteractionOut]:
    if user_id is None and external_id is None:
        return []
    clause = []
    params: list[Any] = []
    if user_id is not None:
        clause.append("user_id = ?")
        params.append(user_id)
    if external_id is not None:
        clause.append("external_id = ?")
        params.append(external_id)
    where = " AND ".join(clause) if clause else "1=1"
    query = (
        "SELECT * FROM interactions "
        f"WHERE {where} "
        "ORDER BY datetime(created_at) DESC, id DESC "
        "LIMIT ?"
    )
    params.append(limit)
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        return [InteractionOut.from_row(row) for row in rows]


def delete_interactions_for_user(
    *, user_id: Optional[int] = None, external_id: Optional[str] = None
) -> int:
    if user_id is None and external_id is None:
        return 0
    clause = []
    params: list[Any] = []
    if user_id is not None:
        clause.append("user_id = ?")
        params.append(user_id)
    if external_id is not None:
        clause.append("external_id = ?")
        params.append(external_id)
    where = " AND ".join(clause)
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(f"DELETE FROM interactions WHERE {where}", params)
        conn.commit()
        return cur.rowcount
