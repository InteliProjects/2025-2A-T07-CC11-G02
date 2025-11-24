# Detecção de Ambiguidades - Sprint 4

## Visão Geral

Este artefato implementa um sistema de detecção de ambiguidades que identifica perguntas vagas ou imprecisas dos usuários e solicita esclarecimentos automaticamente. O mecanismo utiliza o próprio modelo de linguagem do sistema RAG para analisar se uma pergunta é específica o suficiente para gerar uma resposta útil.

## Implementação

### 1. Modificações no RAG Service (`rag_service.py`)

#### Prompt Engineering para Detecção de Ambiguidades

O sistema foi implementado através de instruções específicas no prompt do modelo:

```python
def _format_prompt(self, question: str, docs: Sequence[Dict[str, Any]], user_name: Optional[str]) -> str:
    # ... código existente ...
    
    # Adicionar instruções para detecção de ambiguidades
    ambiguity_instruction = (
        "IMPORTANTE: Se a pergunta for vaga, imprecisa ou muito genérica (como 'me ajude', 'preciso de algo', "
        "'quero comprar', 'tem alguma coisa?', 'me recomende'), você deve responder EXATAMENTE assim: "
        "'PERGUNTA_AMBIGUA: Para te ajudar melhor, preciso de mais detalhes. Que tipo de produto você está procurando? "
        "Tem alguma ocasião específica em mente? Qual seu estilo preferido?' "
        "Caso contrário, responda normalmente com base no contexto."
    )
```

#### Exemplos de Perguntas Ambíguas Detectadas

- "me ajude"
- "preciso de algo"
- "quero comprar"
- "tem alguma coisa?"
- "me recomende"
- "o que vocês têm?"
- "quero ver produtos"

### 2. Processamento no Router (`router.py`)

O router foi modificado para processar respostas que contêm o marcador `PERGUNTA_AMBIGUA:`:

```python
# Verifica se a resposta indica uma pergunta ambígua
if answer and answer.startswith("PERGUNTA_AMBIGUA:"):
    # Remove o prefixo e usa como resposta de esclarecimento
    clarification_response = answer.replace("PERGUNTA_AMBIGUA:", "").strip()
    response_text = clarification_response
    rag_used = True
    # Adiciona metadados específicos para ambiguidade
    metadata["ambiguity_detection"] = {
        "detected": True,
        "original_question": question,
        "clarification_requested": True
    }
```

### 3. Metadados de Resposta

Quando uma ambiguidade é detectada, o sistema adiciona metadados específicos à resposta:

```json
{
  "ambiguity_detection": {
    "detected": true,
    "original_question": "me ajude",
    "clarification_requested": true
  }
}
```

## Como Funciona

1. **Entrada do Usuário**: O usuário envia uma pergunta vaga como "me ajude"
2. **Processamento RAG**: O sistema RAG recebe a pergunta junto com as instruções de detecção
3. **Análise**: O modelo de linguagem analisa se a pergunta é específica o suficiente
4. **Detecção**: Se identificada como ambígua, o modelo retorna uma resposta com o prefixo `PERGUNTA_AMBIGUA:`
5. **Processamento**: O router detecta o prefixo e processa como uma solicitação de esclarecimento
6. **Resposta**: O sistema retorna perguntas específicas para ajudar o usuário a ser mais claro

## Exemplo de Funcionamento

### Entrada Ambígua

```
Usuário: "me ajude"
```

### Resposta do Sistema

```
"Para te ajudar melhor, preciso de mais detalhes. Que tipo de produto você está procurando? Tem alguma ocasião específica em mente? Qual seu estilo preferido?"
```

### Metadados Retornados

```json
{
  "response": "Para te ajudar melhor, preciso de mais detalhes...",
  "intent": "duvida_produto",
  "metadata": {
    "ambiguity_detection": {
      "detected": true,
      "original_question": "me ajude",
      "clarification_requested": true
    },
    "rag": {
      "used": true,
      "question": "me ajude"
    }
  }
}
```

## Vantagens da Implementação

1. **Simplicidade**: Usa o próprio modelo existente sem necessidade de componentes adicionais
2. **Flexibilidade**: Pode ser facilmente ajustado modificando as instruções no prompt
3. **Integração**: Se integra naturalmente com o fluxo RAG existente
4. **Transparência**: Os metadados permitem rastrear quando ambiguidades são detectadas
5. **Manutenibilidade**: Fácil de modificar e expandir os critérios de detecção

## Limitações

1. **Dependência do Modelo**: A qualidade da detecção depende da capacidade do modelo de seguir instruções
2. **Falsos Positivos/Negativos**: Pode ocasionalmente classificar incorretamente perguntas específicas como ambíguas ou vice-versa
3. **Idioma**: Otimizado para português brasileiro, pode precisar ajustes para outros idiomas

## Futuras Melhorias

1. **Classificador Dedicado**: Implementar um modelo específico para detecção de ambiguidades
2. **Aprendizado**: Sistema de feedback para melhorar a detecção ao longo do tempo
3. **Contexto Histórico**: Considerar conversas anteriores para melhor detecção
4. **Personalização**: Adaptar critérios de ambiguidade baseado no perfil do usuário

## Testes Sugeridos

Para validar a implementação, teste com as seguintes entradas:

### Perguntas Ambíguas (devem solicitar esclarecimentos)

- "me ajude"
- "quero comprar algo"
- "tem alguma coisa legal?"
- "me recomende"
- "preciso de ajuda"

### Perguntas Específicas (devem responder normalmente)

- "preciso de um vestido para festa de casamento"
- "qual o preço da blusa azul?"
- "vocês têm calças jeans tamanho M?"
- "quero algo para o trabalho, estilo social"

## Arquivo de Código Relacionados

- `/app/src/rag_service.py`: Implementação das instruções de detecção no prompt
- `/app/src/router.py`: Processamento das respostas com detecção de ambiguidade
- `/app/src/intent.py`: Classes de intenção que utilizam o sistema RAG
