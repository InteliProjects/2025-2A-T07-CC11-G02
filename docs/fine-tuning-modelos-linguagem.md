# Fine-tuning de Modelos de Linguagem

## Visão Geral

Nesta etapa do projeto, realizamos o **fine-tuning de modelos de linguagem** para adaptá-los ao domínio de **moda**, criando uma assistente capaz de responder perguntas de forma clara, objetiva e elegante.

No início do processo, **testamos diferentes modelos base** para avaliar desempenho, qualidade das respostas e custo computacional. Foram realizados experimentos com **Qwen**, **LLaMA** e **BERT**.

Após testes, **o modelo escolhido para _fine-tuning_ foi o Qwen**, onde vimos grande poder de evolução e melhora das respostas com o _fine-tuning_.

---

## Modelos Avaliados

Abaixo estão os modelos testados e os links para os notebooks de cada experimento:

1. **BERT** – Avaliado como baseline por ser um modelo amplamente utilizado para compreensão de texto.  
   [Notebook de Experimento](https://colab.research.google.com/drive/1oeGOzwmPKK0YvSUYlzbJxToE2WTlgbD8?usp=sharing)

2. **LLaMA** – Testado para geração de respostas mais complexas e contextualizadas, porém com maior demanda de recursos.  
   [Notebook de Experimento](https://colab.research.google.com/drive/1jhSgyd3X6XwMHNW6HvpthMSRYOYgjiel?usp=sharing)

3. **Qwen** – Modelo escolhido.  
   [Notebook de Experimento](https://colab.research.google.com/drive/1YpvXIIPE8M33UPIxuyODhhYGcrOGCM8u?usp=sharing)

---

## Fine-tuning do Modelo Qwen

O notebook final de treinamento encontra-se em:  
`/notebooks/fine_tuning_qwen.ipynb`

Principais características do processo de fine-tuning:

- **Modelo Base:** `Qwen/Qwen2.5-0.5B`
- **Objetivo:** adaptar o modelo para responder perguntas do domínio de moda em português.
- **Formato de entrada:** estrutura de conversação com blocos `<|system|>`, `<|user|>`, `<|assistant|>`.
- **Técnica utilizada:** LoRA (Low-Rank Adaptation) para treinamento eficiente em GPU.
- **Saída final:** modelo mesclado salvo em dois formatos:
  - `.pkl` – para carregamento simples via Python.
  - `.safetensors` – formato seguro e otimizado para produção.
        **Validação**: diversos testes manuais de perguntas para o modelo. Ao final, temos três exemplos de perguntas e respostas que foram feitas ao modelo e suas respectivas respostas. As perguntas foram estrategicamente elaboradas para que o modelo não soubesse responder sem o processo de _fine-tuning._

---

## Resultados e Conclusão

Os experimentos demonstraram uma boa performance do processo de _fine-tuning_, conseguindo gerar respostas precisas e com o tom desejado para a assistente virtual de moda.

---
