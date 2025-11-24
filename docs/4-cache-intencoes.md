# Cache de Interações e Personalização

Este documento detalha a funcionalidade introduzida no backend do chatbot Curadobia para registrar interações e reutilizar o histórico nas próximas respostas, entregando personalização contextual.

## 1. Objetivo

- **Persistir todas as conversas** com intent, resposta e metadados, permitindo auditoria e aprendizado contínuo.
- **Resgatar o histórico recente** ao receber uma nova mensagem do mesmo usuário (`external_id`) e adaptar a resposta do bot.
- **Facilitar integrações futuras**, como analytics, recomendações baseadas em histórico e retomada de conversas por humanos.

## 2. Componentes Envolvidos

### 2.1 Tabela `interactions` (SQLite)

Arquivo: `app/src/db.py`

```sql
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
```

- Índices em `user_id`, `external_id` e `created_at` agilizam consultas por usuário e ordenação cronológica.

### 2.2 Repositório de Interações

Arquivo: `app/src/interactions_repo.py`

Principais funções:

- `log_interaction(InteractionCreate)` – grava uma linha na tabela, serializando metadados em JSON.
- `get_recent_interactions(user_id | external_id, limit)` – retorna as últimas N interações, já desserializando metadados.
- `delete_interactions_for_user(...)` – utilitário para limpeza.

### 2.3 Endpoint `/chat`

Arquivo: `app/src/app.py`

Fluxo resumido:

1. Se `external_id` for informado, tenta localizar o usuário. Caso não exista, cria um registro básico com `UserCreate`.
2. Recupera as últimas cinco interações (`get_recent_interactions`) via `user_id` ou `external_id`.
3. Constrói `history_payload` com campos importantes (`intent`, `input_text`, `response_text`, `created_at`).
4. Invoca `route_text(text, history=history_payload)`.
5. Após obter a resposta, chama `log_interaction` para salvar input, output, intent e metadados (incluindo dados do RAG e do fallback inteligente).

### 2.4 Personalização no Router

Arquivo: `app/src/router.py`

- `Router.route` agora aceita `history` opcional.
- Método `_build_personalization` produz mensagens como
  - “Que bom continuar te ajudando com ...” quando a intenção atual coincide com a anterior.
  - “Vi que na última conversa falamos sobre ... Você comentou: ...” caso seja uma intenção diferente.
- Personalização é anexada ao início da resposta e registrada em `metadata['personalization']`.

## 3. Exemplo de Resposta Personalizada

1. Usuário pergunta: “Quero saber o status do meu pedido #9988”.
2. Na segunda interação, pergunta: “E sobre o prazo de entrega?”
3. Resposta do bot pode vir como:
   > “Vi que na última conversa falamos sobre rastreamento pedido. Você comentou: O pedido #9988 está atualmente enviado. Claro, vamos revisar o prazo de entrega…”

Metadados retornados incluem:

```json
"personalization": {
  "note": "Vi que na última conversa falamos sobre rastreamento pedido. Você comentou: O pedido #9988 está atualmente enviado.",
  "history_used": 1
}
```

## 4. Testes Automatizados

- `tests/test_interactions.py` usa um banco SQLite temporário para garantir escrita/leitura do histórico com metadados.
- `tests/test_smart_fallback.py::test_personalization_uses_history` verifica que o router injeta a anotação de histórico e contabiliza `history_used`.

## 5. Como Validar Manualmente

1. Criar (ou permitir criação automática) de usuário via `/users/`.
2. Fazer duas chamadas ao `/chat` com o mesmo `external_id`.
3. Observar a resposta personalizada e o metadata retornado.
4. (Opcional) Consultar a tabela interações:

   ```bash
   sqlite3 app/data/chatbot.db "SELECT input_text, response_text, intent, created_at FROM interactions WHERE external_id='cliente-123' ORDER BY created_at DESC;"
   ```

## 6. Próximos Passos Possíveis

- Ajustar o tamanho do histórico considerado conforme a intenção (ex.: mais longo para suporte técnico).
- Resumir histórico longo antes de enviá-lo ao RAG (prompt engineering).
- Integrar com um painel de analytics para acompanhar intents, tempos e falhas.
- Sincronizar interações com CRM ou ferramentas de atendimento.

---
Com esse cache de interações, o chatbot passa a ter “memória” recente, podendo dar continuidade ao contexto e registrar dados valiosos para evolução do modelo e do atendimento humano.
