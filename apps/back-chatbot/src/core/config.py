CONFIG = {
    "model": {
        "hf_repo_id": "itman-inteli/nsync-sprint2-classificador-intencoes",
        "hf_cache_dir": "~/.cache/huggingface/hub",
    },
    "paths": {
        "best_model_dir": "best_model",
    },
    "id2label": {
        "0": "duvida_produto",
        "1": "solicitacao_informacao",
        "2": "reacao_emocional",
        "3": "interesse_produto",
        "4": "agradecimento",
        "5": "rastreamento_pedido",
        "6": "saudacao",
        "7": "solicitacao_contato",
        "8": "mensagem_sistema",
        "9": "troca_devolucao",
        "10": "problema_tecnico",
        "11": "nao_identificado",
        "12": "reposicao_estoque",
        "13": "confirmacao",
        "14": "parceria_comercial",
        "15": "evento_presencial",
    },
    "embedding": {
        "hf_model_id": "neuralmind/bert-base-portuguese-cased",
        "pooling": "mean",
        "max_length": 128,
    },
    "user": {"name": "Vitto"},
    "rag": {
        "generator": {
            "hf_repo_id": "itman-inteli/nsync-sprint4-qwen-fine-tuned",
            "tokenizer_repo_id": "Qwen/Qwen2.5-0.5B",
            "max_new_tokens": 128,
            "temperature": 0.5,
            "top_p": 0.9,
            "device": None,
        },
        "retriever": {
            "hf_repo_id": "itman-inteli/nsync-sprint4-bert-embeddings-fine-tuned",
            "local_assets_dir": "data/rag",
            "hf_model_id": "intfloat/multilingual-e5-base",
            "pooling": "mean",
            "max_length": 256,
            "documents_file": "documents.jsonl",
            "index_file": "index.faiss",
            "min_score": 0.35,
            "top_k": 3,
            "batch_size": 128,
            "query_prefix": "query: ",
            "passage_prefix": "passage: ",
            "normalize_embeddings": True,
        },
        "prompt": {
            "system": (
                "Você é uma consultora de moda brasileira, com voz feminina, elegante e acolhedora. "
                "Escreva em português impecável, com frases completas, coesas e sem erros gramaticais. "
                "Trate {user_name} com proximidade e profissionalismo, sugerindo combinações e justificando escolhas "
                "quando fizer recomendações. Evite gírias, emojis ou estruturas truncadas. "
                "NUNCA mencione conversas anteriores, saudações ou personalização. Responda APENAS com a informação solicitada."
            ),
            "context_instruction": (
                "Responda APENAS com a informação solicitada, baseada no CONTEXTO fornecido. "
                "NÃO inclua 'Contexto:', 'Usuário:' ou qualquer referência ao prompt. "
                "NÃO cite mensagens anteriores ou saudações. Seja direta e elegante."
            ),
            "context_prefixes": {
                "produto": "PRODUTO",
                "politica": "POLITICA",
                "default": "CONTEUDO",
            },
            "default_user_name": "cliente",
        },
    },
}
