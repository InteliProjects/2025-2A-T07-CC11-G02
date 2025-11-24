<div align="justify">

# Chatbot Consultivo para E-commerce de Moda: Aplicação de PLN e IA Generativa em Sistema de Recomendação Personalizada

Ana Luisa Goes Barbosa, Gabriel Coletto Silva, Gabriel Farias, Hugo Noyma, João Paulo Santos, Lucas Nogueira Nunes, Mauro das Chagas Junior, Vitto Mazeto

# Abstract

&emsp;O _e-commerce_ de moda exige atendimento consultivo em escala, preservando o tom humano da curadoria. Apresentamos um sistema híbrido de _chatbot_ consultivo para o _e-commerce_ Curadobia que integra (i) classificação de intenções com _embeddings_ BERT e SVM e (ii) geração de linguagem especializada via _fine-tuning_ leve (LoRA) de um modelo de linguagem de grande porte (LLM), acoplado a RAG para recuperar catálogo e políticas. O corpus real inclui 1.439 mensagens rotuladas em 16 intenções, 1.000 pares pergunta–resposta para ajuste do LLM e 1.504 documentos indexados para recuperação. Em teste, o SVM superou o Random Forest (acurácia 70,8%; F1-macro 0,681; ganho de 11,5 pontos percentuais em acurácia balanceada), enquanto o LLM ajustado produziu respostas mais específicas e com menor alucinação. A arquitetura adota limiares de confiança e _fallback_ humano para casos ambíguos, demonstrando viabilidade prática de MVP sob dados desbalanceados. Discutimos limitações (classes minoritárias, gírias/sarcasmo) e próximos passos: expansão/deduplicação do corpus, análise de sentimentos por aspecto e métricas híbridas (AHT, CSAT, conversão) para mensurar impacto de negócio.

# 1. Introdução

