<div align="justify">

# Chatbot Consultivo para E-commerce de Moda: Aplicação de PLN e IA Generativa em Sistema de Recomendação Personalizada

Ana Luisa Goes Barbosa, Gabriel Coletto Silva, Gabriel Farias, Hugo Noyma, João Paulo Santos, Lucas Nogueira Nunes, Mauro das Chagas Junior, Vitto Mazeto

# Abstract

...

# 1. Introdução

&emsp;O *e-commerce* de moda tem experimentado transformações aceleradas, especialmente após a pandemia de COVID-19, que forçou a migração de serviços tradicionalmente presenciais para o ambiente digital. Neste cenário, empresas enfrentam o complexo desafio de equilibrar personalização e escalabilidade no atendimento ao cliente, precisando automatizar o suporte sem comprometer a qualidade consultiva. O segmento de moda apresenta particularidades únicas, pois as decisões de compra envolvem aspectos subjetivos como estilo pessoal, ocasião de uso e preferências estéticas que demandam orientação especializada. *chatbots* baseados em Processamento de Linguagem Natural (PLN) e técnicas de Inteligência Artificial Generativa emergem como solução promissora para conciliar eficiência operacional com experiência personalizada, oferecendo potencial para revolucionar o atendimento no *e-commerce* de moda (LANDIM et al., 2024) [[1]](#ref-1).

&emsp;O Curadobia, *marketplace* focado em curadoria especializada de moda, exemplifica perfeitamente essa necessidade emergente do mercado. A empresa, que se posiciona como consultoria de moda integrada ao varejo digital, busca escalar seu atendimento consultivo sem perder o diferencial competitivo fundamental: oferecer orientação personalizada sobre combinações, modelagem, caimento e estilo de vida. Com mais de 20 marcas parceiras e um ano de operação, o Curadobia enfrenta a limitação de manter seu DNA de "peças com história" e experiência de compra guiada conforme cresce. O desafio central é automatizar processos de atendimento mantendo o tom próximo, empático e humanizado que caracteriza a consultoria de moda tradicional, sem recorrer a respostas genéricas ou robóticas que comprometeriam a proposta de valor da marca.

&emsp;Este trabalho propõe o desenvolvimento de um sistema de *chatbot* inteligente capaz de responder dúvidas frequentes e oferecer recomendações de produtos de forma consultiva e personalizada. O objetivo é criar uma solução baseada em PLN e IA generativa que preserve a identidade conversacional e o expertise em curadoria da marca, enquanto permite escalabilidade operacional através de algoritmos de recomendação contextualizados. A implementação busca integrar *machine learning* com o conhecimento especializado em moda, possibilitando interações naturais que mantenham o padrão de qualidade do atendimento humano. Espera-se que a solução contribua tanto para a otimização de recursos da empresa quanto para o avanço do conhecimento em sistemas conversacionais aplicados ao varejo especializado.

# 2. Trabalhos Relacionados

&emsp;A revisão de literatura foi conduzida entre julho e agosto de 2025, utilizando como base o Google Scholar. As consultas foram realizadas com combinações de termos em inglês e português, tais como: *“fashion e-commerce chatbot recommendation system”*, *“sentiment analysis personalized recommendation”*, *“generative AI conversational agent retail”* e *“chatbot consultivo moda”*, entre outras variações. Foi priorizado artigos publicados entre 2024 e 2025, de modo a refletir o estado da arte sobre PLN e IA generativa aplicados ao atendimento digital em varejo.

&emsp;Esta seção revisa a literatura recente sobre o uso de Processamento de Linguagem Natural (PLN) e Análise de Sentimentos em *e-commerce*, com foco em experiências de atendimento via *chatbot* e recomendações personalizadas. Três frentes emergem de forma consistente: (i) fatores humanos que moldam a experiência do cliente com tecnologias de PLN em atendimento, (ii) incorporação de sentimentos de textos (avaliações, comentários) em sistemas de recomendação, e (iii) evidências quantitativas de impacto em lealdade, vendas e retorno financeiro, bem como desafios de privacidade, justiça e reprodutibilidade.

## 2.1. Análise dos trabalhos

&emsp;O primeiro trabalho analisado neste artigo demonstra uma investigação conduzida por Hui [[2]](#ref-2) e realizada por meio de hipóteses testadas empiricamente, com o objetivo de definir quais fatores determinam a experiência e a satisfação do cliente ao interagir com tecnologias de PLN no contexto de *e-commerce*. Os resultados apontam que a facilidade de uso percebida, a influência social e a aprendizagem por observação têm efeitos positivos e significativos sobre a experiência do cliente; a utilidade percebida e a autoeficácia, por outro lado, não se mostraram determinantes. Além disso, a experiência do cliente exerce impacto significativo sobre a satisfação. Pontos positivos incluem a robustez psicométrica dos instrumentos (altas confiabilidades) e implicações gerenciais claras (priorizar usabilidade e alavancar prova social). Entre as limitações, destacam-se a ênfase em construtos perceptuais (com pouca medição comportamental objetiva, como tempo de resolução ou taxa de desvio para o humano), a ausência de métricas operacionais de suporte (ex.: Tempo Médio de Atendimento ou AHT, Satisfação do Cliente ou CSAT, Resolução no Primeiro Contato ou FCR) e a generalização para domínios específicos (moda) ainda aberta.

&emsp;Atuando em uma frente com foco distinto, Gajula [[3]](#ref-3) apresenta em sua pesquisa uma revisão abrangente sobre recomendações sensíveis a sentimentos, destacando a transição de abordagens manuais e modelos rasos para arquiteturas profundas e, mais recentemente, modelos baseados em transformadores e representações gráficas (grafos de conhecimento que conectam usuários, itens e aspectos/opiniões). O trabalho ressalta tendências de 2023–2025: reprodutibilidade (conjuntos de ferramentas, sementes aleatórias ou *seeds*, rastreamento de experimentos), métricas além de acurácia (diversidade, novidade, qualidade/explicabilidade de recomendações), e o papel de Modelos de Linguagem de Grande Porte (LLMs) tanto na compreensão de texto quanto na geração de explicações. Também sistematiza desafios persistentes: ruído e ambiguidade (ironia/sarcasmo), alinhamento de sentimentos por aspecto, preferência dinâmica/temporal, início a frio (*cold start*), escalabilidade e justiça algorítmica (*fairness*)/privacidade. Como pontos fortes, a revisão orienta boas práticas experimentais e transparência; como limitações, há pouca evidência de estudos com testes A/B em produção e menor foco no fluxo de suporte conversacional (embora os achados sejam diretamente úteis para motores de recomendação em *marketplaces* de moda).

&emsp;Por fim, Ismail, Ghareeb e Youssry [[4]](#ref-4) conduzem uma análise empírica relacionando *scores* de sentimento, uso de recursos de PLN e personalização com lealdade do cliente, crescimento de vendas e Retorno sobre o Investimento (ROI). Os autores reportam correlação forte entre sentimento e lealdade (um fator de aproximadamente 78%), efeito positivo dos recursos de PLN na lealdade, ganho de vendas associado a recomendações personalizadas (+5,28% por incremento de personalização) e ROI aproximado de 400% em cenário exemplificativo. O estudo também indica alto nível de satisfação dos usuários com privacidade (85%) e alerta para variações culturais/linguísticas que afetam a acurácia de análises de sentimento. Entre os pontos positivos, destacam-se a quantificação de impacto de negócio e a discussão ética; como limitações, permanecem questões de generalização (tamanho/amostra, controles de confusão) e suposições de ROI, além de necessidade de maior detalhamento metodológico para plena reprodutibilidade.

## 2.2. Síntese e lacunas

&emsp;Em conjunto, os trabalhos convergem para diretrizes úteis ao desenvolvimento de um *chatbot* de suporte para um *marketplace* de roupas. Em suma:

- A experiência do usuário depende criticamente de usabilidade e sinais sociais (ex.: avaliações/indicadores de confiança) [[2]](#ref-2);
- Incorporar sentimentos de textos dos clientes melhora a personalização (produtos, respostas e explicações), mas exige tratar aspectos por atributo (tamanho, tecido, caimento), linguagem coloquial de moda e dinâmica temporal (tendências/estações) [[3]](#ref-3);
- Há evidências de ganhos em lealdade, vendas e ROI quando sentimentos e PLN são aplicados com personalização, desde que se considerem privacidade e diferenças culturais [[4]](#ref-4).

&emsp;Entretanto, persistem lacunas em: (i) detecção de sarcasmo e gírias da moda, (ii) métricas padronizadas que conectem ganhos *offline* (Raiz do Erro Quadrático Médio e Taxa de Acerto) a impacto real (deflexão de chamados, CSAT, conversão), (iii) pipelines reprodutíveis ponta a ponta (dados, *prompts*, *seeds*), e (iv) *fairness* (evitar vieses em linguagem/avaliações). Essas limitações se traduzem em importantes pontos de atenção para o desenvolvimento desta pesquisa, que devem ter seus respectivos níveis de impacto sobre o projeto avaliados para que sejam concebidas tratativas eficazes.

## 2.3. Comparação entre trabalhos

&emsp;A seguir, apresenta-se uma tabela de *benchmark* (Tabela 01) entre os diferentes trabalhos analisados e discutidos nas seções anteriores deste documento, a fim de comparar seus objetivos, resultados e impacto ou relação ao projeto em desenvolvimento.

<div align="center">
<sub>Tabela 01 – Comparação entre os trabalhos relacionados</sub>

| Trabalho                                                       | Escopo/Tipo                                                             | Metodologia/Dados                                                                            | Principais resultados                                                                                                                                   | Métricas/Relatos                                                                   | Pontos positivos                                                              | Limitações                                                                                     |
| -------------------------------------------------------------- | ----------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| [[2]](#ref-2) Hui – The Role of NLP…                           | Modelo de aceitação e experiência em atendimento com PLN (quantitativo) | Hipóteses H1–H6; testes de confiabilidade e significância                                    | Facilidade de uso, influência social e aprendizagem por observação → experiência; experiência → satisfação; utilidade e autoeficácia não significativas | Alfas de confiabilidade elevados; efeitos significativos reportados                | Implicações gerenciais claras (priorizar usabilidade e prova social)          | Pouca métrica operacional (AHT, FCR); foco perceptual; generalização para domínios específicos |
| [[3]](#ref-3) Gajula – Sentiment-aware Recommendation Systems… | Revisão (2023–2025) de recomendação com sentimentos                     | Síntese de estado da arte: transformadores, grafos, LLMs; boas práticas de reprodutibilidade | Integração de sentimentos melhora precisão/explicabilidade; desafios: sarcasmo, aspectos, tempo, *cold start*, escalabilidade, *fairness*/privacidade   | Ênfase em padrões de *benchmarks*, *seeds*, protocolos e métricas além de acurácia | Direciona práticas transparentes e comparáveis; visão ampla do estado da arte | Falta de evidências de testes A/B em produção; foco menor em suporte conversacional            |
| [[4]](#ref-4) Ismail et al. – Enhancing Customer Experience…   | Estudo empírico de impacto de PLN/sentimentos                           | Descritivo + regressão; variáveis de lealdade, vendas, satisfação, privacidade               | r≈0,78 (sentimento↔lealdade); +5,28% vendas por incremento de personalização; ROI≈400%; 85% satisfeitos com privacidade                                 | Estatísticas descritivas; t-values/p-values reportados                             | Quantifica impacto de negócio e aborda ética/privacidade                      | Generalização e suposições de ROI; necessidade de mais detalhes metodológicos                  |

<sup>Fonte: Material produzido pelos próprios autores (2025)</sup>

</div>

## 2.4. Implicações para o projeto

&emsp;Haja vista a análise supracitada, é possível determinar importantes ações e diretrizes que podem ser aplicadas a este projeto. Dentre elas, destacam-se:  

- Priorizar a Experiência do Usuário (UX) do *chatbot* (clareza, tempo de resposta, linguagem da marca);  
- Alavancar evidência social (avaliações/fotos de clientes) no diálogo;  
- Usar análise de sentimentos para personalizar recomendações e explicações por aspecto (ex.: caimento, tecido, tamanho);  
- Adotar práticas robustas de reprodutibilidade (versionamento de dados, *seeds*, rastreamento de experimentos, contêineres);  
- Monitorar métricas de produto e suporte (deflexão, Satisfação do Cliente (CSAT), Tempo Médio de Atendimento (AHT), taxa de conversão e repetição de compra);  
- Tratar privacidade/consentimento e vieses linguísticos/culturais do domínio de moda;  
- Considerar implicações do uso de IA generativa, como controle de alucinações, calibragem de respostas consultivas e alinhamento com a identidade da marca, garantindo transparência e confiabilidade no atendimento.  

# 3. Materiais e Métodos

### 3.1. Aquisição e tratamento dos dados

&emsp;Os dados foram obtidos a partir de um arquivo CSV consolidado contendo mensagens de atendimento do Curadobia oriundas de WhatsApp e Instagram. A coluna `message` foi renomeada para `original`. Foram removidos valores nulos e os registros foram reindexados. Além do texto das mensagens, o conjunto incluía campos auxiliares como identificador da interação, data/hora, canal de origem e categoria inicial, que foram mantidos para apoiar etapas posteriores de análise e rastreabilidade. A taxonomia de *intents* que orienta o escopo do *chatbot* está presente no código de taxonomia e foi utilizada como referência para delimitar as categorias conversacionais.  

&emsp;Essas decisões asseguram padronização do campo-alvo ao longo do *pipeline*, evitam a propagação de registros vazios, preservam a rastreabilidade entre etapas e delimitam o escopo de *intents* que guiará a curadoria do corpus.

## 3.2. Análise exploratória de dados (AED)

&emsp;A AED foi conduzida nos notebooks de exploração e de pré-processamento com o objetivo de caracterizar o corpus e apoiar decisões de pré-processamento e modelagem, sem apresentação de resultados nesta seção. As atividades metodológicas incluíram: (i) cálculo do comprimento das mensagens em tokens, com estatísticas descritivas e histogramas, para orientar limites de truncamento e memória de diálogo; (ii) inspeção do vocabulário após normalização (remoção de *stopwords* e *stemming*) para identificar termos característicos do domínio e apoiar a definição de *intents*/*slots*; (iii) mapeamento das categorias temáticas para verificar cobertura e orientar estratégias de balanceamento; e (iv) organização dos artefatos da AED (tabelas e gráficos) diretamente a partir dos notebooks, garantindo reprodutibilidade e rastreabilidade.

## 3.3. Pré-processamento textual

&emsp;Foi implementado um *pipeline* leve e reprodutível no *notebook* de pré-processamento, composto pelas etapas:

- **lower**: conversão para minúsculas — normaliza a capitalização e reduz a sparsidade lexical;
- **strip_accents**: normalização Unicode e remoção de acentos — unifica variantes ortográficas (p.ex., "ação"/"acao");
- **remove_punctuation**: remoção de pontuação e símbolos — reduz ruído não lexical em representações baseadas em termos;
- **tokenize**: tokenização simples por espaço — viabiliza filtragem e transformações subsequentes por termo;
- **remove_stopwords**: remoção de stopwords em português — atenua termos de alta frequência com baixo poder discriminativo;
- **stem**: redução lexical com RSLPStemmer — agrupa flexões e variações morfológicas, favorecendo a generalização inicial.

&emsp;O *pipeline* é composto por funções puras e orquestrado por uma rotina de execução que produz um conjunto de colunas por etapa (de `original` até `stems`), mantendo rastreabilidade das transformações. A figura a seguir (Figura 01) ilustra o fluxo aplicado:

<div align="center">

<sub>Figura 01: Fluxo Pipeline de Pré-processamento</sub>

![Fluxo do pipeline de pré-processamento](imagens/figura-pipeline-pre-processamento.png)

<sup>Fonte: Material produzido pelos próprios autores por meio do Mermaid (2025).</sup>

</div>

&emsp;Em síntese, as etapas de aquisição, AED e pré-processamento constituem um *pipeline* padronizado, rastreável e reprodutível para sustentar as fases de modelagem e avaliação.

## 3.4. Resultados do processamento com o pipeline de pré-processamento

&emsp;Para evidenciar os efeitos do *pipeline* sobre o corpus, foram gerados gráficos a partir do *notebook* de pré-processamento. As imagens abaixo (Figuras 02 e 03) representam o impacto das transformações, acompanhadas de descrições textuais.

&emsp;Tabela síntese por etapa: estatísticas descritivas do comprimento das mensagens (p.ex., média, mediana e desvio-padrão) ao longo das etapas (`original` → `stems`), ilustrando a redução e normalização progressivas que simplificam a vetorização inicial.

<div align="center">

<sub>Figura 02: Estatísticas de comprimento por etapa do pipeline</sub>

![Tabela síntese por etapa do pipeline](imagens/tabela-comprimento-por-etapa.png)

<sup>Fonte: Produzido pelos autores a partir do notebook de pré-processamento (2025).</sup>

</div>

&emsp;Observa-se redução gradual do comprimento das mensagens entre as etapas, com menor variabilidade após a normalização e a remoção de *stopwords*. Esse comportamento é desejável, pois simplifica a vetorização inicial e orienta a definição de limites de janelamento para diálogos.

&emsp;Vocabulário característico do domínio: gráfico de barras dos Top-20 termos/stems após remoção de *stopwords* e *stemming*, útil para mapear *intents*, *slots* e preservar o tom consultivo.

<div align="center">

<sub>Figura 03: Top-20 termos/stems após pré-processamento</sub>

![Top-20 stems após pré-processamento](imagens/top20-stems.png)

<sup>Fonte: Produzido pelos autores a partir do notebook de pré-processamento (2025).</sup>

</div>

&emsp;O conjunto de termos/stems mais frequentes evidencia o vocabulário característico do domínio de moda e atendimento. Esses termos subsidiam a definição de *intents* e *slots* e ajudam a calibrar dicionários/ontologias, mantendo o tom consultivo da marca.

&emsp;Os resultados do processamento demonstram que o *pipeline* adotado reduz ruído superficial, normaliza o texto e preserva sinais semânticos relevantes. Esses artefatos orientam escolhas práticas do projeto (limites de *tokens*, políticas de memória de diálogo, curadoria de *intents* e *features* iniciais), além de garantirem reprodutibilidade por meio do *notebook* de processamento.

## 3.5. Classificador de intenções

&emsp;O sistema de classificação de intenções foi implementado a partir da combinação de *embeddings* gerados por BERT em português e um classificador baseado em *scikit-learn*. O modelo é disponibilizado em repositório no Hugging Face, o que permite reuso e controle de versões. Para garantir consistência, o serviço valida a dimensionalidade do vetor de entrada em relação ao classificador, assegurando a compatibilidade entre etapas de treinamento e inferência.

&emsp;Na etapa final, foram testados dois classificadores: Support Vector Machine (SVM) e Random Forest. Ambos foram avaliados sobre o mesmo conjunto de dados, permitindo comparação direta de desempenho.

## 3.6. Taxonomia de intenções

&emsp;A taxonomia definida para o chatbot contempla 16 intenções distintas: *dúvida_produto*, *solicitação_informação*, *reação_emocional*, *interesse_produto*, *agradecimento*, *rastreamento_pedido*, *saudação*, *solicitação_contato*, *mensagem_sistema*, *troca_devolução*, *problema_técnico*, *não_identificado*, *reposição_estoque*, *confirmação*, *parceria_comercial* e *evento_presencial*.

&emsp;O mapeamento *id2label* é explicitado no arquivo de configuração, garantindo alinhamento entre fases de treino e inferência.

**Quadro 1 – Taxonomia de intenções do chatbot**  

| Identificador | Intenção | Descrição breve |
|---------------|---------------------------|---------------------------------------------------------------------------------|
| 1 | *dúvida_produto* | Perguntas sobre especificações, tamanhos, variantes ou quantidades de produtos. |
| 2 | *solicitação_informação* | Requisição de informações gerais, políticas ou detalhes adicionais. |
| 3 | *reação_emocional* | Mensagens curtas de reação ou emoção (ex.: emojis, expressões afetivas). |
| 4 | *interesse_produto* | Demonstração de interesse em produtos específicos, tamanhos ou variantes. |
| 5 | *agradecimento* | Expressões de gratidão pelo atendimento. |
| 6 | *rastreamento_pedido* | Solicitações de status ou código de rastreio de pedidos. |
| 7 | *saudação* | Início de conversa com cumprimentos. |
| 8 | *solicitação_contato* | Pedido para ser contatado via WhatsApp, e-mail ou telefone. |
| 9 | *mensagem_sistema* | Mensagens automáticas ou de sistema. |
| 10 | *troca_devolução* | Solicitações para troca ou devolução de pedidos. |
| 11 | *problema_técnico* | Relato de falhas técnicas ou bugs, possivelmente com capturas de tela. |
| 12 | *não_identificado* | Mensagens ambíguas ou não classificadas. |
| 13 | *reposição_estoque* | Perguntas sobre disponibilidade futura de itens ou variantes. |
| 14 | *confirmação* | Respostas confirmando ações ou informações fornecidas. |
| 15 | *parceria_comercial* | Propostas de colaboração ou contato com o time comercial. |
| 16 | *evento_presencial* | Interações sobre participação em eventos presenciais. |

## 3.7. Geração de *embeddings*

&emsp;Os textos são convertidos em vetores densos utilizando o modelo *neuralmind/bert-base-portuguese-cased*, com truncamento em até *128 tokens* e agregação via *mean pooling*. Não foi realizado *fine-tuning*, sendo utilizado o modelo pré-treinado disponível publicamente.

&emsp;Durante o desenvolvimento, a extração de *embeddings* e o treinamento dos classificadores foram realizados na GPU T4 disponibilizada pelo ambiente Google Colab, usando aceleração por hardware para reduzir o tempo de processamento.

## 3.8. Roteamento e fluxos conversacionais

&emsp;As predições de intenção passam por um processo de normalização (conversão para minúsculas, remoção de acentos e substituição de espaços por sublinhados) antes de serem mapeadas para os respectivos *handlers*.

&emsp;O diálogo é conduzido por fluxos orientados a estados, nos quais cada intenção pode acionar transições específicas. Por exemplo, uma *dúvida_produto* pode levar à consulta do catálogo e, em seguida, a um estado de encerramento ou recomendação; já um pedido de *rastreamento_pedido* pode levar à consulta de status e envio do código de rastreio.

&emsp;O fluxo inclui também um estado de transição condicional (*encerrar_ou_recomendar*), que atua como ponto central para concluir ou expandir a interação.

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

&emsp;Cada intenção é associada a um *handler* responsável por gerar respostas modelo. O mecanismo utiliza mensagens pré-definidas e informações simuladas. Por exemplo, para um item de vestuário, pode-se indicar disponibilidade em estoque e variações de tamanho; no caso de rastreamento de pedidos, informar um status fictício.

&emsp;Esse recurso permite avaliar a experiência de diálogo sem depender de integrações externas. Em etapas posteriores, os *handlers* poderão ser estendidos para acionar consultas reais em sistemas de catálogo, logística ou pós-venda.

### 3.10.1. Respostas simuladas com variabilidade

&emsp;Como a solução ainda não está integrada a sistemas reais, algumas intenções utilizam geração randômica de respostas (por exemplo, produtos, tamanhos, cores, preços ou status de pedidos). Esse recurso, implementado com funções como *random.choice* e *random.randint*, introduz variabilidade controlada durante os testes, evitando respostas idênticas e possibilitando avaliar melhor a robustez dos fluxos conversacionais.

## 3.11. *Fine-tuning* de Modelos de Linguagem

&emsp;Para gerar respostas humanizadas específicas do domínio de moda, foi implementado o *fine-tuning* de modelos de linguagem. Após avaliação de diferentes arquiteturas (BERT, LLaMA e Qwen), foi selecionado o modelo *Qwen/Qwen2.5-0.5B* como base para especialização.

&emsp;A escolha do Qwen baseou-se em múltiplos critérios de avaliação. Em relação à performance base, o modelo demonstrou superior capacidade de compreensão e geração em português brasileiro quando comparado às alternativas, apresentando respostas mais coerentes e contextualmente apropriadas mesmo sem especialização. Quanto à praticidade para *fine-tuning*, o Qwen ofereceu maior facilidade de implementação com a técnica LoRA, compatibilidade nativa com formatos de conversa estruturados e menor demanda computacional durante o treinamento. Adicionalmente, o modelo apresentou melhor relação custo-benefício para o contexto de desenvolvimento em GPU T4, arquitetura otimizada para processamento eficiente de sequências conversacionais, e documentação técnica abrangente que facilitou a implementação e ajustes de hiperparâmetros.

&emsp;O processo utilizou a técnica LoRA (*Low-Rank Adaptation*) para treinamento eficiente, aplicada especificamente às camadas de projeção de atenção: `q_proj`, `k_proj`, `v_proj` e `o_proj`. Esta abordagem permite adaptar o modelo mantendo a maior parte dos parâmetros congelados, reduzindo significativamente o custo computacional.

&emsp;O conjunto de dados de treinamento foi construído a partir de 1.000 pares pergunta-resposta em português brasileiro, estruturados no formato de conversa com blocos delimitadores: `<|system|>` (instruções de comportamento e contexto), `<|user|>` (pergunta do usuário) e `<|assistant|>` (resposta esperada do modelo). Esta estruturação permite ao modelo aprender distinções claras entre diferentes tipos de conteúdo durante o diálogo. O conteúdo foi gerado através de um processo híbrido:

1. **Transcrição automatizada**: conversão de vídeos sobre moda em texto utilizando modelos de *speech-to-text*
2. **Estruturação via LLM**: processamento supervisionado para gerar pares pergunta-resposta baseados nas transcrições

&emsp;Os hiperparâmetros utilizados foram: taxa de aprendizado de $2e^{-4}$, *batch size* de 2 por dispositivo com acumulação de gradientes (fator 4), treinamento por 1 época, e configuração LoRA com r=8, α=16 e *dropout* de 0.05. O treinamento foi realizado em ambiente Google Colab utilizando GPU T4.

&emsp;O modelo resultante foi salvo em dois formatos: `.pkl` para carregamento simples via Python e `.safetensors` para uso em produção. A validação qualitativa demonstrou melhoria significativa na geração de respostas específicas do domínio quando comparado ao modelo base.

## 3.12. Sistema de Respostas Contextuais com RAG

&emsp;Foi implementado um sistema de *Retrieval-Augmented Generation* (RAG) para fornecer respostas contextuais baseadas em catálogo de produtos e políticas da empresa. O sistema combina recuperação semântica com geração especializada para oferecer sugestões personalizadas.

### 3.12.1. Construção do corpus e indexação

&emsp;O corpus foi construído com 1.504 documentos, sendo 1.500 produtos simulados e 4 documentos de políticas empresariais. O catálogo de produtos inclui informações detalhadas: nome, descrição, categoria, preço, estoque por tamanho, medidas corporais por tamanho, materiais e cores.

&emsp;Para indexação semântica, foram utilizados *embeddings* gerados pelo modelo `intfloat/multilingual-e5-base`, especializado em português brasileiro. Os textos foram processados com prefixo `passage:` para documentos e `query:` para consultas, seguindo as recomendações do modelo E5.

&emsp;O índice vetorial foi implementado utilizando FAISS (*Facebook AI Similarity Search*) com produto interno normalizado, permitindo busca eficiente por similaridade de cosseno. A normalização dos vetores garante que as pontuações sejam comparáveis e interpretáveis.

### 3.12.2. Pipeline de recuperação e geração

&emsp;O *pipeline* RAG segue as etapas:

1. **Codificação da consulta**: conversão da pergunta do usuário em vetor normalizado
2. **Recuperação top-k**: busca dos k documentos mais similares no índice FAISS (padrão k=5)
3. **Construção do contexto**: concatenação dos documentos recuperados com prefixos identificadores
4. **Geração da resposta**: utilização do modelo Qwen *fine-tunado* com *prompt* estruturado

&emsp;O *template* de *prompt* inclui instruções explícitas para: (i) responder apenas com base no contexto fornecido, (ii) não revelar identificadores internos como SKUs, (iii) manter o tom consultivo e elegante característico da marca, e (iv) indicar quando não há informação suficiente.

### 3.12.3. Parâmetros de geração

&emsp;A geração utiliza os seguintes parâmetros: máximo de 256 *tokens* novos, amostragem habilitada (*do_sample=True*), temperatura de 0.5 para balancear criatividade e consistência, e *top_p* de 0.9 para *nucleus sampling*. Esses valores foram ajustados empiricamente para manter respostas concisas e relevantes.

## 3.13. Análise Semântica Avançada

&emsp;Para identificação de padrões semânticos e agrupamentos temáticos, foi implementada uma análise avançada baseada em *clustering* de *embeddings*. O objetivo é compreender a estrutura semântica do corpus de perguntas e identificar variações linguísticas que expressam intenções similares.

### 3.13.1. Extração e processamento de *embeddings*

&emsp;Foram extraídos *embeddings* semânticos de 1.000 perguntas utilizando o modelo *fine-tunado* Qwen, resultando em representações vetoriais de 896 dimensões. A estratégia de extração utilizou o último estado oculto (*last_hidden_state*) das camadas de atenção, capturando representações contextualizadas específicas do domínio.

&emsp;Para visualização e análise exploratória, foram aplicadas três técnicas de redução de dimensionalidade:

- **PCA** (*Principal Component Analysis*): redução linear preservando máxima variância
- **t-SNE** (*t-Distributed Stochastic Neighbor Embedding*): visualização não-linear em 2D
- **UMAP** (*Uniform Manifold Approximation and Projection*): preservação de estrutura local e global

### 3.13.2. *Clustering* semântico otimizado

&emsp;O número ótimo de *clusters* foi determinado através de otimização baseada em duas métricas complementares:

- **Silhouette Score**: mede qualidade da separação entre *clusters*
- **Calinski-Harabasz Score**: avalia razão entre dispersão inter e intra-*cluster*

&emsp;O algoritmo K-Means identificou 10 *clusters* semânticos ótimos, apresentando Silhouette Score de 1.000 (separação perfeita) e Calinski-Harabasz Score de aproximadamente $1.97\times10^{14}$, indicando excelente separação entre grupos.

### 3.13.3. Análise de variações linguísticas

&emsp;O sistema identificou 50.173 variações linguísticas distribuídas entre os *clusters*, com taxa média de variação de 5.017%. Esta análise permite detectar diferentes formulações para expressar a mesma intenção, fundamental para robustez de sistemas de processamento de linguagem natural.

&emsp;A distribuição das perguntas entre os *clusters* mostrou-se relativamente equilibrada (8.5% a 12.1% por *cluster*), indicando ausência de viés significativo para temas específicos no conjunto de dados analisado.

# 4. Resultados

&emsp;Esta seção integra dois eixos complementares de avaliação do chatbot de moda: (i) classificação de intenções em cenário multiclasse e (ii) geração de respostas com modelo de linguagem especializado (Qwen) por *fine-tuning*. Apresentamos o escopo e a infraestrutura, as métricas quantitativas (global e por classe), indicadores de confiança e padrões de erro na classificação; em seguida, analisamos a estrutura semântica do corpus de geração e comparamos, qualitativamente, o modelo base e o modelo ajustado, finalizando com uma síntese das implicações.

---

&emsp;O conjunto de dados apresenta distribuição assimétrica entre as classes: a categoria nao_identificado concentra 333 exemplos (23%), enquanto evento_presencial possui 19 exemplos (1,3%). Em termos de infraestrutura, os *embeddings* foram extraídos com o modelo neuralmind/bert-base-portuguese-cased (truncamento em 128 tokens, mean pooling), e os classificadores foram treinados e avaliados em ambiente Google Colab com GPU T4

## 4.1. Escopo da avaliação e corpora

**Classificação de intenções (multiclasse).**  
&emsp;Corpus com 1.439 mensagens distribuídas em 16 intenções, com desbalanceamento acentuado (*nao\_identificado* = 333 exemplos, 23%; *evento\_presencial* = 19, 1,3%). Embeddings extraídos com `neuralmind/bert-base-portuguese-cased` (768 dimensões, truncamento em 128 tokens, *mean pooling*). Treino/avaliação em Google Colab (GPU T4).

**Geração de respostas (LLM especializado em moda).**  
&emsp;Conjunto de 1.000 pares pergunta–resposta (pt-BR), formatados em estilo de chat com SYSTEM\_PREFIX (“Você é uma consultora de moda brasileira…”). Partição 90%/10% (treino/teste); limite de 1024 tokens por amostra. Ajuste do Qwen/Qwen2.5-0.5B via LoRA (r=8, α=16, *dropout* 0,05) nas projeções de atenção {q\_proj, k\_proj, v\_proj, o\_proj}, por 1 época (Colab/GPU quando disponível). Para a inspeção semântica, geraram-se embeddings de 896 dimensões e aplicou-se *clustering*.

---

## 4.2. Classificação de intenções: desempenho global

 Observou-se superioridade consistente do SVM frente ao Random Forest em todas as métricas no conjunto de teste.

**Tabela 02 – Desempenho global dos modelos de classificação de intenções**

| Métrica                 | Random Forest | SVM   | Diferença    |
| ----------------------- | ------------- | ----- | ------------ |
| **Acurácia**            | 67,4%         | 70,8% | **+3,4 pp**  |
| **Acurácia Balanceada** | 58,3%         | 69,8% | **+11,5 pp** |
| **Kappa**               | 0,636         | 0,680 | +0,044       |
| **F1-Score Macro**      | 0,579         | 0,681 | +0,102       |
| **F1-Score Weighted**   | 0,662         | 0,709 | +0,047       |

Validação Cruzada (Accuracy ± DP): RF = 66,7% ± 1,9% · SVM = 67,0% ± 2,0%  
*Fonte: resultados do grupo (2025).*

 O ganho de 11,5 pp em acurácia balanceada no SVM indica maior capacidade de lidar com o desbalanceamento do corpus; as médias e desvios-padrão são consistentes com o teste, sugerindo estimativas estáveis.

---

## 4.3. Classificação de intenções: desempenho por classe

 A performance por classe acompanha o tamanho das categorias e a proximidade semântica entre intenções.

- **Críticas (F1 < 0,30):**
  - Random Forest: *evento\_presencial* = 0,00; *interesse\_produto* = 0,00; *rastreamento\_pedido* = 0,33.
  - SVM: *evento\_presencial* = 0,29; *interesse\_produto* = 0,29.
- **Boas (F1 > 0,80) em ambos os modelos:**
  *agradecimento* (RF 0,83; SVM 0,88), *reacao\_emocional* (RF 0,84; SVM 0,84), *saudacao* (RF 0,90; SVM 0,98).

 No agregado, 6/16 classes (37,5%) permanecem críticas (F1 < 0,60), majoritariamente minoritárias.

---

## 4.4. Classificação de intenções: confiabilidade das predições

 As distribuições de “confiança” apontam assertividade superior do SVM:

- **Random Forest:** confiança média ≈ 0,275 (ex.: “Onde está meu pedido?” = 14,5%; “Tem esse produto no tamanho P?” = 29,0%).
- **SVM:** confiança média ≈ 0,857, com maior concentração nas classes corretas.

 • Pipeline funcional com *embeddings* BERT (768d) e classificadores tradicionais;
 • SVM apresentou melhor desempenho absoluto e equilíbrio entre classes (↑ acurácia balanceada e F1 macro);
 • Automação viável nas intenções de cortesia/acolhimento (saudacao, agradecimento, reacao_emocional);
 • Limitações objetivas concentradas em classes minoritárias e mensagens ambíguas/ruidosas

 Os achados sustentam o uso de limiares operacionais (*confidence thresholds*) para encaminhamento humano em casos ambíguos.

---

## 4.5. Classificação de intenções: padrões de erro

 Erros concentram-se em pares semanticamente próximos, refletindo sobreposição lexical/pragmática:

- *duvida\_produto* ↔ *problema\_tecnico*
- *interesse\_produto* ↔ *duvida\_produto*
- *mensagem\_sistema* ↔ *troca\_devolucao*

 As confusões são exacerbadas por exemplos vagos/curtíssimos (mensagens de 1 caractere) e pelo alto volume de *nao\_identificado*.

---

## 4.6. Geração de respostas: qualidade semântica do corpus e cobertura

 A análise de *clustering* sobre embeddings (896d) indicou k=10 como número ótimo, com Silhouette = 1,000 e Calinski–Harabasz ≈ 1,967×10¹⁴, evidenciando separação muito elevada entre grupos — coerente com redundância textual.

**Tabela 03 – Distribuição dos clusters (K-Means, k=10)**

| Cluster | Tópico representativo (exemplo)                  |   n |   %   |
| ------: | ------------------------------------------------ | --: | :---: |
|       0 | Proporções/pantalona para baixas                 | 113 | 11,3% |
|       1 | Tênis em looks elegantes                         | 115 | 11,5% |
|       2 | Versatilidade da bolsa bucket                    |  98 |  9,8% |
|       3 | Marcas de regatas básicas                        | 100 | 10,0% |
|       4 | Botas para looks de inverno                      |  89 |  8,9% |
|       5 | Como usar minissaia com elegância                | 121 | 12,1% |
|       6 | Altura/ajuste de bolsa tiracolo                  |  85 |  8,5% |
|       7 | Cores de bolsa p/ roupas escuras (além do preto) |  92 |  9,2% |
|       8 | Acessórios que elevam elegância                  |  91 |  9,1% |
|       9 | Como escolher regata básica de qualidade         |  96 |  9,6% |

*Fonte: resultados do grupo (2025).*  

 Amostragem intraclasse revelou exemplos quase idênticos aos centróides (similaridade≈1,0) e 50.173 pares de paráfrases, sugerindo boa cobertura de intenções frequentes, porém redundância elevada, o que facilita separabilidade e reduz a pressão por generalização no treino.

---

## 4.7. Geração de respostas: comparativo qualitativo (Qwen base vs. Qwen ajustado)

 Em três prompts representativos, avaliou-se clareza, utilidade, vocabulário de moda e consistência.

**Tabela 04 – Comparativo qualitativo (excertos resumidos)**

| Pergunta                                                     | Qwen base (antes)                                             | Qwen FT (depois)                                                           | Observação                     |
| ------------------------------------------------------------ | ------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------ |
| “Quais marcas oferecem boas regatas básicas?”                | Saída redundante com **loop**; ausência de marcas.            | Lista **marcas específicas** (“Rye T-shirt, Tatá, My Basic…”).             | ↑ Especificidade; ↓ alucinação |
| “Como combinar tênis em looks elegantes?”                    | **Genérico**, reexpõe a pergunta.                             | **Dicas acionáveis** (design limpo, solado fino, pantalonas/saia/vestido). | ↑ Utilidade                    |
| “Que cor de bolsa combina com roupas escuras além do preto?” | **Contradição** (responde “preto” como alternativa ao preto). | **Marinho** como alternativa coerente (contraste sutil).                   | ↑ Coerência                    |

*Fonte: resultados do grupo (2025).*  

 Em todas as instâncias, o modelo ajustado produziu respostas curtas, direcionadas e alinhadas ao tom, com redução de alucinação e de repetição.

---

## 4.8. Geração de respostas: evidências de robustez e limitações

- **Generalização com baixo orçamento**: mesmo com 1 época e LoRA parcial, observou-se ganho qualitativo consistente.
- **Cobertura temática**: os 10 clusters capturam os tópicos dominantes do atendimento (pantalona, tênis elegante, bucket, regatas etc.).
- **Ameaças à validade**:
  1. **Redundância** (Silhouette=1,0) pode inflar separabilidade;
  2. **Factualidade temporal** (marcas/coleções variam) demanda checagem contínua;
  3. **Vazamento de tokens de template** em raras saídas (mitigável com *stop sequences*).
- **Cobertura de paráfrases (estimativa interna)**: compreensão de ≥70% das variações não vistas (indicador qualitativo, não *benchmark* padronizado).

---

## 4.9. Síntese e implicações

- Classificação de intenções fornece roteamento confiável (SVM superior), viabilizando automação em intenções de cortesia/acolhimento e apoio a *triage* operacional com limiares de confiança.
- Geração com modelo especializado adiciona capacidade consultiva: respostas específicas de domínio, justificadas e coerentes, favorecendo micro-decisões de estilo do usuário final.
- Arquitetura prática: empregar classificação para roteamento e LLM ajustado para resposta nas intenções estilísticas; manter *fallback* humano condicionado por limiar/ausência de evidência factual.

---

## 4.10. Sumário factual dos achados

- Pipeline de classificação com embeddings BERT (768d): SVM supera RF (↑ acurácia balanceada, ↑ F1 macro); erros concentram-se em classes minoritárias e intenções próximas; *thresholds* sustentam encaminhamento humano.
- Pipeline de geração com Qwen 0,5B + LoRA: melhora clara de clareza, utilidade e coerência; análise semântica indica 10 clusters dominantes (Silhouette=1,0) e alto volume de paráfrases; limitações residuais incluem redundância do corpus e artefatos de decodificação.
- Conclusão operacional: a combinação classificação + geração especializada é viável e já apresenta ganhos práticos; próximos passos incluem deduplicação e diversificação do corpus, métricas automáticas para geração (EM/F1/ROUGE/BERTScore e *faithfulness* quando houver RAG) e guardrails de inferência (sequências de parada, penalidades de repetição e verificação factual leve).

# 5. Análise e Discussão

## 5.1. Contextualização com o estado da arte

&emsp;Os resultados obtidos neste trabalho devem ser contextualizados frente aos *benchmarks* de classificação de intenções e sistemas conversacionais. O *dataset* CLINC150, amplamente utilizado como referência na área, compreende 23.700 consultas distribuídas em 150 intenções across 10 domínios gerais, onde modelos BERT demonstraram acurácia *in-scope* de 96% ou superior. Em contraste, nosso sistema alcançou 67.4% (Random Forest) e 70.8% (SVM) de acurácia geral, evidenciando o impacto das limitações específicas do domínio e *dataset*.

&emsp;Estudos em domínios especializados apresentam resultados mais próximos aos nossos achados. Implementações com SlovakBERT *fine-tuned* para *chatbots* bancários reportam acurácia de 77,2% ± 0,012, enquanto GPT-3.5-turbo fine-tuned alcançou aproximadamente 80% de acurácia no mesmo domínio. Nosso resultado de 70.8% com SVM posiciona-se dentro da faixa competitiva para aplicações de domínio específico, especialmente considerando as limitações do *dataset* de treinamento

&emsp;Os achados devem ser lidos sob dois eixos: classificação de intenções (multiclasse) e geração especializada via *fine-tuning* de LLM. Na literatura, corpora amplos e balanceados como o CLINC150 reportam acurácia in-scope próxima a 96% com variantes BERT, patamar dificilmente replicável em domínios estreitos, com dados assimétricos e ruído. Nesses cenários, resultados entre 70–80% são comuns e compatíveis com aplicações reais quando combinados a encaminhamento humano por limiar de confiança e desenho de fluxos híbridos. No eixo de geração, abordagens PEFT/LoRA (adaptação de poucos parâmetros) têm mostrado ganhos qualitativos relevantes com baixo custo, sobretudo quando há consistência de template e pares (instrução, resposta) curados [[7]](#ref-7). Em moda, desafios como ambiguidade semântica, dinâmica temporal (tendências/coleções) e preferências subjetivas ajudam a explicar o *gap* em relação aos *benchmarks* abertos — e reforçam a pertinência de um arranjo classificador + gerador especializado.

## 5.2. Comparação e leitura dos resultados de classificação

 A vantagem do SVM sobre o Random Forest (↑ Acurácia Balanceada em +11,5 pp; ↑ F1-Macro em +0,102) decorre de dois fatores: (i) melhor aproveitamento da geometria dos embeddings BERT (768d) após normalização (p.ex., *StandardScaler*), e (ii) maior robustez a desbalanceamento, reduzindo vieses para classes majoritárias. A leitura por classe confirma a hipótese de dependência do volume e de proximidade semântica: intenções frequentes (p.ex., *saudacao*, *agradecimento*) apresentam F1 elevados em ambos os modelos, enquanto pares próximos (*interesse\_produto* ↔ *duvida\_produto*; *duvida\_produto* ↔ *problema\_tecnico*) concentram erros. O perfil de confiança também é distinto: SVM mostra médias mais altas e concentradas nas predições corretas, habilitando limiares operacionais para *fallback* humano em casos ambíguos.

## 5.3. Análise dos *embeddings* BERT e representação semântica

&emsp;A utilização do modelo `neuralmind/bert-base-portuguese-cased` para geração de *embeddings* demonstrou adequação técnica, produzindo vetores de 768 dimensões para o corpus de 1.439 mensagens. A execução em GPU T4 no ambiente Google Colab permitiu processamento eficiente, com tempo médio de ~100ms por mensagem durante a fase de inferência.

&emsp;A análise dos *embeddings* revela características semânticas apropriadas para o domínio. Mensagens semanticamente próximas como "Bom dia, como posso ser ajudado?" e "Boa tarde!" demonstram proximidade no espaço vetorial, sendo adequadamente classificadas como saudacao com alta confiança. Contudo, a separabilidade entre classes semanticamente próximas permanece desafiadora, explicando confusões frequentes entre duvida_produto ↔ problema_tecnico e interesse_produto ↔ duvida_produto.

&emsp;A análise de confiança das predições revela diferenças substanciais entre os modelos. O Random Forest apresenta baixa confiança média (0.275), com exemplos como "Onde está meu pedido?" obtendo apenas 14.5% de confiança. Em contraste, o SVM demonstra confiança média superior (0.857), indicando predições mais assertivas e alinhamento superior com os padrões dos *embeddings* BERT.

## 5.4. Implicações para o domínio de e-commerce de moda

&emsp;Os resultados obtidos apresentam implicações diretas para a implementação prática no contexto do Curadobia. A acurácia de 70.8% do melhor modelo (SVM) representa um desempenho adequado para um Mínimo Produto Viável (MVP), especialmente considerando a estratégia de encaminhamento para atendimento humano em casos de baixa confiança.

&emsp;A distribuição das categorias revela alinhamento com as necessidades operacionais identificadas. As três categorias com melhor performance (agradecimento, saudacao, reacao_emocional) correspondem a 37% do volume total (455/1.439 mensagens), permitindo automação efetiva de interações de cortesia e reconhecimento emocional. Esta capacidade é particularmente relevante para manter o "tom próximo, empático e humanizado que caracteriza a consultoria de moda tradicional" conforme especificado nos objetivos do projeto.

&emsp;Contudo, as limitações identificadas em categorias críticas como duvida_produto (F1 = 0.47 no SVM) e rastreamento_pedido (F1 = 0.63 no SVM) indicam necessidade de aprimoramento antes da implementação em produção. Estas categorias representam interações de alto valor comercial que exigem maior precisão para manter a experiência de consultoria especializada.

## 5.5. Limitações identificadas e diagnóstico técnico

### 5.5.1. Limitações do *dataset* e qualidade dos dados

&emsp;A análise revela limitações significativas que impactam diretamente a performance do sistema. O desbalanceamento severo constitui o fator limitante principal, com a categoria "nao_identificado" representando 23% do *dataset* (333 exemplos) versus categorias minoritárias como "evento_presencial" com apenas 1.3% (19 exemplos). Esta distribuição evidencia limitações significativas quando comparada com estudos que sugerem que classificadores de texto requerem entre 3.000 e 30.000 exemplos de treinamento para performance otimizada, dependendo do número de classes e complexidade do domínio [[6]](#ref-6).

&emsp;A qualidade dos dados apresenta desafios adicionais evidenciados pela prevalência da categoria "não_identificado" e pela presença de mensagens de 1 caractere no *dataset*. Exemplos vagos como "qual foi a mensagem?" e "na verdade foi o porteiro, rs!" indicam inconsistências na taxonomia manual que comprometem o aprendizado supervisionado.

### 5.5.2. Desafios específicos do domínio brasileiro de moda

&emsp;O contexto brasileiro introduz complexidades linguísticas específicas não adequadamente capturadas pelo *dataset* atual. A necessidade de "tratar aspectos por atributo (tamanho, tecido, caimento), linguagem coloquial de moda e dinâmica temporal (tendências/estações)" conforme identificado por Gajula [[3]](#ref-3) não é adequadamente representada na taxonomia atual de 16 categorias.

&emsp;Adicionalmente, "variações culturais/linguísticas que afetam a acurácia de análises de sentimento" documentadas por Ismail et al. [[4]](#ref-4) são particularmente relevantes no contexto brasileiro, onde regionalismos e expressões idiomáticas podem interferir na classificação precisa de intenções. A ausência de tratamento específico para gírias de moda e sarcasmo limita a aplicabilidade em conversas naturais de consultoria de moda.

## 5.6. Execução técnica e reprodutibilidade

&emsp;A implementação técnica no Google Colab demonstrou adequação para prototipagem e experimentação, aproveitando recursos de GPU T4 para aceleração do processamento de *embeddings* BERT. O pipeline desenvolvido seguiu práticas de reprodutibilidade com *seeds* fixos (random_state=42) e versionamento explícito do modelo base (`neuralmind/bert-base-portuguese-cased`).

&emsp;Contudo, a migração para produção exigirá adaptações significativas, incluindo remoção de dependências do Colab, otimização de performance para atendimento em tempo real, implementação de *logging* estruturado e métricas operacionais (AHT, CSAT, FCR) conforme demonstrado em estudos sobre métricas operacionais de *chatbots* [2] para avaliação holística de *chatbots*.

## 5.7. Recomendação de modelo e estratégia de implementação

&emsp;Com base na análise quantitativa e qualitativa realizada, recomenda-se a adoção do SVM como algoritmo de classificação principal para o contexto da Curadobia, fundamentada nos seguintes critérios objetivos:

1. **Performance superior**: Acurácia balanceada 11.5% maior (69.8% vs 58.3%) indica melhor capacidade de lidar com desbalanceamento, crucial para o *dataset* atual.

2. **Confiança nas predições**: Confiança média de 0.857 versus 0.275 do Random Forest permite implementação de limiares efetivos para encaminhamento humano.

3. **Adequação aos *embeddings* BERT**: A normalização via StandardScaler otimiza os vetores de 768 dimensões, aproveitando melhor a representação semântica.

&emsp;A estratégia de implementação deve priorizar categorias com performance adequada (F1 > 0.60) para automação inicial, mantendo encaminhamento humano para categorias críticas. Esta abordagem híbrida permite captura de valor imediato enquanto preserva a qualidade consultiva da marca.

## 5.8. Direções futuras e roadmap de melhorias

### 5.8.1. Expansão e refinamento do *dataset*

&emsp;A primeira prioridade constitui expansão significativa do *dataset*, targeting mínimo de 5.000 exemplos bem distribuídos por categoria. Estratégias de data augmentation específicas para o domínio de moda devem ser implementadas, incluindo geração sintética de variações linguísticas e paráfrases contextuais. Esta abordagem pode aumentar a acurácia em até 16% conforme evidenciado em estudos similares.

### 5.8.2. Integração com análise de sentimentos por aspecto

&emsp;Implementação de capacidades de análise de sentimentos por aspecto permitirá personalização mais refinada das recomendações. Esta funcionalidade deve considerar aspectos específicos do domínio (caimento, tecido, cor, ocasião de uso) e estados emocionais do cliente, alinhando-se com evidências de que "integração de sentimentos melhora precisão/explicabilidade" conforme documentado por Gajula [[3]](#ref-3).

### 5.8.3. Fine-tuning do modelo BERT para o domínio

&emsp;O desenvolvimento futuro deve explorar *fine-tuning* específico do modelo BERT português no corpus de moda e atendimento do Curadobia. Esta abordagem, inspirada em sucessos documentados com modelos especializados, pode resultar em melhorias substanciais de performance, potencialmente alcançando os *benchmarks* de 96%+ observados em domínios otimizados.

### 5.8.4. Implementação de métricas híbridas e monitoramento contínuo

&emsp;Estabelecimento de sistema de métricas que combine indicadores técnicos (acurácia, F1-score) com métricas de experiência do usuário (satisfação, taxa de conversão, tempo de resolução). Esta abordagem holística, alinhada com as "métricas operacionais de suporte como AHT, CSAT e FCR", permitirá otimização contínua baseada em impacto real nos resultados de negócio.

# 6. Conclusão

&emsp;...

# Referências

<a id="ref-1"></a>
[1] LANDIM, A. R. D. B. et al. Analysing the effectiveness of *chatbots* as recommendation systems in fashion e-commerce: a cross-cultural comparison. **Computers in Human Behavior**, v. 142, 107659, 2024. Disponível em: <https://discovery.researcher.life/article/analysing-the-effectiveness-of-*chatbots*-as-recommendation-systems-in-fashion-e-commerce-a-crosscultural-comparison/8f0aebee9855310fa6db39654f2957a1>. Acesso em: 11 ago. 2025.

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
