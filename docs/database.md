# Database Guide (SQLite)

This project uses a lightweight SQLite database to store user profiles that help personalize chatbot responses.

- File path: `app/data/chatbot.db`
- Auto-init: created on app startup (`init_db()`), no manual step needed
- Access layer: `app/src/users_repo.py` (Pydantic models + CRUD)
- HTTP API: `app/src/users_api.py` router under `/users`

## Schema

Table: `users`

- id: INTEGER PRIMARY KEY AUTOINCREMENT
- external_id: TEXT UNIQUE (e.g., `whatsapp:5511999999999`, `auth0|...`)
- email: TEXT UNIQUE
- phone: TEXT
- name: TEXT
- preferred_name: TEXT
- pronouns: TEXT
- locale: TEXT DEFAULT `pt-BR`
- timezone: TEXT DEFAULT `America/Sao_Paulo`
- birthdate: TEXT (YYYY-MM-DD)
- marketing_opt_in: INTEGER NOT NULL DEFAULT 0 (CHECK IN (0,1))
- city: TEXT
- state: TEXT
- country: TEXT
- avatar_url: TEXT
- last_intent: TEXT
- last_seen_at: TEXT (ISO datetime)
- preferences: TEXT (JSON string: tone, interests, sizes, colors, budget, etc.)
- notes: TEXT
- created_at: TEXT DEFAULT `datetime('now')`
- updated_at: TEXT DEFAULT `datetime('now')`

Indexes

- `idx_users_external_id` on (`external_id`)
- `idx_users_email` on (`email`)
- `idx_users_last_seen_at` on (`last_seen_at`)

## How It Integrates with Chat

- `POST /chat` accepts `{ text, external_id? }`.
- If `external_id` is provided and found, the app temporarily uses the user’s `preferred_name` (or `name`) to personalize responses (e.g., greetings).

## Running Locally

1) Create and activate a virtualenv (optional)

```bash
python -m venv .venv
source .venv/bin/activate
```

2) Install dependencies

```bash
pip install -r app/src/requirements.txt
```

3) Start the API

```bash
uvicorn app.src.app:app --host 0.0.0.0 --port 8000 --reload
```

The database initializes on the first start and lives at `app/data/chatbot.db`.

## Quick Testing (HTTP)

Create a user

```bash
curl -sS -X POST http://localhost:8000/users \
  -H 'Content-Type: application/json' \
  -d '{
    "external_id": "whatsapp:5511999999999",
    "email": "ana@example.com",
    "name": "Ana",
    "preferred_name": "Aninha",
    "marketing_opt_in": 1,
    "preferences": "{\"sizes\":[\"M\"],\"tone\":\"friendly\"}"
  }' | jq
```

Get by id

```bash
curl -sS http://localhost:8000/users/1 | jq
```

Get by external id

```bash
curl -sS http://localhost:8000/users/by-external/whatsapp:5511999999999 | jq
```

List users

```bash
curl -sS 'http://localhost:8000/users?limit=50&offset=0' | jq
```

Update user (partial)

```bash
curl -sS -X PATCH http://localhost:8000/users/1 \
  -H 'Content-Type: application/json' \
  -d '{ "city": "São Paulo", "country": "BR" }' | jq
```

Delete user

```bash
curl -sS -X DELETE http://localhost:8000/users/1 | jq
```

Personalized chat using the user

```bash
curl -sS -X POST http://localhost:8000/chat \
  -H 'Content-Type: application/json' \
  -d '{ "text": "oi", "external_id": "whatsapp:5511999999999" }' | jq
```

## Quick Testing (Python API)

```python
from app.src.users_repo import UserCreate, create_user, get_user_by_external_id
from app.src.db import init_db

init_db()
user = create_user(UserCreate(external_id="local:demo", name="Maria", preferred_name="Mah"))
print(user)
print(get_user_by_external_id("local:demo"))
```

## Resetting the Database

- Stop the app.
- Delete the file `app/data/chatbot.db`.
- Start the app again; it recreates the schema automatically.

```bash
rm -f app/data/chatbot.db
```

## Migrations & Evolving the Schema

- For simple changes, you can add `ALTER TABLE` statements in `init_db()` guarded by checks.
- For larger changes or multiple environments, consider a migration tool (e.g., Alembic) or maintain manual migration scripts executed at startup.

## Notes

- SQLite is file-based; avoid concurrent writes from many processes. For higher throughput, consider a server DB (PostgreSQL) and swap the connection layer.
- `preferences` is a JSON string for flexibility; if you want structure and validation, promote it to dedicated columns or parse/validate JSON in Pydantic models.