&emsp;O _e-commerce_ de moda tem experimentado transformações aceleradas, especialmente após a pandemia de COVID-19, que forçou a migração de serviços tradicionalmente presenciais para o ambiente digital. Neste cenário, empresas enfrentam o complexo desafio de equilibrar personalização e escalabilidade no atendimento ao cliente, precisando automatizar o suporte sem comprometer a qualidade consultiva. O segmento de moda apresenta particularidades únicas, pois as decisões de compra envolvem aspectos subjetivos como estilo pessoal, ocasião de uso e preferências estéticas que demandam orientação especializada. _chatbots_ baseados em Processamento de Linguagem Natural (PLN) e técnicas de Inteligência Artificial Generativa emergem como solução promissora para conciliar eficiência operacional com experiência personalizada, oferecendo potencial para revolucionar o atendimento no _e-commerce_ de moda (LANDIM et al., 2024) [[1]](#ref-1).

&emsp;O Curadobia, _marketplace_ focado em curadoria especializada de moda, exemplifica perfeitamente essa necessidade emergente do mercado. A empresa, que se posiciona como consultoria de moda integrada ao varejo digital, busca escalar seu atendimento consultivo sem perder o diferencial competitivo fundamental: oferecer orientação personalizada sobre combinações, modelagem, caimento e estilo de vida. Com mais de 20 marcas parceiras e um ano de operação, o Curadobia enfrenta a limitação de manter seu DNA de "peças com história" e experiência de compra guiada conforme cresce. O desafio central é automatizar processos de atendimento mantendo o tom próximo, empático e humanizado que caracteriza a consultoria de moda tradicional, sem recorrer a respostas genéricas ou robóticas que comprometeriam a proposta de valor da marca.

&emsp;Este trabalho propõe o desenvolvimento de um sistema de _chatbot_ inteligente capaz de responder dúvidas frequentes e oferecer recomendações de produtos de forma consultiva e personalizada. O objetivo é criar uma solução baseada em PLN e IA generativa que preserve a identidade conversacional e o expertise em curadoria da marca, enquanto permite escalabilidade operacional através de algoritmos de recomendação contextualizados. A implementação busca integrar _machine learning_ com o conhecimento especializado em moda, possibilitando interações naturais que mantenham o padrão de qualidade do atendimento humano. Espera-se que a solução contribua tanto para a otimização de recursos da empresa quanto para o avanço do conhecimento em sistemas conversacionais aplicados ao varejo especializado.

# 2. Trabalhos Relacionados

&emsp;A revisão de literatura foi conduzida entre julho e agosto de 2025, utilizando como base o Google Scholar. As consultas foram realizadas com combinações de termos em inglês e português, tais como: _“fashion e-commerce chatbot recommendation system”_, _“sentiment analysis personalized recommendation”_, _“generative AI conversational agent retail”_ e _“chatbot consultivo moda”_, entre outras variações. Foi priorizado artigos publicados entre 2024 e 2025, de modo a refletir o estado da arte sobre PLN e IA generativa aplicados ao atendimento digital em varejo.

&emsp;Esta seção revisa a literatura recente sobre o uso de Processamento de Linguagem Natural (PLN) e Análise de Sentimentos em _e-commerce_, com foco em experiências de atendimento via _chatbot_ e recomendações personalizadas. Três frentes emergem de forma consistente: (i) fatores humanos que moldam a experiência do cliente com tecnologias de PLN em atendimento, (ii) incorporação de sentimentos de textos (avaliações, comentários) em sistemas de recomendação, e (iii) evidências quantitativas de impacto em lealdade, vendas e retorno financeiro, bem como desafios de privacidade, justiça e reprodutibilidade.

## 2.1. Análise dos trabalhos

&emsp;O primeiro trabalho analisado neste artigo demonstra uma investigação conduzida por Hui [[2]](#ref-2) e realizada por meio de hipóteses testadas empiricamente, com o objetivo de definir quais fatores determinam a experiência e a satisfação do cliente ao interagir com tecnologias de PLN no contexto de _e-commerce_. Os resultados apontam que a facilidade de uso percebida, a influência social e a aprendizagem por observação têm efeitos positivos e significativos sobre a experiência do cliente; a utilidade percebida e a autoeficácia, por outro lado, não se mostraram determinantes. Além disso, a experiência do cliente exerce impacto significativo sobre a satisfação. Pontos positivos incluem a robustez psicométrica dos instrumentos (altas confiabilidades) e implicações gerenciais claras (priorizar usabilidade e alavancar prova social). Entre as limitações, destacam-se a ênfase em construtos perceptuais (com pouca medição comportamental objetiva, como tempo de resolução ou taxa de desvio para o humano), a ausência de métricas operacionais de suporte (ex.: Tempo Médio de Atendimento ou AHT, Satisfação do Cliente ou CSAT, Resolução no Primeiro Contato ou FCR) e a generalização para domínios específicos (moda) ainda aberta.

&emsp;Atuando em uma frente com foco distinto, Gajula [[3]](#ref-3) apresenta em sua pesquisa uma revisão abrangente sobre recomendações sensíveis a sentimentos, destacando a transição de abordagens manuais e modelos rasos para arquiteturas profundas e, mais recentemente, modelos baseados em transformadores e representações gráficas (grafos de conhecimento que conectam usuários, itens e aspectos/opiniões). O trabalho ressalta tendências de 2023–2025: reprodutibilidade (conjuntos de ferramentas, sementes aleatórias ou _seeds_, rastreamento de experimentos), métricas além de acurácia (diversidade, novidade, qualidade/explicabilidade de recomendações), e o papel de Modelos de Linguagem de Grande Porte (LLMs) tanto na compreensão de texto quanto na geração de explicações. Também sistematiza desafios persistentes: ruído e ambiguidade (ironia/sarcasmo), alinhamento de sentimentos por aspecto, preferência dinâmica/temporal, início a frio (_cold start_), escalabilidade e justiça algorítmica (_fairness_)/privacidade. Como pontos fortes, a revisão orienta boas práticas experimentais e transparência; como limitações, há pouca evidência de estudos com testes A/B em produção e menor foco no fluxo de suporte conversacional (embora os achados sejam diretamente úteis para motores de recomendação em _marketplaces_ de moda).

&emsp;Por fim, Ismail, Ghareeb e Youssry [[4]](#ref-4) conduzem uma análise empírica relacionando _scores_ de sentimento, uso de recursos de PLN e personalização com lealdade do cliente, crescimento de vendas e Retorno sobre o Investimento (ROI). Os autores reportam correlação forte entre sentimento e lealdade (um fator de aproximadamente 78%), efeito positivo dos recursos de PLN na lealdade, ganho de vendas associado a recomendações personalizadas (+5,28% por incremento de personalização) e ROI aproximado de 400% em cenário exemplificativo. O estudo também indica alto nível de satisfação dos usuários com privacidade (85%) e alerta para variações culturais/linguísticas que afetam a acurácia de análises de sentimento. Entre os pontos positivos, destacam-se a quantificação de impacto de negócio e a discussão ética; como limitações, permanecem questões de generalização (tamanho/amostra, controles de confusão) e suposições de ROI, além de necessidade de maior detalhamento metodológico para plena reprodutibilidade.

## 2.2. Síntese e lacunas

&emsp;Em conjunto, os trabalhos convergem para diretrizes úteis ao desenvolvimento de um _chatbot_ de suporte para um _marketplace_ de roupas. Em suma:

- A experiência do usuário depende criticamente de usabilidade e sinais sociais (ex.: avaliações/indicadores de confiança) [[2]](#ref-2);
- Incorporar sentimentos de textos dos clientes melhora a personalização (produtos, respostas e explicações), mas exige tratar aspectos por atributo (tamanho, tecido, caimento), linguagem coloquial de moda e dinâmica temporal (tendências/estações) [[3]](#ref-3);
- Há evidências de ganhos em lealdade, vendas e ROI quando sentimentos e PLN são aplicados com personalização, desde que se considerem privacidade e diferenças culturais [[4]](#ref-4).

&emsp;Entretanto, persistem lacunas em: (i) detecção de sarcasmo e gírias da moda, (ii) métricas padronizadas que conectem ganhos _offline_ (Raiz do Erro Quadrático Médio e Taxa de Acerto) a impacto real (deflexão de chamados, CSAT, conversão), (iii) pipelines reprodutíveis ponta a ponta (dados, _prompts_, _seeds_), e (iv) _fairness_ (evitar vieses em linguagem/avaliações). Essas limitações se traduzem em importantes pontos de atenção para o desenvolvimento desta pesquisa, que devem ter seus respectivos níveis de impacto sobre o projeto avaliados para que sejam concebidas tratativas eficazes.

## 2.3. Comparação entre trabalhos

&emsp;A seguir, apresenta-se uma tabela de _benchmark_ (Tabela 01) entre os diferentes trabalhos analisados e discutidos nas seções anteriores deste documento, a fim de comparar seus objetivos, resultados e impacto ou relação ao projeto em desenvolvimento.

<div align="center">
<sub>Tabela 01 – Comparação entre os trabalhos relacionados</sub>

| Trabalho                                                       | Escopo/Tipo                                                             | Metodologia/Dados                                                                            | Principais resultados                                                                                                                                   | Métricas/Relatos                                                                   | Pontos positivos                                                              | Limitações                                                                                     |
| -------------------------------------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [[2]](#ref-2) Hui – The Role of NLP…                           | Modelo de aceitação e experiência em atendimento com PLN (quantitativo) | Hipóteses H1–H6; testes de confiabilidade e significância                                    | Facilidade de uso, influência social e aprendizagem por observação → experiência; experiência → satisfação; utilidade e autoeficácia não significativas | Alfas de confiabilidade elevados; efeitos significativos reportados                | Implicações gerenciais claras (priorizar usabilidade e prova social)          | Pouca métrica operacional (AHT, FCR); foco perceptual; generalização para domínios específicos |
| [[3]](#ref-3) Gajula – Sentiment-aware Recommendation Systems… | Revisão (2023–2025) de recomendação com sentimentos                     | Síntese de estado da arte: transformadores, grafos, LLMs; boas práticas de reprodutibilidade | Integração de sentimentos melhora precisão/explicabilidade; desafios: sarcasmo, aspectos, tempo, _cold start_, escalabilidade, _fairness_/privacidade   | Ênfase em padrões de _benchmarks_, _seeds_, protocolos e métricas além de acurácia | Direciona práticas transparentes e comparáveis; visão ampla do estado da arte | Falta de evidências de testes A/B em produção; foco menor em suporte conversacional            |
| [[4]](#ref-4) Ismail et al. – Enhancing Customer Experience…   | Estudo empírico de impacto de PLN/sentimentos                           | Descritivo + regressão; variáveis de lealdade, vendas, satisfação, privacidade               | r≈0,78 (sentimento↔lealdade); +5,28% vendas por incremento de personalização; ROI≈400%; 85% satisfeitos com privacidade                                 | Estatísticas descritivas; t-values/p-values reportados                             | Quantifica impacto de negócio e aborda ética/privacidade                      | Generalização e suposições de ROI; necessidade de mais detalhes metodológicos                  |

<sup>Fonte: Material produzido pelos próprios autores (2025)</sup>

</div>

## 2.4. Implicações para o projeto

&emsp;Haja vista a análise supracitada, é possível determinar importantes ações e diretrizes que podem ser aplicadas a este projeto. Dentre elas, destacam-se:

- Priorizar a Experiência do Usuário (UX) do _chatbot_ (clareza, tempo de resposta, linguagem da marca);
- Alavancar evidência social (avaliações/fotos de clientes) no diálogo;
- Usar análise de sentimentos para personalizar recomendações e explicações por aspecto (ex.: caimento, tecido, tamanho);
- Adotar práticas robustas de reprodutibilidade (versionamento de dados, _seeds_, rastreamento de experimentos, contêineres);
- Monitorar métricas de produto e suporte (deflexão, Satisfação do Cliente (CSAT), Tempo Médio de Atendimento (AHT), taxa de conversão e repetição de compra);
- Tratar privacidade/consentimento e vieses linguísticos/culturais do domínio de moda;
- Considerar implicações do uso de IA generativa, como controle de alucinações, calibragem de respostas consultivas e alinhamento com a identidade da marca, garantindo transparência e confiabilidade no atendimento.

# 3. Materiais e Métodos

### 3.1. Aquisição e tratamento dos dados

&emsp;Os dados foram obtidos a partir de um arquivo CSV consolidado contendo mensagens de atendimento do Curadobia oriundas de WhatsApp e Instagram. o arquivo encontrava-se estruturado com as seguintes colunas: `Usuário`, `Data/Hora`, `Remetente`, `Mensagem` e `Tipo de Conteúdo` (texto, link, áudio, imagem ou vídeo). Como processos iniciais do tratamento de dados, a coluna `Mensagem` foi renomeada para `original`, foram removidos valores nulos e os registros foram reindexados. Os campos auxiliares como identificador da interação, data/hora, canal de origem e categoria inicial foram mantidos para apoiar etapas posteriores de análise e rastreabilidade. A taxonomia de _intents_ que orienta o escopo do _chatbot_ está presente no código de taxonomia e foi utilizada como referência para delimitar as categorias conversacionais.

&emsp;Essas decisões asseguram padronização do campo-alvo ao longo do _pipeline_, evitam a propagação de registros vazios, preservam a rastreabilidade entre etapas e delimitam o escopo de _intents_ que guiará a curadoria do corpus.

## 3.2. Análise exploratória de dados (AED)

&emsp;A AED foi conduzida nos notebooks de exploração e de pré-processamento com o objetivo de caracterizar o corpus e apoiar decisões de pré-processamento e modelagem, sem apresentação de resultados nesta seção. As atividades metodológicas incluíram: (i) cálculo do comprimento das mensagens em tokens, com estatísticas descritivas e histogramas, para orientar limites de truncamento e memória de diálogo; (ii) inspeção do vocabulário após normalização (remoção de _stopwords_ e _stemming_) para identificar termos característicos do domínio e apoiar a definição de _intents_/_slots_; (iii) mapeamento das categorias temáticas para verificar cobertura e orientar estratégias de balanceamento; e (iv) organização dos artefatos da AED (tabelas e gráficos) diretamente a partir dos notebooks, garantindo reprodutibilidade e rastreabilidade.

## 3.3. Pré-processamento textual

&emsp;Foi implementado um _pipeline_ leve e reprodutível no _notebook_ de pré-processamento, composto pelas etapas:

- **lower**: conversão para minúsculas — normaliza a capitalização e reduz a sparsidade lexical;
- **strip_accents**: normalização Unicode e remoção de acentos — unifica variantes ortográficas (p.ex., "ação"/"acao");
- **remove_punctuation**: remoção de pontuação e símbolos — reduz ruído não lexical em representações baseadas em termos;
- **tokenize**: tokenização simples por espaço — viabiliza filtragem e transformações subsequentes por termo;
- **remove_stopwords**: remoção de stopwords em português — atenua termos de alta frequência com baixo poder discriminativo;
- **stem**: redução lexical com RSLPStemmer — agrupa flexões e variações morfológicas, favorecendo a generalização inicial.

&emsp;O _pipeline_ é composto por funções puras e orquestrado por uma rotina de execução que produz um conjunto de colunas por etapa (de `original` até `stems`), mantendo rastreabilidade das transformações. A figura a seguir (Figura 01) ilustra o fluxo aplicado:

<div align="center">

<sub>Figura 01: Fluxo Pipeline de Pré-processamento</sub>

![Fluxo do pipeline de pré-processamento](imagens/figura-pipeline-pre-processamento.png)

<sup>Fonte: Material produzido pelos próprios autores por meio do Mermaid (2025).</sup>

</div>

&emsp;Em síntese, as etapas de aquisição, AED e pré-processamento constituem um _pipeline_ padronizado, rastreável e reprodutível para sustentar as fases de modelagem e avaliação.

## 3.4. Resultados do processamento com o pipeline de pré-processamento

&emsp;Para evidenciar os efeitos do _pipeline_ sobre o corpus, foram gerados gráficos a partir do _notebook_ de pré-processamento. As imagens abaixo (Figuras 02 e 03) representam o impacto das transformações, acompanhadas de descrições textuais.

&emsp;Tabela síntese por etapa: estatísticas descritivas do comprimento das mensagens (p.ex., média, mediana e desvio-padrão) ao longo das etapas (`original` → `stems`), ilustrando a redução e normalização progressivas que simplificam a vetorização inicial.

<div align="center">

<sub>Figura 02: Estatísticas de comprimento por etapa do pipeline</sub>

![Tabela síntese por etapa do pipeline](imagens/tabela-comprimento-por-etapa.png)

<sup>Fonte: Produzido pelos autores a partir do notebook de pré-processamento (2025).</sup>

</div>

&emsp;Observa-se redução gradual do comprimento das mensagens entre as etapas, com menor variabilidade após a normalização e a remoção de _stopwords_. Esse comportamento é desejável, pois simplifica a vetorização inicial e orienta a definição de limites de janelamento para diálogos.

&emsp;Vocabulário característico do domínio: gráfico de barras dos Top-20 termos/stems após remoção de _stopwords_ e _stemming_, útil para mapear _intents_, _slots_ e preservar o tom consultivo.

<div align="center">

<sub>Figura 03: Top-20 termos/stems após pré-processamento</sub>

![Top-20 stems após pré-processamento](imagens/top20-stems.png)

<sup>Fonte: Produzido pelos autores a partir do notebook de pré-processamento (2025).</sup>

</div>

&emsp;O conjunto de termos/stems mais frequentes evidencia o vocabulário característico do domínio de moda e atendimento. Esses termos subsidiam a definição de _intents_ e _slots_ e ajudam a calibrar dicionários/ontologias, mantendo o tom consultivo da marca.

&emsp;Os resultados do processamento demonstram que o _pipeline_ adotado reduz ruído superficial, normaliza o texto e preserva sinais semânticos relevantes. Esses artefatos orientam escolhas práticas do projeto (limites de _tokens_, políticas de memória de diálogo, curadoria de _intents_ e _features_ iniciais), além de garantirem reprodutibilidade por meio do _notebook_ de processamento.

## 3.5. Classificador de intenções

&emsp;O sistema de classificação de intenções foi implementado a partir da combinação de _embeddings_ gerados por BERT em português e um classificador baseado em _scikit-learn_. O modelo é disponibilizado em repositório no Hugging Face, o que permite reuso e controle de versões. Para garantir consistência, o serviço valida a dimensionalidade do vetor de entrada em relação ao classificador, assegurando a compatibilidade entre etapas de treinamento e inferência.

&emsp;Na etapa final, foram testados dois classificadores: Support Vector Machine (SVM) e Random Forest. Ambos foram avaliados sobre o mesmo conjunto de dados, permitindo comparação direta de desempenho.

## 3.6. Taxonomia de intenções

&emsp;A taxonomia definida para o chatbot contempla 16 intenções distintas: _dúvida_produto_, _solicitação_informação_, _reação_emocional_, _interesse_produto_, _agradecimento_, _rastreamento_pedido_, _saudação_, _solicitação_contato_, _mensagem_sistema_, _troca_devolução_, _problema_técnico_, _não_identificado_, _reposição_estoque_, _confirmação_, _parceria_comercial_ e _evento_presencial_.

&emsp;O mapeamento _id2label_ é explicitado no arquivo de configuração, garantindo alinhamento entre fases de treino e inferência.

**Quadro 1 – Taxonomia de intenções do chatbot**

| Identificador | Intenção                 | Descrição breve                                                                 |
| ------------- | ------------------------ | ------------------------------------------------------------------------------- |
| 1             | _dúvida_produto_         | Perguntas sobre especificações, tamanhos, variantes ou quantidades de produtos. |
| 2             | _solicitação_informação_ | Requisição de informações gerais, políticas ou detalhes adicionais.             |
| 3             | _reação_emocional_       | Mensagens curtas de reação ou emoção (ex.: emojis, expressões afetivas).        |
| 4             | _interesse_produto_      | Demonstração de interesse em produtos específicos, tamanhos ou variantes.       |
| 5             | _agradecimento_          | Expressões de gratidão pelo atendimento.                                        |
| 6             | _rastreamento_pedido_    | Solicitações de status ou código de rastreio de pedidos.                        |
| 7             | _saudação_               | Início de conversa com cumprimentos.                                            |
| 8             | _solicitação_contato_    | Pedido para ser contatado via WhatsApp, e-mail ou telefone.                     |
| 9             | _mensagem_sistema_       | Mensagens automáticas ou de sistema.                                            |
| 10            | _troca_devolução_        | Solicitações para troca ou devolução de pedidos.                                |
| 11            | _problema_técnico_       | Relato de falhas técnicas ou bugs, possivelmente com capturas de tela.          |
| 12            | _não_identificado_       | Mensagens ambíguas ou não classificadas.                                        |
| 13            | _reposição_estoque_      | Perguntas sobre disponibilidade futura de itens ou variantes.                   |
| 14            | _confirmação_            | Respostas confirmando ações ou informações fornecidas.                          |
| 15            | _parceria_comercial_     | Propostas de colaboração ou contato com o time comercial.                       |
| 16            | _evento_presencial_      | Interações sobre participação em eventos presenciais.                           |

## 3.7. Geração de _embeddings_

&emsp;Os textos são convertidos em vetores densos utilizando o modelo _neuralmind/bert-base-portuguese-cased_, com truncamento em até _128 tokens_ e agregação via _mean pooling_. Não foi realizado _fine-tuning_, sendo utilizado o modelo pré-treinado disponível publicamente.

&emsp;Durante o desenvolvimento, a extração de _embeddings_ e o treinamento dos classificadores foram realizados na GPU T4 disponibilizada pelo ambiente Google Colab, usando aceleração por hardware para reduzir o tempo de processamento.

## 3.8. Roteamento e fluxos conversacionais

&emsp;As predições de intenção passam por um processo de normalização (conversão para minúsculas, remoção de acentos e substituição de espaços por sublinhados) antes de serem mapeadas para os respectivos _handlers_.

&emsp;O diálogo é conduzido por fluxos orientados a estados, nos quais cada intenção pode acionar transições específicas. Por exemplo, uma _dúvida_produto_ pode levar à consulta do catálogo e, em seguida, a um estado de encerramento ou recomendação; já um pedido de _rastreamento_pedido_ pode levar à consulta de status e envio do código de rastreio.

&emsp;O fluxo inclui também um estado de transição condicional (_encerrar_ou_recomendar_), que atua como ponto central para concluir ou expandir a interação.

## 3.9. API de inferência

&emsp;A camada de acesso é publicada como um serviço baseado em FastAPI[[5]](#ref-5), com endpoints bem definidos. O serviço disponibiliza:

- O endpoint `GET /healthz`, para monitoramento.
- O endpoint `POST /chat`, responsável pela classificação da mensagem e pelo roteamento conversacional.

**Quadro 2 – Exemplo ilustrativo de requisição e resposta do endpoint `/chat`**

Request:

```json
{ "text": "Quais tamanhos tem da BLUSA MOLONA?" }
```

Response:

```json
{ "response": "A BLUSA MOLONA está disponível nos tamanhos: P, M, G." }
```

## 3.10. Respostas e ações

&emsp;Cada intenção é associada a um _handler_ responsável por gerar respostas modelo. O mecanismo utiliza mensagens pré-definidas e informações simuladas. Por exemplo, para um item de vestuário, pode-se indicar disponibilidade em estoque e variações de tamanho; no caso de rastreamento de pedidos, informar um status fictício.

&emsp;Esse recurso permite avaliar a experiência de diálogo sem depender de integrações externas. Em etapas posteriores, os _handlers_ poderão ser estendidos para acionar consultas reais em sistemas de catálogo, logística ou pós-venda.

### 3.10.1. Respostas simuladas com variabilidade

&emsp;Como a solução ainda não está integrada a sistemas reais, algumas intenções utilizam geração randômica de respostas (por exemplo, produtos, tamanhos, cores, preços ou status de pedidos). Esse recurso, implementado com funções como _random.choice_ e _random.randint_, introduz variabilidade controlada durante os testes, evitando respostas idênticas e possibilitando avaliar melhor a robustez dos fluxos conversacionais.

## 3.11. _Fine-tuning_ de Modelos de Linguagem

&emsp;Para gerar respostas humanizadas específicas do domínio de moda, foi implementado o _fine-tuning_ de modelos de linguagem. Após avaliação de diferentes arquiteturas (BERT, LLaMA e Qwen), foi selecionado o modelo _Qwen/Qwen2.5-0.5B_ como base para especialização.

&emsp;A escolha do Qwen baseou-se em múltiplos critérios de avaliação. Em relação à performance base, o modelo demonstrou superior capacidade de compreensão e geração em português brasileiro quando comparado às alternativas, apresentando respostas mais coerentes e contextualmente apropriadas mesmo sem especialização. Quanto à praticidade para _fine-tuning_, o Qwen ofereceu maior facilidade de implementação com a técnica LoRA, compatibilidade nativa com formatos de conversa estruturados e menor demanda computacional durante o treinamento. Adicionalmente, o modelo apresentou melhor relação custo-benefício para o contexto de desenvolvimento em GPU T4, arquitetura otimizada para processamento eficiente de sequências conversacionais, e documentação técnica abrangente que facilitou a implementação e ajustes de hiperparâmetros.

&emsp;O processo utilizou a técnica LoRA (_Low-Rank Adaptation_) para treinamento eficiente, aplicada especificamente às camadas de projeção de atenção: `q_proj`, `k_proj`, `v_proj` e `o_proj`. Esta abordagem permite adaptar o modelo mantendo a maior parte dos parâmetros congelados, reduzindo significativamente o custo computacional.

&emsp;O conjunto de dados de treinamento foi construído a partir de 1.000 pares pergunta-resposta em português brasileiro, estruturados no formato de conversa com blocos delimitadores: `<|system|>` (instruções de comportamento e contexto), `<|user|>` (pergunta do usuário) e `<|assistant|>` (resposta esperada do modelo). Esta estruturação permite ao modelo aprender distinções claras entre diferentes tipos de conteúdo durante o diálogo. O conteúdo foi gerado através de um processo híbrido:

1. **Transcrição automatizada**: conversão de vídeos sobre moda em texto utilizando modelos de _speech-to-text_
2. **Estruturação via LLM**: processamento supervisionado para gerar pares pergunta-resposta baseados nas transcrições

&emsp;Os hiperparâmetros utilizados foram: taxa de aprendizado de $2e^{-4}$, _batch size_ de 2 por dispositivo com acumulação de gradientes (fator 4), treinamento por 1 época, e configuração LoRA com r=8, α=16 e _dropout_ de 0.05. O treinamento foi realizado em ambiente Google Colab utilizando GPU T4.

&emsp;O modelo resultante foi salvo em dois formatos: `.pkl` para carregamento simples via Python e `.safetensors` para uso em produção. A validação qualitativa demonstrou melhoria significativa na geração de respostas específicas do domínio quando comparado ao modelo base.

## 3.12. Sistema de Respostas Contextuais com RAG

&emsp;Foi implementado um sistema de _Retrieval-Augmented Generation_ (RAG) para fornecer respostas contextuais baseadas em catálogo de produtos e políticas da empresa. O sistema combina recuperação semântica com geração especializada para oferecer sugestões personalizadas.

### 3.12.1. Construção do corpus e indexação

&emsp;O corpus foi construído com 1.504 documentos, sendo 1.500 produtos simulados e 4 documentos de políticas empresariais. O catálogo de produtos inclui informações detalhadas: nome, descrição, categoria, preço, estoque por tamanho, medidas corporais por tamanho, materiais e cores.

&emsp;Para indexação semântica, foram utilizados _embeddings_ gerados pelo modelo `intfloat/multilingual-e5-base`, especializado em português brasileiro. Os textos foram processados com prefixo `passage:` para documentos e `query:` para consultas, seguindo as recomendações do modelo E5.

&emsp;O índice vetorial foi implementado utilizando FAISS (_Facebook AI Similarity Search_) com produto interno normalizado, permitindo busca eficiente por similaridade de cosseno. A normalização dos vetores garante que as pontuações sejam comparáveis e interpretáveis.

### 3.12.2. Pipeline de recuperação e geração

&emsp;O _pipeline_ RAG segue as etapas:

1. **Codificação da consulta**: conversão da pergunta do usuário em vetor normalizado
2. **Recuperação top-k**: busca dos k documentos mais similares no índice FAISS (padrão k=5)
3. **Construção do contexto**: concatenação dos documentos recuperados com prefixos identificadores
4. **Geração da resposta**: utilização do modelo Qwen _fine-tunado_ com _prompt_ estruturado

&emsp;O _template_ de _prompt_ inclui instruções explícitas para: (i) responder apenas com base no contexto fornecido, (ii) não revelar identificadores internos como SKUs, (iii) manter o tom consultivo e elegante característico da marca, e (iv) indicar quando não há informação suficiente.

### 3.12.3. Parâmetros de geração

&emsp;A geração utiliza os seguintes parâmetros: máximo de 256 _tokens_ novos, amostragem habilitada (_do_sample=True_), temperatura de 0.5 para balancear criatividade e consistência, e _top_p_ de 0.9 para _nucleus sampling_. Esses valores foram ajustados empiricamente para manter respostas concisas e relevantes.

## 3.13. Análise Semântica Avançada

&emsp;Para identificação de padrões semânticos e agrupamentos temáticos, foi implementada uma análise avançada baseada em _clustering_ de _embeddings_. O objetivo é compreender a estrutura semântica do corpus de perguntas e identificar variações linguísticas que expressam intenções similares.

### 3.13.1. Extração e processamento de _embeddings_

&emsp;Foram extraídos _embeddings_ semânticos de 1.000 perguntas utilizando o modelo _fine-tunado_ Qwen, resultando em representações vetoriais de 896 dimensões. A estratégia de extração utilizou o último estado oculto (_last_hidden_state_) das camadas de atenção, capturando representações contextualizadas específicas do domínio.

&emsp;Para visualização e análise exploratória, foram aplicadas três técnicas de redução de dimensionalidade:

- **PCA** (_Principal Component Analysis_): redução linear preservando máxima variância
- **t-SNE** (_t-Distributed Stochastic Neighbor Embedding_): visualização não-linear em 2D
- **UMAP** (_Uniform Manifold Approximation and Projection_): preservação de estrutura local e global

### 3.13.2. _Clustering_ semântico otimizado

&emsp;O número ótimo de _clusters_ foi determinado através de otimização baseada em duas métricas complementares:

- **Silhouette Score**: mede qualidade da separação entre _clusters_
- **Calinski-Harabasz Score**: avalia razão entre dispersão inter e intra-_cluster_

&emsp;O algoritmo K-Means identificou 10 _clusters_ semânticos ótimos, apresentando Silhouette Score de 1.000 (separação perfeita) e Calinski-Harabasz Score de aproximadamente $1.97\times10^{14}$, indicando excelente separação entre grupos.

### 3.13.3. Análise de variações linguísticas

&emsp;O sistema identificou 50.173 variações linguísticas distribuídas entre os _clusters_, com taxa média de variação de 5.017%. Esta análise permite detectar diferentes formulações para expressar a mesma intenção, fundamental para robustez de sistemas de processamento de linguagem natural.

&emsp;A distribuição das perguntas entre os _clusters_ mostrou-se relativamente equilibrada (8.5% a 12.1% por _cluster_), indicando ausência de viés significativo para temas específicos no conjunto de dados analisado.

# 4. RESULTADOS

&emsp;Esta seção apresenta os resultados obtidos no desenvolvimento do chatbot consultivo para e-commerce de moda, organizados em dois eixos principais: (i) classificação de intenções em cenário multiclasse e (ii) geração de respostas com modelo de linguagem especializado. Os resultados são fundamentados em dados quantitativos extraídos de 1.439 mensagens rotuladas e 1.000 pares pergunta-resposta.

## 4.1. Corpus e infraestrutura experimental

&emsp;O conjunto de dados para classificação de intenções totaliza 1.439 mensagens distribuídas em 16 categorias. A distribuição das classes evidencia desbalanceamento acentuado, conforme detalhado na Tabela 02.

<div align="center">
<sub>Tabela 02: Distribuição de mensagens por categoria de intenção</sub>

| Categoria | Quantidade | Percentual | Observação |
|-----------|-----------|-----------|------------|
| nao_identificado | 333 | 23,1% | Maior categoria |
| duvida_produto | 187 | 13,0% | |
| solicitacao_informacao | 156 | 10,8% | |
| interesse_produto | 143 | 9,9% | |
| agradecimento | 128 | 8,9% | |
| reacao_emocional | 115 | 8,0% | |
| saudacao | 97 | 6,7% | |
| rastreamento_pedido | 85 | 5,9% | |
| solicitacao_contato | 72 | 5,0% | |
| troca_devolucao | 54 | 3,8% | |
| confirmacao | 41 | 2,8% | |
| problema_tecnico | 38 | 2,6% | |
| reposicao_estoque | 32 | 2,2% | |
| mensagem_sistema | 28 | 1,9% | |
| parceria_comercial | 24 | 1,7% | |
| evento_presencial | 19 | 1,3% | Menor categoria |
| **Total** | **1.439** | **100%** | |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&emsp;A categoria _nao_identificado_ concentra 333 exemplos (23,1% do total), enquanto _evento_presencial_ possui apenas 19 exemplos (1,3%), caracterizando desbalanceamento de classe com razão de 17,5:1 entre a maior e menor categoria. As três maiores categorias (_nao_identificado_, _duvida_produto_, _solicitacao_informacao_) representam 46,9% do corpus total (676 mensagens).

&emsp;Para geração de respostas, o corpus compreende 1.000 pares pergunta-resposta em português brasileiro, particionados em 900 exemplos para treinamento (90%) e 100 para teste (10%). Os embeddings foram extraídos com o modelo `neuralmind/bert-base-portuguese-cased`, gerando vetores de 768 dimensões com truncamento em 128 tokens e agregação via mean pooling. O ambiente experimental utilizou GPU T4 no Google Colab, com tempo médio de processamento de 100ms por mensagem durante inferência.

## 4.2. Desempenho global dos classificadores de intenção

&emsp;Foram avaliados dois algoritmos de classificação: Random Forest e Support Vector Machine (SVM), ambos treinados sobre os mesmos embeddings BERT. A Tabela 03 apresenta as métricas de desempenho no conjunto de teste.

<div align="center">
<sub>Tabela 03 – Desempenho global dos modelos de classificação de intenções</sub>

| Métrica | Random Forest | SVM | Diferença Absoluta | Interpretação |
|---------|--------------|-----|-------------------|---------------|
| **Acurácia Geral** | 67,4% | 70,8% | +3,4 pp | Moderada |
| **Acurácia Balanceada** | 58,3% | 69,8% | +11,5 pp | Substancial |
| **Coeficiente Kappa** | 0,636 | 0,680 | +0,044 | Concordância substancial |
| **F1-Score Macro** | 0,579 | 0,681 | +0,102 | Melhoria significativa |
| **F1-Score Weighted** | 0,662 | 0,709 | +0,047 | Melhoria moderada |
| **Validação Cruzada (5-fold)** | 66,7% ± 1,9% | 67,0% ± 2,0% | +0,3 pp | Consistência entre modelos |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&emsp;O SVM demonstrou desempenho superior em todas as métricas avaliadas. O ganho mais expressivo ocorreu na acurácia balanceada, com incremento de 11,5 pontos percentuais (58,3% → 69,8%), indicando maior capacidade do SVM para lidar com classes minoritárias. O coeficiente Kappa de 0,680 para o SVM caracteriza concordância substancial segundo a escala de Landis e Koch. A validação cruzada com 5 folds apresentou resultados consistentes para ambos os modelos, com desvios-padrão similares (~2%), sugerindo estabilidade das estimativas.

## 4.3. Desempenho por categoria de intenção

&emsp;A Tabela 04 detalha as métricas de desempenho por categoria, ordenadas por F1-Score do modelo SVM, incluindo métricas complementares de precisão e revocação.

<div align="center">
<sub>Tabela 04 – Desempenho detalhado por categoria: comparação Random Forest vs SVM</sub>

| Categoria | Exemplos | RF Precisão | RF Revocação | RF F1 | SVM Precisão | SVM Revocação | SVM F1 | Ganho F1 | Classificação |
|-----------|----------|------------|-------------|-------|--------------|--------------|--------|----------|---------------|
| saudacao | 97 | 0,88 | 0,92 | 0,90 | 0,96 | 1,00 | 0,98 | +0,08 | Excelente |
| agradecimento | 128 | 0,81 | 0,86 | 0,83 | 0,85 | 0,91 | 0,88 | +0,05 | Excelente |
| reacao_emocional | 115 | 0,82 | 0,86 | 0,84 | 0,81 | 0,88 | 0,84 | 0,00 | Boa |
| solicitacao_informacao | 156 | 0,69 | 0,74 | 0,71 | 0,76 | 0,81 | 0,78 | +0,07 | Adequada |
| confirmacao | 41 | 0,62 | 0,68 | 0,65 | 0,70 | 0,74 | 0,72 | +0,07 | Adequada |
| nao_identificado | 333 | 0,68 | 0,73 | 0,70 | 0,69 | 0,74 | 0,71 | +0,01 | Adequada |
| troca_devolucao | 54 | 0,55 | 0,61 | 0,58 | 0,65 | 0,72 | 0,68 | +0,10 | Adequada |
| rastreamento_pedido | 85 | 0,30 | 0,36 | 0,33 | 0,60 | 0,66 | 0,63 | +0,30 | Crítica |
| mensagem_sistema | 28 | 0,49 | 0,56 | 0,52 | 0,58 | 0,64 | 0,61 | +0,09 | Crítica |
| solicitacao_contato | 72 | 0,45 | 0,52 | 0,48 | 0,53 | 0,59 | 0,56 | +0,08 | Crítica |
| reposicao_estoque | 32 | 0,39 | 0,46 | 0,42 | 0,48 | 0,55 | 0,51 | +0,09 | Crítica |
| duvida_produto | 187 | 0,35 | 0,42 | 0,38 | 0,44 | 0,51 | 0,47 | +0,09 | Crítica |
| parceria_comercial | 24 | 0,32 | 0,39 | 0,35 | 0,42 | 0,49 | 0,45 | +0,10 | Crítica |
| problema_tecnico | 38 | 0,26 | 0,33 | 0,29 | 0,38 | 0,45 | 0,41 | +0,12 | Crítica |
| interesse_produto | 143 | 0,00 | 0,00 | 0,00 | 0,26 | 0,33 | 0,29 | +0,29 | Crítica |
| evento_presencial | 19 | 0,00 | 0,00 | 0,00 | 0,26 | 0,33 | 0,29 | +0,29 | Crítica |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&emsp;Os resultados revelam três grupos distintos de desempenho:

- **Grupo Excelente/Boa** (F1 > 0,80): Três categorias (_saudacao_, _agradecimento_, _reacao_emocional_) totalizando 340 mensagens (23,6% do corpus). Estas categorias apresentam F1-Scores entre 0,84 e 0,98, com o SVM alcançando revocação perfeita (1,00) em _saudacao_.

- **Grupo Adequada** (0,60 < F1 ≤ 0,80): Quatro categorias (_solicitacao_informacao_, _confirmacao_, _nao_identificado_, _troca_devolucao_) totalizando 584 mensagens (40,6% do corpus). Demonstram desempenho moderado, com F1-Scores variando entre 0,68 e 0,78.

- **Grupo Crítica** (F1 ≤ 0,60): Nove categorias totalizando 515 mensagens (35,8% do corpus). Apresentam desempenho insatisfatório para automação completa, com F1-Scores entre 0,29 e 0,63. Destaca-se que _interesse_produto_ e _evento_presencial_ obtiveram F1 zero no Random Forest, melhorando para 0,29 no SVM.

&emsp;O SVM apresentou ganhos superiores a 0,20 em F1-Score nas categorias _rastreamento_pedido_ (+0,30), _interesse_produto_ (+0,29) e _evento_presencial_ (+0,29), demonstrando capacidade superior de aprendizado em classes minoritárias. Contudo, mesmo com estes ganhos, seis categorias permanecem com F1 < 0,50, indicando limitações fundamentais relacionadas ao volume de dados e ambiguidade semântica.

## 4.4. Análise de confiança das predições

&emsp;A confiança das predições, medida pela probabilidade máxima atribuída à classe prevista, apresentou distribuições contrastantes entre os modelos. A Tabela 05 sumariza as estatísticas de confiança.

<div align="center">
<sub>Tabela 05 – Estatísticas de confiança das predições</sub>

| Métrica de Confiança | Random Forest | SVM | Diferença |
|---------------------|--------------|-----|-----------|
| **Média** | 0,275 | 0,857 | +0,582 |
| **Mediana** | 0,250 | 0,910 | +0,660 |
| **Desvio-Padrão** | 0,142 | 0,168 | +0,026 |
| **Percentil 25** | 0,160 | 0,780 | +0,620 |
| **Percentil 75** | 0,380 | 0,965 | +0,585 |
| **Predições > 80%** | 8,3% | 68,2% | +59,9 pp |
| **Predições < 40%** | 82,1% | 12,4% | -69,7 pp |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&emsp;O Random Forest apresentou distribuição de confiança dispersa e baixa, com média de apenas 27,5% e mediana de 25,0%. Apenas 8,3% das predições ultrapassaram 80% de confiança, enquanto 82,1% permaneceram abaixo de 40%, indicando alta incerteza generalizada do modelo. Em contraste, o SVM demonstrou padrão de confiança elevado e concentrado, com média de 85,7% e mediana de 91,0%. Aproximadamente 68,2% das predições do SVM superaram o limiar de 80% de confiança, com apenas 12,4% abaixo de 40%.

&emsp;Exemplos ilustrativos de mensagens específicas demonstram esta diferença quantitativamente:

<div align="center">
<sub>Tabela 06 – Exemplos de confiança por mensagem</sub>

| Mensagem | Categoria Real | RF Confiança | SVM Confiança | Diferença |
|----------|---------------|--------------|---------------|-----------|
| "Onde está meu pedido?" | rastreamento_pedido | 14,5% | 91,2% | +76,7 pp |
| "Tem esse produto no tamanho P?" | duvida_produto | 29,0% | 87,6% | +58,6 pp |
| "Bom dia! Tudo bem?" | saudacao | 35,2% | 98,4% | +63,2 pp |
| "Muito obrigada pela ajuda!" | agradecimento | 31,8% | 95,1% | +63,3 pp |
| "Quando chega meu pacote?" | rastreamento_pedido | 18,4% | 88,9% | +70,5 pp |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&emsp;As diferenças de confiança variaram entre 58,6 e 76,7 pontos percentuais nos exemplos analisados, com ganho médio de 66,5 pontos percentuais favorecendo o SVM. Esta característica habilita implementação prática de limiares de confiança para roteamento híbrido (automação alta confiança + fallback humano baixa confiança).

## 4.5. Padrões de erro e confusões entre categorias

&emsp;A análise da matriz de confusão do modelo SVM revelou padrões sistemáticos de erro concentrados em pares de categorias semanticamente próximas. A Tabela 07 apresenta as dez confusões mais frequentes.

<div align="center">
<sub>Tabela 07 – Top-10 confusões entre categorias (modelo SVM)</sub>

| Ranking | Categoria Real | Predição Incorreta | Casos | % Total Erros | Sobreposição Semântica |
|---------|----------------|-------------------|-------|---------------|----------------------|
| 1 | duvida_produto | problema_tecnico | 28 | 15,1% | "não funciona", "está errado" |
| 2 | interesse_produto | duvida_produto | 26 | 14,0% | "tem?", "disponível?" |
| 3 | duvida_produto | solicitacao_informacao | 22 | 11,9% | "informações sobre", "detalhes" |
| 4 | problema_tecnico | duvida_produto | 18 | 9,7% | "como funciona", "não entendi" |
| 5 | mensagem_sistema | troca_devolucao | 15 | 8,1% | Confirmações automáticas |
| 6 | solicitacao_contato | solicitacao_informacao | 13 | 7,0% | "quero falar", "preciso de ajuda" |
| 7 | reposicao_estoque | duvida_produto | 12 | 6,5% | "quando volta", "tem novamente?" |
| 8 | parceria_comercial | solicitacao_contato | 11 | 5,9% | "contato comercial", "proposta" |
| 9 | rastreamento_pedido | solicitacao_informacao | 10 | 5,4% | "informação do pedido" |
| 10 | confirmacao | reacao_emocional | 9 | 4,9% | "ok", "perfeito", emoticons |
| | | **Subtotal Top-10** | **164** | **88,5%** | |
| | | **Total de Erros** | **185** | **100%** | |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&emsp;As três confusões mais frequentes (_duvida_produto_ ↔ _problema_tecnico_, _interesse_produto_ ↔ _duvida_produto_, _duvida_produto_ ↔ _solicitacao_informacao_) representam 41,0% dos erros totais (76 de 185 casos). A categoria _duvida_produto_ aparece em seis das dez principais confusões (rankings 1-4, 7, 9), funcionando como "categoria atratora" devido ao seu volume (187 exemplos, 13,0% do corpus) e vocabulário genérico relacionado a características de produtos.

&emsp;Análise qualitativa dos erros revela sobreposição lexical significativa: 73% das confusões _duvida_produto_/_problema_tecnico_ continham termos ambíguos como "não funciona", "está errado" ou "não aparece", que podem expressar tanto dúvida sobre características quanto defeito técnico. Similarmente, 81% das confusões _interesse_produto_/_duvida_produto_ incluíam formulações interrogativas curtas ("Tem?", "Disponível no P?") sem contexto suficiente para desambiguação.

## 4.6. Estrutura semântica do corpus de geração

&emsp;Para o corpus de 1.000 pares pergunta-resposta, foram extraídos embeddings de 896 dimensões utilizando o modelo Qwen fine-tunado. Análise de clustering via K-Means identificou k=10 como número ótimo de agrupamentos através de métricas complementares.

<div align="center">
<sub>Tabela 08 – Métricas de otimização do clustering</sub>

| Número de Clusters | Silhouette Score | Calinski-Harabasz Score | Interpretação |
|-------------------|-----------------|------------------------|---------------|
| 5 | 0,892 | 8,45×10¹³ | Subclustering |
| 7 | 0,946 | 1,21×10¹⁴ | Próximo ao ótimo |
| **10** | **1,000** | **1,97×10¹⁴** | **Ótimo** |
| 12 | 0,998 | 1,89×10¹⁴ | Overfitting |
| 15 | 0,995 | 1,72×10¹⁴ | Overfitting |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&emsp;O Silhouette Score de 1,000 para k=10 indica separação perfeita entre grupos, enquanto o Calinski-Harabasz Score de 1,97×10¹⁴ confirma máxima razão entre dispersão inter e intra-cluster. A Tabela 09 detalha a distribuição temática dos clusters identificados.

<div align="center">
<sub>Tabela 09 – Distribuição temática e volumétrica dos clusters semânticos</sub>

| Cluster | Tópico Principal | Subtópicos | Exemplos | % | Similaridade Intra-Cluster |
|---------|------------------|-----------|----------|---|---------------------------|
| 0 | Proporções e pantalona | Altura, comprimento, caimento | 113 | 11,3% | 0,983 |
| 1 | Tênis em looks elegantes | Combinações, ocasiões formais | 115 | 11,5% | 0,991 |
| 2 | Versatilidade bolsa bucket | Cores, tamanhos, estilos | 98 | 9,8% | 0,987 |
| 3 | Marcas regatas básicas | Qualidade, tecidos, durabilidade | 100 | 10,0% | 0,989 |
| 4 | Botas looks inverno | Materiais, altura, modelagens | 89 | 8,9% | 0,985 |
| 5 | Minissaia com elegância | Comprimentos, combinações | 121 | 12,1% | 0,994 |
| 6 | Ajuste bolsa tiracolo | Altura, conforto, posicionamento | 85 | 8,5% | 0,981 |
| 7 | Cores bolsa roupas escuras | Alternativas preto, contrastes | 92 | 9,2% | 0,988 |
| 8 | Acessórios elevam elegância | Joias, lenços, cintos | 91 | 9,1% | 0,986 |
| 9 | Escolher regata qualidade | Critérios, acabamento, costuras | 96 | 9,6% | 0,990 |
| | **Total** | | **1.000** | **100%** | **0,987 (média)** |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&emsp;A distribuição apresenta equilíbrio relativo entre clusters, variando de 8,5% (_Ajuste bolsa tiracolo_) a 12,1% (_Minissaia com elegância_), com amplitude de apenas 3,6 pontos percentuais. A similaridade intra-cluster média de 0,987 indica alta coesão temática dentro de cada agrupamento. Análise de variações linguísticas identificou 50.173 pares de paráfrases distribuídos entre os clusters, resultando em taxa média de variação de 5.017% (equivalente a aproximadamente 50 paráfrases por pergunta base).

<div align="center">
<sub>Tabela 10 – Estatísticas de variação linguística por cluster</sub>

| Cluster | Perguntas Base (Est.) | Variações Totais | Taxa Variação | Exemplo Variações |
|---------|----------------------|-----------------|---------------|-------------------|
| 0 | 20 | 5.650 | 28.250% | "pantalona baixas", "calça wide-leg altura", "modelagem pantalona pequenas" |
| 1 | 23 | 5.750 | 25.000% | "tênis elegantes", "sneakers formais", "calçado esportivo chique" |
| 2 | 19 | 4.900 | 25.789% | "bolsa bucket versátil", "bucket bag combina", "saco bucket estilos" |
| 3 | 20 | 5.000 | 25.000% | "marcas regata", "camiseta básica marca", "brand regata qualidade" |
| 4 | 18 | 4.450 | 24.722% | "botas inverno", "bota frio", "calçado coturno estação fria" |
| 5 | 24 | 6.050 | 25.208% | "minissaia elegante", "saia curta chique", "mini elegância" |
| 6 | 17 | 4.250 | 25.000% | "ajustar tiracolo", "altura bolsa transversal", "regular crossbody" |
| 7 | 18 | 4.600 | 25.556% | "cor bolsa roupas escuras", "tonalidade preto alternativa", "shade bag dark clothes" |
| 8 | 18 | 4.550 | 25.278% | "acessórios elegância", "bijoux sofisticação", "adornos requinte" |
| 9 | 19 | 4.973 | 26.174% | "escolher regata", "selecionar camiseta", "pick basic tee" |
| **Total** | **~200** | **50.173** | **~5.017%** | |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&emsp;A taxa média de variação de 5.017% indica redundância significativa no corpus: cada pergunta conceitual possui, em média, 50 variações linguísticas. Esta característica facilita o aprendizado de padrões de paráfrase durante o fine-tuning, mas potencialmente reduz a pressão de generalização para perguntas verdadeiramente novas fora da distribuição de treinamento.

## 4.7. Comparação qualitativa: modelo base vs. modelo especializado

&emsp;A avaliação qualitativa comparou respostas geradas pelo modelo Qwen2.5-0.5B base (pré-treinado) e pela versão fine-tunada com LoRA sobre 100 perguntas de teste. A Tabela 11 apresenta métricas agregadas de qualidade.

<div align="center">
<sub>Tabela 11 – Métricas agregadas de qualidade: base vs. fine-tuned</sub>

| Aspecto Avaliado | Qwen Base | Qwen Fine-tuned | Diferença | Critério de Avaliação |
|------------------|-----------|-----------------|-----------|---------------------|
| **Especificidade Domínio** | 1,8/5,0 | 4,5/5,0 | +2,7 (+150%) | Menção entidades específicas (marcas, modelos) |
| **Frequência Alucinações** | 3,4/5,0 | 0,9/5,0 | -2,5 (-72%) | Loops, contradições, informações inexistentes |
| **Coerência Interna** | 2,1/5,0 | 4,8/5,0 | +2,7 (+129%) | Consistência lógica, ausência contradições |
| **Aderência Tom Consultivo** | 2,3/5,0 | 4,7/5,0 | +2,4 (+104%) | Linguagem próxima, empática, especializada |
| **Utilidade Prática** | 1,9/5,0 | 4,6/5,0 | +2,7 (+142%) | Orientações acionáveis vs. generalidades |
| **Comprimento Resposta (tokens)** | 142 ± 68 | 58 ± 21 | -84 (-59%) | Concisão (menor variabilidade) |
| **Taxa Repetição** | 18,3% | 2,1% | -16,2 pp (-89%) | Frases/palavras repetidas |

<sup>Fonte: Avaliação qualitativa pelos autores em escala ordinal 1-5 (2025)</sup>
</div>

&emsp;O modelo fine-tunado demonstrou ganhos substanciais em todos os aspectos avaliados. A especificidade de domínio aumentou 150%, caracterizada pela capacidade de mencionar marcas reais (Rye T-shirt, Tatá Martello, My Basic, Farm) em vez de generalidades. A frequência de alucinações reduziu 72%, eliminando loops de repetição e contradições lógicas. O comprimento médio das respostas reduziu 59% (142 → 58 tokens), indicando maior concisão e objetividade.

&emsp;A Tabela 12 apresenta três casos representativos com respostas completas para ilustração qualitativa detalhada.

<div align="center">
<sub>Tabela 12 – Casos ilustrativos: comparação qualitativa de respostas</sub>

| Aspecto | Detalhamento |
|---------|--------------|
| **CASO 1: Pergunta sobre marcas de regatas básicas** | |
| Pergunta | "Quais marcas oferecem boas regatas básicas?" |
| Categoria | Recomendação de produto |
| **Qwen Base** | "Regatas básicas são peças fundamentais no guarda-roupa feminino. Para escolher boas regatas básicas, é importante considerar a qualidade do tecido. Regatas básicas de qualidade apresentam caimento adequado. Marcas brasileiras oferecem regatas básicas de qualidade. Regatas básicas de qualidade apresentam durabilidade. Para escolher boas regatas básicas é importante considerar a qualidade do tecido. Marcas brasileiras..." [continua repetindo por 187 tokens sem mencionar marcas específicas] |
| Tokens | 187 |
| Repetições | 15 ocorrências de "regatas básicas" |
| Alucinações | Loop de repetição sem informação útil |
| **Qwen Fine-tuned** | "Recomendo as marcas Rye T-shirt, Tatá Martello e My Basic pela qualidade do algodão egípcio e durabilidade excepcional. A Farm também oferece opções interessantes com estampas discretas que mantêm a versatilidade da peça básica." |
| Tokens | 52 |
| Repetições | 0 |
| Alucinações | 0 |
| **Ganhos** | +100% especificidade (4 marcas nomeadas), -72% tokens, eliminação completa de loops |
| **CASO 2: Pergunta sobre combinações de tênis** | |
| Pergunta | "Como combinar tênis em looks elegantes?" |
| Categoria | Consultoria de estilo |
| **Qwen Base** | "Tênis podem ser usados em diversos looks. Para looks elegantes, é importante escolher o tênis adequado. A combinação de tênis em looks elegantes depende do estilo pessoal. Tênis podem ser combinados com diferentes peças. Para looks elegantes é importante escolher o tênis adequado." [reafirma a pergunta sem oferecer orientações] |
| Tokens | 98 |
| Utilidade | 1,2/5,0 (reafirma problema sem solução) |
| **Qwen Fine-tuned** | "Priorize modelos de design limpo em couro branco ou nude, evitando elementos muito esportivos. Combine com pantalonas de alfaiataria, saias midi fluidas ou vestidos de corte reto. Prefira solados finos e evite calçados de corrida para manter a elegância do conjunto." |
| Tokens | 61 |
| Utilidade | 4,8/5,0 (3 orientações acionáveis específicas) |
| **Ganhos** | +275% utilidade prática, especificação de cores/materiais/modelagens |

| **CASO 3: Pergunta sobre cores de bolsa** | |
| Pergunta | "Que cor de bolsa combina com roupas escuras além do preto?" |
| Categoria | Consultoria de cores |
| **Qwen Base** | "Para roupas escuras, o preto é uma escolha clássica e versátil. Além do preto, outras cores também podem funcionar bem com roupas escuras. O preto oferece contraste interessante e é uma cor que combina facilmente." [contradição: responde "preto" como alternativa ao preto] |
| Tokens | 87 |
| Coerência | 1,5/5,0 (contradição lógica) |
| **Qwen Fine-tuned** | "O azul-marinho oferece contraste sutil e elegante sem o óbvio do preto total. Outras opções refinadas incluem burgundy para ocasiões noturnas e cinza-carvão para versatilidade diurna, mantendo a sofisticação." |
| Tokens | 49 |
| Coerência | 5,0/5,0 (resposta logicamente consistente) |
| **Ganhos** | Eliminação de contradição, +3 alternativas cromáticas específicas, redução 44% tokens |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&emsp;Os três casos demonstram padrões consistentes de melhoria: (i) eliminação de loops de repetição e alucinações, (ii) inclusão de entidades específicas do domínio (marcas, cores específicas, tipos de tecido), (iii) orientações acionáveis em vez de reafirmações genéricas, e (iv) coerência lógica sem contradições. O modelo fine-tunado manteve consistentemente respostas entre 49-61 tokens (média 54 ± 6), comparado a 87-187 tokens (média 124 ± 50) do modelo base, demonstrando maior controle sobre a geração.

## 4.8. Desempenho do sistema RAG com catálogo

&emsp;O sistema de Retrieval-Augmented Generation foi implementado com 1.504 documentos indexados via FAISS, compreendendo 1.500 produtos simulados do catálogo e 4 documentos de políticas empresariais. A Tabela 13 apresenta métricas de desempenho do sistema.

<div align="center">
<sub>Tabela 13 – Métricas de desempenho do sistema RAG</sub>

| Métrica | Valor | Benchmark Desejável | Status |
|---------|-------|-------------------|--------|
| **Tempo médio de recuperação** | 23ms | < 50ms | ✓ Adequado |
| **Tempo médio de geração** | 340ms | < 450ms | ✓ Adequado |
| **Latência total** | 363ms | < 500ms | ✓ Adequado |
| **Taxa de contexto relevante** | 87,3% | > 80% | ✓ Adequado |
| **Cobertura do catálogo** | 94,2% | > 90% | ✓ Adequado |
| **Produtos não-recuperáveis** | 5,8% (87 itens) | < 10% | ✓ Adequado |
| **Top-k documentos recuperados** | 5 | 3-7 (configurável) | 5 padrão |
| **Taxa de acerto Top-1** | 73,4% | > 70% | ✓ Adequado |
| **Taxa de acerto Top-5** | 94,1% | > 90% | ✓ Adequado |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&emsp;O sistema apresentou latência total média de 363ms (23ms recuperação + 340ms geração) por consulta, enquadrando-se nos limites aceitáveis para experiência conversacional (< 500ms). A taxa de contexto relevante de 87,3% indica que, em média, 4,37 dos 5 documentos recuperados eram pertinentes à consulta do usuário. A cobertura de catálogo de 94,2% demonstra que 1.415 dos 1.500 produtos são adequadamente recuperáveis via busca semântica, com 85 produtos (5,8%) apresentando descrições insuficientemente ricas para recuperação efetiva.

&emsp;A análise de acerto por posição revela que 73,4% das consultas obtiveram o documento mais relevante na primeira posição (Top-1), expandindo para 94,1% quando considerados os 5 documentos recuperados (Top-5). Estes resultados indicam eficácia da recuperação semântica via embeddings E5 multilingual.

<div align="center">
<sub>Tabela 14 – Distribuição de latência por percentil</sub>

| Percentil | Latência Total | Recuperação | Geração | Observação |
|-----------|---------------|-------------|---------|------------|
| P50 (Mediana) | 351ms | 22ms | 329ms | Caso típico |
| P75 | 412ms | 28ms | 384ms | Aceitável |
| P90 | 487ms | 34ms | 453ms | Limite aceitável |
| P95 | 542ms | 39ms | 503ms | Requer otimização |
| P99 | 681ms | 48ms | 633ms | Crítico |
| Máximo | 823ms | 67ms | 756ms | Outlier (consultas complexas) |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&emsp;A distribuição de latência mostra que 90% das consultas são atendidas em menos de 487ms, com a mediana em 351ms. Contudo, 5% das consultas (P95-P100) excedem o limiar desejável de 500ms, atingindo até 823ms em casos extremos. Análise qualitativa destes outliers revela correlação com consultas envolvendo múltiplos atributos (ex: "vestido vermelho, longo, decote V, para casamento") que resultam em maior tempo de geração devido à complexidade da resposta.

## 4.9. Sumário quantitativo consolidado

&emsp;A Tabela 15 consolida os principais indicadores numéricos obtidos no desenvolvimento e avaliação do sistema completo.

<div align="center">
<sub>Tabela 15 – Dashboard consolidado de métricas do sistema</sub>

| Dimensão | Métrica | Valor | Interpretação |
|----------|---------|-------|---------------|
| **Classificação de Intenções** | | | |
| | Corpus total | 1.439 mensagens | 16 categorias |
| | Acurácia SVM | 70,8% | Melhor modelo |
| | Acurácia Balanceada SVM | 69,8% | +11,5 pp vs. RF |
| | F1-Macro SVM | 0,681 | Concordância substancial |
| | Kappa SVM | 0,680 | Landis-Koch |
| | Categorias automatizáveis (F1>0,80) | 3 (23,6% volume) | saudacao, agradecimento, reacao_emocional |
| | Categorias críticas (F1<0,50) | 6 (17,6% volume) | Requerem atenção |
| | Confiança média SVM | 85,7% | vs. 27,5% RF |
| | Predições alta confiança (>80%) | 68,2% | Viabiliza threshold |
| **Geração de Respostas** | | | |
| | Corpus fine-tuning | 1.000 pares Q&A | 90/10 treino/teste |
| | Dimensão embeddings | 896d | Qwen hidden states |
| | Clusters semânticos ótimos | 10 | k-means |
| | Silhouette Score | 1,000 | Separação perfeita |
| | Calinski-Harabasz Score | 1,97×10¹⁴ | Máxima dispersão inter/intra |
| | Variações linguísticas | 50.173 pares | Taxa 5.017% |
| | Redução alucinações | 72% | Fine-tuned vs. base |
| | Ganho especificidade | 150% | Entidades nomeadas |
| | Ganho coerência | 129% | Eliminação contradições |
| | Redução comprimento | 59% | 142→58 tokens médios |
| **Sistema RAG** | | | |
| | Documentos indexados | 1.504 | 1.500 produtos + 4 políticas |
| | Método indexação | FAISS | Inner product normalizado |
| | Modelo embeddings | E5-multilingual-base | 768d |
| | Latência total média | 363ms | Dentro do aceitável (<500ms) |
| | Latência recuperação | 23ms | Top-5 documentos |
| | Latência geração | 340ms | 256 tokens max |
| | Contexto relevante | 87,3% | 4,37/5 docs pertinentes |
| | Cobertura catálogo | 94,2% | 1.415/1.500 produtos |
| | Acerto Top-1 | 73,4% | Documento mais relevante |
| | Acerto Top-5 | 94,1% | Expandido para 5 docs |
| **Infraestrutura** | | | |
| | Modelo embeddings classificação | BERT-pt-cased | 768d, 128 tokens max |
| | Modelo LLM base | Qwen2.5-0.5B | 0,5B parâmetros |
| | Técnica fine-tuning | LoRA | r=8, α=16, dropout=0,05 |
| | Camadas LoRA | q,k,v,o_proj | Projeções atenção |
| | Épocas treinamento | 1 | Learning rate 2e-4 |
| | Hardware | GPU T4 | Colab, 15GB VRAM |
| | Tempo inferência embedding | 100ms/msg | Classificação |
| | Throughput geração | 75 tokens/s | 340ms para 256 tokens |

<sup>Fonte: Material produzido pelos autores (2025)</sup>
</div>

&emsp;Este sumário consolida 42 indicadores quantitativos distribuídos em quatro dimensões principais: classificação de intenções (11 métricas), geração de respostas (9 métricas), sistema RAG (10 métricas) e infraestrutura técnica (12 especificações). Os resultados demonstram sistema funcional com desempenho adequado para MVP (Mínimo Produto Viável), apresentando capacidade de automação em 23,6% das interações com alta confiança, geração especializada com redução de 72% em alucinações, e latência de resposta dentro dos padrões de experiência conversacional (< 500ms em 90% dos casos).

## 5. ANÁLISE E DISCUSSÃO

### 5.1. Interpretação do desempenho em classificação de intenções

&emsp;O desempenho observado na classificação de intenções deve ser contextualizado frente aos benchmarks estabelecidos na literatura. Conforme apresentado na Seção 4.2, o modelo SVM alcançou acurácia de 70,8% e acurácia balanceada de 69,8%, valores significativamente inferiores aos 96%+ reportados para o dataset CLINC150 por Larson et al. (2019), que utilizou BERT fine-tunado em corpus de 23.700 exemplos balanceados. Esta diferença de 25,2 pontos percentuais reflete três fatores estruturais do presente trabalho: (i) volume de dados 16,5× menor (1.439 vs. 23.700), (ii) desbalanceamento de classe com razão 17,5:1 (nao_identificado/evento_presencial), conforme evidenciado na Figura 04, e (iii) ausência de fine-tuning do modelo BERT, utilizando apenas embeddings pré-treinados.

&emsp;Estudos em domínios especializados apresentam resultados mais próximos aos obtidos. Filippi et al. (2023) reportaram 77,2% ± 1,2% de acurácia com SlovakBERT fine-tuned para chatbot bancário, enquanto Chen e Wang (2024) alcançaram aproximadamente 80% com GPT-3.5-turbo fine-tuned no mesmo domínio. O desempenho de 70,8% deste trabalho posiciona-se 6,4 a 9,2 pontos percentuais abaixo desses benchmarks, diferença atribuível principalmente ao não-fine-tuning do modelo de embeddings e ao volume limitado de dados de treinamento. Nyckel (2024) [[6]](#ref-6) estabelece que classificadores de texto requerem entre 3.000-30.000 exemplos para performance otimizada em cenários multiclasse, enquanto este trabalho operou com 1.439 exemplos, ou seja, 52% abaixo do limiar mínimo sugerido.

&emsp;A análise por categoria (Tabela 03, Seção 4.3) revela padrão coerente com a literatura: classes com maior volume de exemplos apresentam melhor desempenho. As três categorias com F1 > 0,80 (saudacao, agradecimento, reacao_emocional) totalizam 340 exemplos (média 113/categoria), enquanto as oito categorias críticas com F1 < 0,60 somam apenas 331 exemplos (média 41/categoria), uma diferença de 175% no volume médio. Este resultado valida os achados de Ismail et al. [[4]](#ref-4) sobre a dependência crítica do volume de dados em tarefas de classificação de texto.

&emsp;A superioridade do SVM sobre o Random Forest, particularmente evidente na acurácia balanceada (+11,5 pp, conforme Tabela 02 da Seção 4.2), pode ser explicada por dois mecanismos técnicos: (i) melhor exploração da geometria vetorial dos embeddings BERT normalizados via StandardScaler, aproveitando a estrutura de alta dimensionalidade (768d) do espaço de representação, e (ii) robustez natural do SVM a desbalanceamento de classes através de margens maximais, conforme demonstrado por Huang et al. (2020) em análise comparativa de classificadores em cenários assimétricos.

### 5.2. Análise dos padrões de erro e confusões semânticas

&emsp;Os padrões de erro identificados na Figura 07 (Seção 4.5) concentram-se em três pares de confusão principais: (i) duvida_produto ↔ problema_tecnico (28 casos), (ii) interesse_produto ↔ duvida_produto (26 casos), e (iii) duvida_produto ↔ solicitacao_informacao (22 casos), representando conjuntamente 41% dos erros totais. A análise qualitativa desses casos revela sobreposição lexical significativa: 73% das confusões duvida_produto/problema_tecnico continham termos como "não funciona", "está errado" ou "não aparece", ambíguos entre dúvida sobre características do produto versus defeito técnico.

&emsp;Este resultado alinha-se com os achados de Gajula [[3]](#ref-3) sobre desafios de "ruído e ambiguidade (ironia/sarcasmo)" em análise de sentimentos, extensíveis à classificação de intenções. No domínio de moda, a distinção entre interesse_produto e duvida_produto é particularmente nebulosa: mensagens como "Tem esse vestido no P?" podem expressar tanto interesse em adquirir (se disponível) quanto dúvida sobre disponibilidade, requerendo contexto conversacional adicional não capturado por embeddings de mensagens isoladas.

&emsp;A análise de confiança (Figura 06, Seção 4.4) corrobora esta interpretação: o Random Forest apresentou confiança média de apenas 27,5%, com 68% das predições abaixo de 40%, indicando incerteza generalizada do modelo. Em contraste, o SVM concentrou 68% das predições acima de 80% de confiança, demonstrando maior assertividade. Especificamente, a mensagem "Onde está meu pedido?" obteve confiança de 91,2% no SVM versus 14,5% no Random Forest, diferença de 76,7 pontos percentuais que evidencia a superioridade do SVM na calibração de probabilidades em embeddings de alta dimensionalidade.

### 5.3. Validação do fine-tuning e ganhos qualitativos em geração

&emsp;A comparação qualitativa apresentada na Tabela 05 e Figura 09 (Seção 4.7) demonstra ganhos substanciais do modelo Qwen fine-tunado via LoRA. A redução de 72% em alucinações, observada através da eliminação de loops de repetição (exemplo: Pergunta 1 da Figura 09, onde o modelo base gerou 15 repetições da frase "regatas básicas" sem mencionar marcas), valida os achados de Hu et al. (2021) [[7]](#ref-7) sobre a eficácia de técnicas PEFT (Parameter-Efficient Fine-Tuning) para especialização de domínio com baixo orçamento computacional.

&emsp;O ganho de 85% em especificidade, quantificado pela presença de entidades nomeadas específicas do domínio (marcas "Rye T-shirt", "Tatá Martello", "My Basic" na resposta fine-tunada versus ausência total no modelo base), alinha-se diretamente com os requisitos levantados por Hui [[2]](#ref-2) sobre "facilidade de uso percebida" e "utilidade percebida" como determinantes da experiência do cliente em sistemas de PLN. A capacidade de fornecer recomendações acionáveis (exemplo: "Priorize modelos de design limpo em couro branco ou nude" na Pergunta 2) versus reafirmações genéricas ("Para looks elegantes, é importante escolher o tênis adequado") representa diferencial crítico para manutenção do "tom consultivo" objetivado pelo Curadobia.

&emsp;O ganho de 91% em coerência interna é exemplificado pela eliminação de contradições lógicas: na Pergunta 3 (Figura 09), o modelo base respondeu "Para roupas escuras, o preto é uma escolha clássica" quando questionado sobre alternativas "além do preto", enquanto o modelo fine-tunado forneceu resposta coerente ("O azul-marinho oferece contraste sutil"). Esta melhoria demonstra aprendizado de restrições pragmáticas do diálogo consultivo, não presentes no treinamento base do modelo.

### 5.4. Estrutura semântica e redundância do corpus de geração

&emsp;A análise de clustering (Figura 08 e Tabela 04, Seção 4.6) revelou estrutura semântica bem definida com Silhouette Score perfeito (1,000), indicando separação máxima entre os 10 clusters identificados. Embora este resultado sugira qualidade estrutural do corpus, a identificação de 50.173 variações linguísticas para 1.000 perguntas base (taxa de variação de 5.017%) indica redundância significativa: em média, cada pergunta possui 50 paráfrases no corpus.

&emsp;Esta redundância apresenta implicações ambivalentes: (i) **positiva**, facilita o aprendizado de variações linguísticas naturais (exemplo: "Como combinar tênis elegantemente?", "Tênis em looks formais, como fazer?", "Dicas para usar tênis com elegância"), essencial para robustez conversacional, conforme destacado por Gajula [[3]](#ref-3) sobre a importância de "tratar aspectos por atributo... linguagem coloquial de moda"; (ii) **negativa**, reduz a pressão de generalização durante fine-tuning, potencialmente inflando as métricas de separabilidade e limitando a capacidade do modelo de lidar com perguntas verdadeiramente novas fora da distribuição de treinamento.

&emsp;A distribuição equilibrada entre clusters (8,5%-12,1%, conforme Tabela 04) indica ausência de viés temático significativo no corpus de geração, contrastando positivamente com o desbalanceamento observado no corpus de classificação (23,1% em nao_identificado). Esta diferença reflete a natureza sintética controlada do corpus de geração versus a coleta orgânica do corpus de classificação, validando a estratégia de geração híbrida (transcrição automatizada + estruturação via LLM) descrita na Seção 3.11.

### 5.5. Desempenho do sistema RAG e latência operacional

&emsp;O sistema RAG apresentou latência total média de 363ms (23ms recuperação + 340ms geração, conforme Tabela 06 da Seção 4.8), enquadrando-se na faixa aceitável para experiência conversacional segundo Nielsen (1993), que estabelece limites de 100ms para resposta instantânea e 1.000ms para manter fluxo de pensamento do usuário. A taxa de contexto relevante de 87,3% demonstra eficácia da recuperação semântica via embeddings E5 multilingual, superando os 70-80% típicos de sistemas baseados em busca lexical (BM25), conforme documentado por Wang et al. (2023).

&emsp;A cobertura de catálogo de 94,2% indica que 5,8% dos produtos (aproximadamente 87 de 1.500) não são adequadamente recuperáveis via busca semântica, limitação atribuível a descrições de produtos insuficientemente ricas ou ambíguas. Esta lacuna representa risco operacional em cenário de produção: produtos não recuperáveis efetivamente "não existem" para o sistema, comprometendo a completude das recomendações e potencialmente gerando frustração do usuário.

&emsp;O tempo de geração de 340ms (média para 256 tokens novos) resulta em taxa de 1,33 tokens/ms ou 75 tokens/segundo, inferior aos 100-150 tokens/segundo típicos de modelos de 7B parâmetros em hardware otimizado (GPUs A100), porém coerente com a execução em GPU T4 (arquitetura Turing, 2018) utilizada neste trabalho. A migração para hardware mais recente (Ampere/Hopper) ou técnicas de otimização (quantização INT8, KV-cache compartilhado) poderia reduzir latência em 40-60%, conforme benchmarks de Frantar et al. (2023).

### 5.6. Implicações para implementação no Curadobia

&emsp;Os resultados obtidos têm implicações diretas para a estratégia de implantação no e-commerce Curadobia, particularmente considerando o objetivo declarado de "escalar atendimento consultivo sem perder o diferencial competitivo fundamental" (Seção 1). A análise de desempenho por categoria (Tabela 03) permite priorização estratégica baseada em viabilidade técnica e impacto de negócio.

&emsp;**Categorias automatizáveis com alta confiança** (F1 > 0,80, 23,6% do volume): saudacao, agradecimento e reacao_emocional podem ser completamente automatizadas, liberando aproximadamente 340 interações humanas por cada 1.439 atendimentos (23,6% de deflexão potencial). Esta automação, contudo, apresenta baixo impacto comercial direto, pois tais categorias raramente envolvem transações ou recomendações de produtos. Hui [[2]](#ref-2) identifica que "facilidade de uso" e "influência social" afetam positivamente a experiência, sugerindo que respostas automatizadas rápidas e consistentes nessas categorias podem aumentar satisfação geral mesmo sem impacto transacional direto.

&emsp;**Categorias de médio risco** (0,60 < F1 ≤ 0,80, 53,4% do volume): solicitacao_informacao, confirmacao, nao_identificado, troca_devolucao e rastreamento_pedido representam 768 mensagens que poderiam ser semi-automatizadas com supervisão humana. A implementação de limiar de confiança de 80% (observado em 68% das predições do SVM, conforme Figura 06) permitiria roteamento automático de aproximadamente 522 mensagens (68% de 768), mantendo 246 mensagens (32%) para triagem humana. Esta abordagem híbrida mitiga riscos de erro em categorias transacionais enquanto captura ganhos de eficiência.

&emsp;**Categorias críticas não automatizáveis** (F1 < 0,60, 23,0% do volume): duvida_produto, interesse_produto, problema_tecnico e outras categorias minoritárias devem permanecer sob atendimento humano integral. Crucialmente, estas categorias incluem as interações de maior valor comercial (dúvidas e interesse em produtos), validando a estratégia de fallback humano para preservar "o tom próximo, empático e humanizado que caracteriza a consultoria de moda tradicional".

&emsp;A integração do sistema RAG (Seção 4.8) com latência de 363ms possibilita uso como ferramenta de suporte ao atendente humano: ao receber uma duvida_produto, o sistema pode fornecer contexto relevante do catálogo em tempo real (< 500ms), permitindo que o atendente humano mantenha o tom consultivo enquanto acessa informações precisas instantaneamente. Esta configuração híbrida alinha-se com os achados de Ismail et al. [[4]](#ref-4) sobre ganhos de "lealdade do cliente" (correlação de 78%) quando PLN e personalização são aplicados conjuntamente.

### 5.7. Comparação com trabalhos relacionados e posicionamento

&emsp;A Tabela 07 sintetiza o posicionamento deste trabalho frente aos trabalhos relacionados analisados na Seção 2.

<div align="center">
<sub>Tabela 07 – Comparação com trabalhos relacionados</sub>

| Aspecto | Hui [[2]](#ref-2) | Gajula [[3]](#ref-3) | Ismail et al. [[4]](#ref-4) | Este Trabalho |
|---------|------|--------|-------------|---------------|
| **Foco Principal** | Fatores experiência usuário | Recomendação com sentimentos | Impacto PLN em negócio | Chatbot consultivo moda |
| **Metodologia** | Quantitativa (hipóteses) | Revisão literatura | Empírica (regressão) | Experimental (ML + LLM) |
| **Métricas Reportadas** | Alfas confiabilidade, efeitos | Benchmarks, práticas | r≈0,78, +5,28% vendas, ROI≈400% | Acurácia 70,8%, F1 0,681 |
| **Implementação Prática** | Não (modelo teórico) | Não (revisão) | Parcial (sem detalhes) | Sim (MVP funcional) |
| **Domínio Específico** | Geral e-commerce | Geral recomendação | Geral e-commerce | Moda (brasileiro) |
| **Tratamento Desbalanceamento** | Não aplicável | Mencionado como desafio | Não abordado | SVM com ganho +11,5 pp |
| **Considerações Éticas** | Limitado | Fairness/privacidade discutido | 85% satisfeitos com privacidade | Implementado (consentimento) |

<sup>Fonte: Análise comparativa pelos autores (2025)</sup>
</div>

&emsp;Este trabalho distingue-se pela implementação prática end-to-end de sistema conversacional em domínio especializado (moda brasileira), enquanto os trabalhos relacionados focam em aspectos teóricos (Hui), revisão de literatura (Gajula) ou análise empírica sem detalhamento técnico completo (Ismail et al.). A contribuição principal reside na demonstração de viabilidade técnica de MVP com dados limitados e desbalanceados (1.439 exemplos, razão 17,5:1), cenário típico de startups/PMEs no mercado brasileiro, através da estratégia híbrida classificador (SVM) + gerador (Qwen fine-tuned) + RAG.

&emsp;Limitações compartilhadas com os trabalhos relacionados incluem: (i) ausência de testes A/B em produção para validar impacto real em KPIs de negócio (conversão, CSAT, AHT), conforme apontado por Gajula [[3]](#ref-3); (ii) tratamento insuficiente de sarcasmo e gírias específicas de moda, destacado como desafio persistente por todos os autores; (iii) generalização limitada além do contexto específico (startup brasileira de moda versus e-commerce genérico), similar à limitação de escopo identificada em Hui [[2]](#ref-2).

### 5.8. Limitações do estudo e ameaças à validade

#### 5.8.1. Limitações dos dados

&emsp;A principal limitação estrutural reside no volume e qualidade dos dados de treinamento. O corpus de 1.439 mensagens situa-se 52% abaixo do limiar mínimo de 3.000 exemplos sugerido por Nyckel [[6]](#ref-6) para classificação multiclasse otimizada, explicando parcialmente o gap de 25,2 pontos percentuais em relação aos benchmarks (70,8% vs. 96%+ no CLINC150). O desbalanceamento severo (razão 17,5:1) exacerba esta limitação: categorias minoritárias como evento_presencial (19 exemplos) e interesse_produto (143 exemplos) apresentam volume insuficiente para aprendizado robusto, evidenciado por F1-Scores críticos de 0,29 para ambas (Tabela 03).

&emsp;A qualidade dos dados apresenta inconsistências significativas: 23,1% do corpus concentra-se na categoria nao_identificado, indicando ambiguidade na taxonomia manual. Mensagens de 1 caractere (emoticons isolados), frases vagas ("qual foi a mensagem?") e sarcasmo não-rotulado ("na verdade foi o porteiro, rs!") introduzem ruído que compromete a aprendizagem supervisionada. Esta limitação é reconhecida por Gajula [[3]](#ref-3) como desafio persistente em análise de sentimentos, extensível à classificação de intenções.

#### 5.8.2. Limitações metodológicas

&emsp;A ausência de fine-tuning do modelo BERT constitui limitação metodológica deliberada, adotada por restrições de orçamento computacional (GPU T4, 15GB VRAM) e tempo de projeto. Estudos demonstram ganhos de 15-25% em acurácia com fine-tuning específico de domínio (Chen & Wang, 2024), sugerindo que o desempenho observado de 70,8% poderia alcançar 85-95% com ajuste adicional. Esta limitação representa trade-off consciente entre viabilidade técnica (MVP) e performance otimizada.

&emsp;A redundância do corpus de geração (50.173 variações para 1.000 perguntas base, taxa 5.017%) ameaça a validade externa dos resultados qualitativos. O Silhouette Score perfeito de 1,000 pode refletir memorização de paráfrases em vez de generalização semântica, limitando a capacidade do modelo de lidar com perguntas verdadeiramente novas. Validação adicional com conjunto de teste out-of-distribution seria necessária para quantificar esta ameaça.

#### 5.8.3. Limitações de generalização

&emsp;Os resultados são específicos ao contexto do Curadobia (segmento moda curada, modelo marketplace) e podem não generalizar para: (i) e-commerces de moda fast-fashion com vocabulário distinto, (ii) mercados internacionais com padrões conversacionais diferentes, (iii) categorias de produto além de vestuário (calçados, acessórios, joias). A validação em Hui [[2]](#ref-2) sobre limitações de generalização em construtos perceptuais aplica-se integralmente a este trabalho.

&emsp;Adicionalmente, a ausência de métricas operacionais reais (CSAT, AHT, FCR, taxa de conversão) limita a interpretação de impacto de negócio. As métricas técnicas reportadas (acurácia, F1, latência) são necessárias mas insuficientes para validar o objetivo declarado de "escalar atendimento consultivo sem perder o diferencial competitivo". Testes A/B em produção, conforme destacado por Gajula [[3]](#ref-3) como lacuna na literatura, seriam essenciais para esta validação.

### 5.9. Direções futuras e roadmap técnico

&emsp;As limitações identificadas orientam roadmap técnico estruturado em três horizontes temporais:

**Curto prazo (0-3 meses):**
- Expansão do corpus de classificação para mínimo 5.000 exemplos via anotação incremental de mensagens reais + data augmentation sintética (backtranslation, paráfrase via LLM), priorizando categorias críticas (F1 < 0,60);
- Implementação de limiar de confiança de 80% no SVM para roteamento híbrido (automação alta confiança + fallback humano baixa confiança), capturando ganhos imediatos em categorias de cortesia (23,6% deflexão potencial);
- Deduplicação do corpus de geração para reduzir redundância de 5.017% para ~500-1.000%, aumentando pressão de generalização no fine-tuning.

**Médio prazo (3-6 meses):**
- Fine-tuning do modelo BERT português no corpus específico de moda (técnica TAPT - Task-Adaptive Pre-Training), targeting ganho de 15-20% em acurácia para alcançar 85%+;
- Integração de análise de sentimentos por aspecto (caimento, tecido, cor, ocasião) via modelos ABSA (Aspect-Based Sentiment Analysis), alinhando-se às recomendações de Gajula [[3]](#ref-3);
- Implementação de métricas automáticas para geração (ROUGE, BERTScore, GPTScore) e avaliação de faithfulness quando RAG ativo, estabelecendo pipeline de avaliação contínua.

**Longo prazo (6-12 meses):**
- Testes A/B em produção comparando (i) atendimento 100% humano, (ii) híbrido com limiar 80%, (iii) híbrido com limiar 60%, medindo CSAT, AHT, taxa de conversão e NPS, validando impacto em KPIs de negócio conforme framework de Ismail et al. [[4]](#ref-4);
- Desenvolvimento de capacidades multimodais (análise de imagens de produtos, reconhecimento de fotos de clientes para recomendação por similaridade visual), expandindo além de PLN puro;
- Implementação de guardrails éticos: detecção de viés linguístico (gênero, idade, classe social) em recomendações, auditoria de fairness via métricas de paridade demográfica, e controle de alucinações via external knowledge grounding.

## 6. CONCLUSÃO

&emsp;Este trabalho investigou a viabilidade de desenvolvimento de um sistema de chatbot consultivo para e-commerce de moda, aplicando técnicas de Processamento de Linguagem Natural e Inteligência Artificial Generativa para automatizar atendimento ao cliente preservando características consultivas. O objetivo central de "automatizar processos de atendimento mantendo o tom próximo, empático e humanizado que caracteriza a consultoria de moda tradicional" foi parcialmente atingido, conforme demonstrado pelos resultados apresentados na Seção 4.

&emsp;O sistema desenvolvido comprovou-se viável como Mínimo Produto Viável (MVP) para prototipagem e validação conceitual. Conforme detalhado na Seção 4, a arquitetura híbrida combinando classificação de intenções (SVM com embeddings BERT) e geração especializada (Qwen fine-tunado via LoRA) demonstrou capacidade de automação seletiva: categorias de cortesia e acolhimento apresentaram desempenho adequado para automação completa, enquanto categorias de alto valor comercial requerem estratégia híbrida com suporte humano. A integração do sistema RAG possibilitou respostas contextualizadas baseadas em catálogo de produtos com latência aceitável para aplicações conversacionais.

&emsp;As limitações identificadas na Seção 5 evidenciam que, embora funcional, o sistema atual não atinge os padrões de automação completa observados em benchmarks da literatura. O volume reduzido de dados de treinamento, o desbalanceamento entre categorias e a ausência de fine-tuning específico do modelo de embeddings constituem fatores limitantes que impactam o desempenho geral. Estas limitações, contudo, são típicas de contextos de startups e PMEs brasileiras, validando a relevância prática da solução desenvolvida para cenários com recursos computacionais e orçamentários restritos.

&emsp;A principal contribuição científica deste trabalho reside na demonstração empírica de que soluções conversacionais baseadas em PLN e IA generativa são implementáveis em domínios especializados (moda brasileira) com dados limitados, através de arquitetura pragmática que prioriza automação de baixo risco enquanto preserva intervenção humana em interações críticas. Esta abordagem híbrida, fundamentada em limiares de confiança e análise quantitativa de desempenho por categoria, oferece modelo replicável para empresas que buscam equilibrar eficiência operacional com manutenção de diferencial competitivo baseado em atendimento consultivo especializado.

&emsp;Para trabalhos futuros, recomenda-se três frentes de desenvolvimento: **(i) Expansão e balanceamento do corpus** de treinamento, prioritariamente para categorias críticas identificadas na Seção 4, com implementação de técnicas de data augmentation e deduplicação do corpus de geração; **(ii) Otimização arquitetural** através de fine-tuning específico do modelo BERT no domínio de moda e integração de capacidades de análise de sentimentos por aspecto (caimento, tecido, ocasião de uso), conforme lacunas identificadas na revisão de literatura; **(iii) Validação em ambiente de produção** mediante testes A/B que estabeleçam conexão mensurável entre métricas técnicas (acurácia, latência) e indicadores de negócio (CSAT, taxa de conversão, NPS), superando a principal limitação metodológica deste trabalho destacada na Seção 5.

&emsp;Adicionalmente, sugere-se investigação de capacidades multimodais (análise de imagens de produtos e clientes para recomendação por similaridade visual) e implementação de guardrails éticos para detecção de vieses linguísticos e controle de alucinações, temas emergentes em sistemas de IA generativa aplicados ao varejo. A evolução deste trabalho poderá contribuir para o avanço do conhecimento sobre sistemas conversacionais em domínios especializados de alta subjetividade, nos quais a automação completa permanece desafiadora devido à natureza consultiva e contextual das interações.

# Referências

<a id="ref-1"></a>
[1] LANDIM, A. R. D. B. et al. Analysing the effectiveness of _chatbots_ as recommendation systems in fashion e-commerce: a cross-cultural comparison. **Computers in Human Behavior**, v. 142, 107659, 2024. Disponível em: <https://discovery.researcher.life/article/analysing-the-effectiveness-of-*chatbots*-as-recommendation-systems-in-fashion-e-commerce-a-crosscultural-comparison/8f0aebee9855310fa6db39654f2957a1>. Acesso em: 11 ago. 2025.

<a id="ref-2"></a>
[2] HUI, Kuek Shu. The Role of Natural Language Processing in Improving Customer Service and Support in E-Commerce. 15 dez. 2023. Disponível em: <http://eprints.utar.edu.my/6295/1/202306-51_Kuek_Shu_Hui_KUEK_SHU_HUI.pdf>. Acesso em: 11 ago. 2025.

<a id="ref-3"></a>
[3] GAJULA, Yogesh. Sentiment-Aware Recommendation Systems in E-Commerce: A Review from a Natural Language Processing Perspective. 3 maio 2025. Disponível em: <https://arxiv.org/abs/2505.03828>. Acesso em: 11 ago. 2025.

<a id="ref-4"></a>
[4] ISMAIL, Walaa Saber; GHAREEB, Marwa M.; YOUSSRY, Howida. Enhancing Customer Experience through Sentiment Analysis and Natural Language Processing in E-commerce. 30 set. 2024. Disponível em: <https://jowua.com/wp-content/uploads/2024/10/2024.I3.005.pdf>. Acesso em: 11 ago. 2025.

<a id="ref-5"></a>
[5] FASTAPI. FastAPI framework, high performance, easy to learn, fast to code, ready for production. Disponível em: <https://fastapi.tiangolo.com/>. Acesso em: 28 ago. 2025.

<a id="ref-6"></a>
[6] NYCKEL. How much training data is needed for classification? 24 maio 2024. Disponível em: <https://www.nyckel.com/blog/classification-training-data-needs/>. Acesso em: 11 set. 2025

<a id="ref-7"></a>
[7] HU, E. J. et al. LoRA: Low-Rank Adaptation of Large Language Models. arXiv:2106.09685, 2021. Disponível em: <https://arxiv.org/abs/2106.09685>. Acesso em: 11 set. 2025.

</div>
