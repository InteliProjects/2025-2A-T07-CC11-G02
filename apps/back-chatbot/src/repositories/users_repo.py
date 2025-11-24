from __future__ import annotations

import sqlite3
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .db import get_connection


class UserCreate(BaseModel):
    external_id: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    name: Optional[str] = None
    preferred_name: Optional[str] = None
    pronouns: Optional[str] = None
    locale: Optional[str] = "pt-BR"
    timezone: Optional[str] = "America/Sao_Paulo"
    birthdate: Optional[str] = None  # YYYY-MM-DD
    marketing_opt_in: int = Field(default=0, ge=0, le=1)
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    avatar_url: Optional[str] = None
    last_intent: Optional[str] = None
    last_seen_at: Optional[str] = None  # ISO datetime
    preferences: Optional[str] = None  # JSON string
    notes: Optional[str] = None


class UserUpdate(BaseModel):
    external_id: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    name: Optional[str] = None
    preferred_name: Optional[str] = None
    pronouns: Optional[str] = None
    locale: Optional[str] = None
    timezone: Optional[str] = None
    birthdate: Optional[str] = None
    marketing_opt_in: Optional[int] = Field(default=None, ge=0, le=1)
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    avatar_url: Optional[str] = None
    last_intent: Optional[str] = None
    last_seen_at: Optional[str] = None
    preferences: Optional[str] = None
    notes: Optional[str] = None


class UserOut(BaseModel):
    id: int
    external_id: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    name: Optional[str] = None
    preferred_name: Optional[str] = None
    pronouns: Optional[str] = None
    locale: Optional[str] = None
    timezone: Optional[str] = None
    birthdate: Optional[str] = None
    marketing_opt_in: int
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    avatar_url: Optional[str] = None
    last_intent: Optional[str] = None
    last_seen_at: Optional[str] = None
    preferences: Optional[str] = None
    notes: Optional[str] = None
    created_at: str
    updated_at: str

    @classmethod
    def from_row(cls, row: sqlite3.Row) -> "UserOut":
        return cls(**{k: row[k] for k in row.keys()})


def _now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"


def create_user(data: UserCreate) -> UserOut:
    fields = [
        "external_id",
        "email",
        "phone",
        "name",
        "preferred_name",
        "pronouns",
        "locale",
        "timezone",
        "birthdate",
        "marketing_opt_in",
        "city",
        "state",
        "country",
        "avatar_url",
        "last_intent",
        "last_seen_at",
        "preferences",
        "notes",
    ]
    values = [getattr(data, f) for f in fields]
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            f"""
            INSERT INTO users ({", ".join(fields)})
            VALUES ({", ".join(["?"] * len(fields))})
            """,
            values,
        )
        conn.commit()
        uid = cur.lastrowid
        return get_user_by_id(uid)  # type: ignore[return-value]


def get_user_by_id(user_id: int) -> Optional[UserOut]:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        row = cur.fetchone()
        return UserOut.from_row(row) if row else None


def get_user_by_external_id(external_id: str) -> Optional[UserOut]:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE external_id = ?", (external_id,))
        row = cur.fetchone()
        return UserOut.from_row(row) if row else None


def list_users(limit: int = 50, offset: int = 0) -> list[UserOut]:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM users ORDER BY id DESC LIMIT ? OFFSET ?",
            (limit, offset),
        )
        rows = cur.fetchall()
        return [UserOut.from_row(r) for r in rows]


def update_user(user_id: int, data: UserUpdate) -> Optional[UserOut]:
    updates = {k: v for k, v in data.model_dump(exclude_unset=True).items()}
    if not updates:
        return get_user_by_id(user_id)

    updates["updated_at"] = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    cols = ", ".join([f"{k} = ?" for k in updates.keys()])
    vals = list(updates.values())
    vals.append(user_id)
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(f"UPDATE users SET {cols} WHERE id = ?", vals)
        conn.commit()
    return get_user_by_id(user_id)


def delete_user(user_id: int) -> bool:
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        return cur.rowcount > 0
