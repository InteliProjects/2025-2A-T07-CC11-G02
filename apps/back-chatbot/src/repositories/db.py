import os
import sqlite3

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
DB_PATH = os.path.join(DATA_DIR, "chatbot.db")


def _ensure_dirs() -> None:
    os.makedirs(DATA_DIR, exist_ok=True)


def get_connection() -> sqlite3.Connection:
    """Open a SQLite connection with row factory returning dict-like rows."""
    _ensure_dirs()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    """Create tables and indexes if they don't exist."""
    _ensure_dirs()
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                external_id TEXT UNIQUE,
                email TEXT UNIQUE,
                phone TEXT,
                name TEXT,
                preferred_name TEXT,
                pronouns TEXT,
                locale TEXT DEFAULT 'pt-BR',
                timezone TEXT DEFAULT 'America/Sao_Paulo',
                birthdate TEXT,
                marketing_opt_in INTEGER NOT NULL DEFAULT 0 CHECK (marketing_opt_in IN (0,1)),
                city TEXT,
                state TEXT,
                country TEXT,
                avatar_url TEXT,
                last_intent TEXT,
                last_seen_at TEXT,
                preferences TEXT, -- JSON string (tone, interests, sizes, colors, budget...)
                notes TEXT,
                created_at TEXT NOT NULL DEFAULT (datetime('now')),
                updated_at TEXT NOT NULL DEFAULT (datetime('now'))
            );
            """
        )
        cur.execute(
            "CREATE INDEX IF NOT EXISTS idx_users_external_id ON users(external_id);"
        )
        cur.execute("CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);")
        cur.execute(
            "CREATE INDEX IF NOT EXISTS idx_users_last_seen_at ON users(last_seen_at);"
        )
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS interactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                external_id TEXT,
                input_text TEXT NOT NULL,
                response_text TEXT NOT NULL,
                intent TEXT,
                metadata TEXT,
                created_at TEXT NOT NULL DEFAULT (datetime('now')),
                FOREIGN KEY(user_id) REFERENCES users(id)
            );
            """
        )
        cur.execute(
            "CREATE INDEX IF NOT EXISTS idx_interactions_user_id ON interactions(user_id);"
        )
        cur.execute(
            "CREATE INDEX IF NOT EXISTS idx_interactions_external_id ON interactions(external_id);"
        )
        cur.execute(
            "CREATE INDEX IF NOT EXISTS idx_interactions_created_at ON interactions(created_at);"
        )
        conn.commit()
