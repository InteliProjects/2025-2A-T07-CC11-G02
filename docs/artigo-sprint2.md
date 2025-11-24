<div align="justify">

# Chatbot Consultivo para E-commerce de Moda: Aplicação de PLN em Sistema de Recomendação Personalizada

Ana Luisa Goes Barbosa, Gabriel Coletto Silva, Gabriel Farias, Hugo Noyma, João Paulo Santos, Lucas Nogueira Nunes, Mauro das Chagas Junior, Vitto Mazeto

# Abstract

...

# 1. Introdução

&emsp;O _e-commerce_ de moda tem experimentado transformações aceleradas, especialmente após a pandemia de COVID-19, que forçou a migração de serviços tradicionalmente presenciais para o ambiente digital. Neste cenário, empresas enfrentam o complexo desafio de equilibrar personalização e escalabilidade no atendimento ao cliente, precisando automatizar o suporte sem comprometer a qualidade consultiva. O segmento de moda apresenta particularidades únicas, pois as decisões de compra envolvem aspectos subjetivos como estilo pessoal, ocasião de uso e preferências estéticas que demandam orientação especializada. _Chatbots_ baseados em processamento de linguagem natural (PLN) emergem como solução promissora para conciliar eficiência operacional com experiência personalizada, oferecendo potencial para revolucionar o atendimento no _e-commerce_ de moda (LANDIM et al., 2024) [[1]](#ref-1).

&emsp;O Curadobia, _marketplace_ focado em curadoria especializada de moda, exemplifica perfeitamente essa necessidade emergente do mercado. A empresa, que se posiciona como consultoria de moda integrada ao varejo digital, busca escalar seu atendimento consultivo sem perder o diferencial competitivo fundamental: oferecer orientação personalizada sobre combinações, modelagem, caimento e estilo de vida. Com mais de 20 marcas parceiras e um ano de operação, o Curadobia enfrenta a limitação de manter seu DNA de "peças com história" e experiência de compra guiada conforme cresce. O desafio central é automatizar processos de atendimento mantendo o tom próximo, empático e humanizado que caracteriza a consultoria de moda tradicional, sem recorrer a respostas genéricas ou robóticas que comprometeriam a proposta de valor da marca.

&emsp;Este trabalho propõe o desenvolvimento de um sistema de _chatbot_ inteligente capaz de responder dúvidas frequentes e oferecer recomendações de produtos de forma consultiva e personalizada. O objetivo é criar uma solução baseada em PLN que preserve a identidade conversacional e o expertise em curadoria da marca, enquanto permite escalabilidade operacional através de algoritmos de recomendação contextualizados. A implementação busca integrar _machine learning_ com o conhecimento especializado em moda, possibilitando interações naturais que mantenham o padrão de qualidade do atendimento humano. Espera-se que a solução contribua tanto para a otimização de recursos da empresa quanto para o avanço do conhecimento em sistemas conversacionais aplicados ao varejo especializado.

# 2. Trabalhos Relacionados

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
- Adotar práticas robustas de reprodutibilidade (versionamento de dados, _seeds_, rastreamento de experimentos, contêineres),
- Monitorar métricas de produto e suporte (deflexão, CSAT, AHT, taxa de conversão e repetição de compra);
- Tratar privacidade/consentimento e vieses linguísticos/culturais do domínio de moda.

# 3. Materiais e Métodos

## 3.1. Aquisição e tratamento dos dados

&emsp;Os dados foram obtidos a partir de um arquivo CSV consolidado contendo mensagens de atendimento do Curadobia oriundas de WhatsApp e Instagram. A coluna `message` foi renomeada para `original`. Foram removidos valores nulos e os registros foram reindexados. A taxonomia de _intents_ que orienta o escopo do chatbot está presente no código de taxonomia.

&emsp;Essas decisões asseguram padronização do campo-alvo ao longo do pipeline, evitam a propagação de registros vazios, preservam a rastreabilidade entre etapas e delimitam o escopo de intents que guiará a curadoria do corpus.

## 3.2. Análise exploratória de dados (AED)

&emsp;A AED foi conduzida nos notebooks de exploração e pré-processamento com o objetivo de caracterizar o corpus e apoiar decisões de pré-processamento e modelagem, sem apresentação de resultados nesta seção. As atividades metodológicas incluíram: (i) cálculo do comprimento das mensagens em tokens, com estatísticas descritivas e histogramas, para orientar limites de truncamento e memória de diálogo; (ii) inspeção do vocabulário após normalização (remoção de _stopwords_ e _stemming_) para identificar termos característicos do domínio e apoiar a definição de _intents_/_slots_; (iii) mapeamento das categorias temáticas para verificar cobertura e orientar estratégias de balanceamento; e (iv) organização dos artefatos da AED (tabelas e gráficos) diretamente a partir dos _notebooks_, garantindo reprodutibilidade e rastreabilidade.

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

&emsp;Na etapa final, foram testados dois classificadores: **Support Vector Machine (SVM)** e **Random Forest**. Ambos foram avaliados sobre o mesmo conjunto de dados, permitindo comparação direta de desempenho.

## 3.6. Taxonomia de intenções

&emsp;A taxonomia definida para o chatbot contempla 16 intenções distintas: _dúvida_produto_, _solicitação_informação_, _reação_emocional_, _interesse_produto_, _agradecimento_, _rastreamento_pedido_, _saudação_, _solicitação_contato_, _mensagem_sistema_, _troca_devolução_, _problema_técnico_, _não_identificado_, _reposição_estoque_, _confirmação_, _parceria_comercial_ e _evento_presencial_.

&emsp;O mapeamento _id2label_ é explicitado no arquivo de configuração, garantindo alinhamento entre fases de treino e inferência.

**Quadro 1 – Taxonomia de intenções do chatbot**  

| Identificador | Intenção | Descrição breve |
|---------------|---------------------------|---------------------------------------------------------------------------------|
| 1 | _dúvida_produto_ | Perguntas sobre especificações, tamanhos, variantes ou quantidades de produtos. |
| 2 | _solicitação_informação_ | Requisição de informações gerais, políticas ou detalhes adicionais. |
| 3 | _reação_emocional_ | Mensagens curtas de reação ou emoção (ex.: emojis, expressões afetivas). |
| 4 | _interesse_produto_ | Demonstração de interesse em produtos específicos, tamanhos ou variantes. |
| 5 | _agradecimento_ | Expressões de gratidão pelo atendimento. |
| 6 | _rastreamento_pedido_ | Solicitações de status ou código de rastreio de pedidos. |
| 7 | _saudação_ | Início de conversa com cumprimentos. |
| 8 | _solicitação_contato_ | Pedido para ser contatado via WhatsApp, e-mail ou telefone. |
| 9 | _mensagem_sistema_ | Mensagens automáticas ou de sistema. |
| 10 | _troca_devolução_ | Solicitações para troca ou devolução de pedidos. |
| 11 | _problema_técnico_ | Relato de falhas técnicas ou bugs, possivelmente com capturas de tela. |
| 12 | _não_identificado_ | Mensagens ambíguas ou não classificadas. |
| 13 | _reposição_estoque_ | Perguntas sobre disponibilidade futura de itens ou variantes. |
| 14 | _confirmação_ | Respostas confirmando ações ou informações fornecidas. |
| 15 | _parceria_comercial_ | Propostas de colaboração ou contato com o time comercial. |
| 16 | _evento_presencial_ | Interações sobre participação em eventos presenciais. |

## 3.7. Geração de _embeddings_

&emsp;Os textos são convertidos em vetores densos utilizando o modelo _neuralmind/bert-base-portuguese-cased_, com truncamento em até _128 tokens_ e agregação via _mean pooling_. Não foi realizado _fine-tuning_, sendo utilizado o modelo pré-treinado disponível publicamente.

&emsp;Durante o desenvolvimento, a extração de _embeddings_ e o treinamento dos classificadores foram realizados na GPU T4 disponibilizada pelo ambiente Google Colab, usando aceleração por hardware para reduzir o tempo de processamento.

## 3.8. Roteamento e fluxos conversacionais

&emsp;As predições de intenção passam por um processo de normalização (conversão para minúsculas, remoção de acentos e substituição de espaços por sublinhados) antes de serem mapeadas para os respectivos _handlers_.

&emsp;O diálogo é conduzido por fluxos orientados a estados, nos quais cada intenção pode acionar transições específicas. Por exemplo, uma _dúvida_produto_ pode levar à consulta do catálogo e, em seguida, a um estado de encerramento ou recomendação; já um pedido de _rastreamento_pedido_ pode levar à consulta de status e envio do código de rastreio.

&emsp;O fluxo inclui também um **estado de transição condicional** (_encerrar_ou_recomendar_), que atua como ponto central para concluir ou expandir a interação.

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

# 4. Resultados

&emsp;Esta seção apresenta os resultados obtidos com o sistema de classificação de intenções e a avaliação funcional do chatbot consultivo para o e-commerce de moda do Curadobia. Os experimentos consideraram 16 intenções em um corpus de 1.439 mensagens, vetorizadas com BERT em português (768 dimensões) e avaliadas em cenário multiclasse. Reportamos: (i) desempenho global dos modelos; (ii) desempenho por classe; (iii) evidências de confiabilidade das predições; e (iv) padrões de erro observados.

## 4.1. Escopo da avaliação e corpus

&emsp;O conjunto de dados apresenta distribuição assimétrica entre as classes: a categoria nao_identificado concentra 333 exemplos (23%), enquanto evento_presencial possui 19 exemplos (1,3%). Em termos de infraestrutura, os embeddings foram extraídos com o modelo neuralmind/bert-base-portuguese-cased (truncamento em 128 tokens, mean pooling), e os classificadores foram treinados e avaliados em ambiente Google Colab com GPU T4.

## 4.2. Desempenho global dos modelos

&emsp;A Tabela 02 consolida as métricas principais no conjunto de teste e os resultados de validação cruzada estratificada. Observou-se superioridade consistente do SVM frente ao Random Forest em todas as métricas.

Tabela 02 – Desempenho global dos modelos de classificação de intenções

| Métrica                 | Random Forest |  SVM   | Diferença  |
|-------------------------|---------------|--------|------------|
| **Acurácia**            | 67,4%         | 70,8%  | **+3,4 pp** |
| **Acurácia Balanceada** | 58,3%         | 69,8%  | **+11,5 pp** |
| **Kappa**               | 0,636         | 0,680  | +0,044     |
| **F1-Score Macro**      | 0,579         | 0,681  | +0,102     |
| **F1-Score Weighted**   | 0,662         | 0,709  | +0,047     |

**Validação Cruzada (Accuracy ± DP):** RF = **66,7% ± 1,9%** · SVM = **67,0% ± 2,0%**  
_Fonte: resultados do grupo (2025)._

&emsp;O ganho de 11,5 pontos percentuais em acurácia balanceada no SVM indica maior capacidade de lidar com o desbalanceamento do corpus. As médias e os desvios-padrão da validação cruzada são consistentes com o desempenho de teste, sugerindo estimativas estáveis.

## 4.3. Desempenho por classe

&emsp;A análise por classe evidencia forte dependência do tamanho das categorias e da proximidade semântica entre intenções.
 • Classes com performance crítica (F1 < 0,30):
 • Random Forest: evento_presencial = 0,00; interesse_produto = 0,00; rastreamento_pedido = 0,33.
 • SVM: evento_presencial = 0,29; interesse_produto = 0,29.
 • Classes com boa performance (F1 > 0,80) em ambos os modelos:
agradecimento (RF 0,83; SVM 0,88), reacao_emocional (RF 0,84; SVM 0,84), saudacao (RF 0,90; SVM 0,98).

&emsp;No agregado, 6 das 16 classes (37,5%) permanecem críticas (F1 < 0,60), concentradas nas categorias minoritárias.

## 4.4. Confiabilidade das predições

&emsp;A inspeção dos escores de decisão/“confiança” mostrou distribuições distintas entre os modelos:
 • Random Forest: tendência a baixa confiança média (≈ 0,275), com exemplos como “Onde está meu pedido?” obtendo 14,5% e “Tem esse produto no tamanho P?” 29,0%.
 • SVM: maior assertividade média (≈ 0,857), com concentração de escores nas classes previstas corretas.

&emsp;Esses achados sustentam o uso de limiares operacionais (p.ex., confidence thresholds) para encaminhamento humano nos cenários ambíguos.

## 4.5. Padrões de erro observados

&emsp;Os erros concentram-se em pares de intenções semanticamente próximas, refletindo sobreposição lexical e pragmática no domínio:
 • duvida_produto ↔ problema_tecnico
 • interesse_produto ↔ duvida_produto
 • mensagem_sistema ↔ troca_devolucao

&emsp;As confusões são exacerbadas pela presença de exemplos vagos e curtíssimos (mensagens de 1 caractere) e pelo volume elevado de nao_identificado no corpus.

## 4.6. Sumário factual dos achados

 • Pipeline funcional com embeddings BERT (768d) e classificadores tradicionais;
 • SVM apresentou melhor desempenho absoluto e equilíbrio entre classes (↑ acurácia balanceada e F1 macro);
 • Automação viável nas intenções de cortesia/acolhimento (saudacao, agradecimento, reacao_emocional);
 • Limitações objetivas concentradas em classes minoritárias e mensagens ambíguas/ruidosas.

# 5. Análise e Discussão

## 5.1. Contextualização dos resultados com o estado da arte

&emsp;Os resultados obtidos neste trabalho devem ser contextualizados frente aos benchmarks estabelecidos na literatura de classificação de intenções e sistemas conversacionais. O **dataset CLINC150**, amplamente utilizado como referência na área, compreende 23.700 consultas distribuídas em 150 intenções across 10 domínios gerais, onde modelos BERT demonstraram **acurácia in-scope de 96% ou superior**. Em contraste, nosso sistema alcançou **67.4% (Random Forest) e 70.8% (SVM) de acurácia geral**, evidenciando o impacto das limitações específicas do domínio e dataset.

&emsp;Estudos em domínios especializados apresentam resultados mais próximos aos nossos achados. Implementações com **SlovakBERT fine-tuned para chatbots bancários** reportam acurácia de **77,2% ± 0,012**, enquanto **GPT-3.5-turbo fine-tuned** alcançou aproximadamente **80% de acurácia** no mesmo domínio. Nosso resultado de **70.8% com SVM** posiciona-se dentro da faixa competitiva para aplicações de domínio específico, especialmente considerando as limitações do dataset de treinamento.

&emsp;A literatura especializada em e-commerce de moda destaca desafios únicos que explicam parcialmente nossa performance. Conforme documentado por Gajula [[3]](#ref-3), sistemas de recomendação sensíveis a sentimentos enfrentam dificuldades persistentes com "ruído e ambiguidade (ironia/sarcasmo), alinhamento de sentimentos por aspecto, preferência dinâmica/temporal, início a frio (_cold start_), escalabilidade e justiça algorítmica". Estes fatores são particularmente relevantes no contexto de consultoria de moda, onde aspectos subjetivos como estilo pessoal e ocasião de uso demandam orientação especializada.

## 5.2. Análise comparativa dos resultados dos modelos

&emsp;A comparação sistemática entre Random Forest e SVM revela diferenças significativas em múltiplas dimensões de performance, conforme detalhado na Tabela 02:

<div align="center">
<sub>Tabela 02 – Comparação quantitativa de performance dos modelos</sub>

| Métrica                 | Random Forest | SVM   | Diferença | Interpretação        |
|-------------------------|---------------|-------|-----------|----------------------|
| **Acurácia Geral**      | 67.4%         | 70.8% | +3.4%     | SVM superior         |
| **Acurácia Balanceada** | 58.3%         | 69.8% | +11.5%    | SVM muito superior   |
| **Kappa Score**         | 0.636         | 0.680 | +0.044    | SVM moderadamente melhor |
| **F1-Score Macro**      | 0.579         | 0.681 | +0.102    | SVM substancialmente melhor |
| **F1-Score Weighted**   | 0.662         | 0.709 | +0.047    | SVM moderadamente melhor |
| **CV Accuracy**         | 66.7% ±1.9%   | 67.0% ±2.0% | +0.3% | Equivalência estatística |

<sup>Fonte: Material produzido pelos próprios autores (2025)</sup>
</div>

&emsp;A **acurácia balanceada 11.5% superior do SVM** constitui o achado mais significativo, indicando melhor capacidade de lidar com o desbalanceamento severo do dataset. Esta superioridade alinha-se com observações da literatura de que "SVM funciona melhor em dados esparsos do que árvores em geral, especialmente em classificação de documentos onde milhares de features podem estar presentes" (literatura especializada). A aplicação de **StandardScaler** no SVM otimiza os embeddings BERT (768 dimensões), enquanto o Random Forest opera diretamente nos vetores não-normalizados.

&emsp;A análise por categorias revela padrões consistentes com as limitações identificadas. Classes com **≥100 exemplos** (agradecimento, saudacao, reacao_emocional) demonstram **F1-scores > 0.80 em ambos os modelos**, enquanto classes minoritárias apresentam performance crítica. Especificamente, as categorias **evento_presencial** (19 exemplos) e **interesse_produto** (26 exemplos) obtiveram **F1 = 0.00 no Random Forest** e **F1 ≤ 0.29 no SVM**, evidenciando a insuficiência de dados de treinamento para generalização adequada.

## 5.3. Análise dos embeddings BERT e representação semântica

&emsp;A utilização do modelo `neuralmind/bert-base-portuguese-cased` para geração de embeddings demonstrou adequação técnica, produzindo **vetores de 768 dimensões** para o corpus de 1.439 mensagens. A execução em **GPU T4 no ambiente Google Colab** permitiu processamento eficiente, com **tempo médio de ~100ms por mensagem** durante a fase de inferência.

&emsp;A análise dos embeddings revela características semânticas apropriadas para o domínio. Mensagens semanticamente próximas como "Bom dia, como posso ser ajudado?" e "Boa tarde!" demonstram proximidade no espaço vetorial, sendo adequadamente classificadas como **saudacao** com alta confiança. Contudo, a separabilidade entre classes semanticamente próximas permanece desafiadora, explicando confusões frequentes entre **duvida_produto ↔ problema_tecnico** e **interesse_produto ↔ duvida_produto**.

&emsp;A análise de confiança das predições revela diferenças substanciais entre os modelos. O Random Forest apresenta **baixa confiança média (0.275)**, com exemplos como "Onde está meu pedido?" obtendo apenas **14.5% de confiança**. Em contraste, o SVM demonstra **confiança média superior (0.857)**, indicando predições mais assertivas e alinhamento superior com os padrões dos embeddings BERT.

## 5.4. Implicações para o domínio de e-commerce de moda

&emsp;Os resultados obtidos apresentam implicações diretas para a implementação prática no contexto do Curadobia. A **acurácia de 70.8%** do melhor modelo (SVM) situa-se abaixo dos padrões comerciais típicos (>85%), mas permanece funcional para um **Mínimo Produto Viável (MVP)**, especialmente considerando a estratégia de **encaminhamento para atendimento humano** em casos de baixa confiança.

&emsp;A distribuição das categorias revela alinhamento com as necessidades operacionais identificadas. As **três categorias com melhor performance** (agradecimento, saudacao, reacao_emocional) correspondem a **37% do volume total** (455/1.439 mensagens), permitindo automação efetiva de interações de cortesia e reconhecimento emocional. Esta capacidade é particularmente relevante para manter o "tom próximo, empático e humanizado que caracteriza a consultoria de moda tradicional" conforme especificado nos objetivos do projeto.

&emsp;Contudo, as limitações identificadas em categorias críticas como **duvida_produto** (F1 = 0.47 no SVM) e **rastreamento_pedido** (F1 = 0.63 no SVM) indicam necessidade de aprimoramento antes da implementação em produção. Estas categorias representam interações de alto valor comercial que exigem maior precisão para manter a experiência de consultoria especializada.

## 5.5. Limitações identificadas e diagnóstico técnico

### 5.5.1. Limitações do dataset e qualidade dos dados

&emsp;A análise revela limitações significativas que impactam diretamente a performance do sistema. O **desbalanceamento severo** constitui o fator limitante principal, com a categoria "nao_identificado" representando **23% do dataset** (333 exemplos) versus categorias minoritárias como "evento_presencial" com apenas **1.3%** (19 exemplos). Esta distribuição contrasta com recomendações da literatura de que "sistemas simples precisem de 5.000 exemplos rotulados, enquanto sistemas complexos podem necessitar até 50.000 para performance otimizada".

&emsp;A **qualidade dos dados** apresenta desafios adicionais evidenciados pela prevalência da categoria "não_identificado" e pela presença de **mensagens de 1 caractere** no dataset. Exemplos vagos como "qual foi a mensagem?" e "na verdade foi o porteiro, rs!" indicam inconsistências na taxonomia manual que comprometem o aprendizado supervisionado. Esta observação alinha-se com alertas da literatura sobre chatbots que "frequentemente recebem perguntas para as quais não estão preparados, podendo causar experiências frustrantes para usuários".

### 5.5.2. Desafios específicos do domínio brasileiro de moda

&emsp;O contexto brasileiro introduz complexidades linguísticas específicas não adequadamente capturadas pelo dataset atual. A necessidade de "tratar aspectos por atributo (tamanho, tecido, caimento), linguagem coloquial de moda e dinâmica temporal (tendências/estações)" conforme identificado por Gajula [[3]](#ref-3) não é adequadamente representada na taxonomia atual de 16 categorias.

&emsp;Adicionalmente, "variações culturais/linguísticas que afetam a acurácia de análises de sentimento" documentadas por Ismail et al. [[4]](#ref-4) são particularmente relevantes no contexto brasileiro, onde regionalismos e expressões idiomáticas podem interferir na classificação precisa de intenções. A ausência de tratamento específico para gírias de moda e sarcasmo - desafios persistentes identificados na literatura - limita a aplicabilidade em conversas naturais de consultoria de moda.

## 5.6. Execução técnica e reprodutibilidade

&emsp;A implementação técnica no **Google Colab** demonstrou adequação para prototipagem e experimentação, aproveitando recursos de **GPU T4** para aceleração do processamento de embeddings BERT. O pipeline desenvolvido seguiu práticas de reprodutibilidade com **seeds fixos** (random_state=42) e versionamento explícito do modelo base (`neuralmind/bert-base-portuguese-cased`).

&emsp;Contudo, a **migração para produção** exigirá adaptações significativas, incluindo remoção de dependências do Colab, otimização de performance para atendimento em tempo real, implementação de logging estruturado e métricas operacionais (AHT, CSAT, FCR) conforme identificado na literatura como essenciais para avaliação holística de chatbots.

## 5.7. Recomendação de modelo e estratégia de implementação

&emsp;Com base na análise quantitativa e qualitativa realizada, **recomenda-se a adoção do SVM** como algoritmo de classificação principal para o contexto da Curadobia, fundamentada nos seguintes critérios objetivos:

1. **Performance superior**: Acurácia balanceada 11.5% maior (69.8% vs 58.3%) indica melhor capacidade de lidar com desbalanceamento, crucial para o dataset atual.

2. **Confiança nas predições**: Confiança média de 0.857 versus 0.275 do Random Forest permite implementação de limiares efetivos para encaminhamento humano.

3. **Adequação aos embeddings BERT**: A normalização via StandardScaler otimiza os vetores de 768 dimensões, aproveitando melhor a representação semântica.

&emsp;A **estratégia de implementação** deve priorizar categorias com performance adequada (F1 > 0.60) para automação inicial, mantendo encaminhamento humano para categorias críticas. Esta abordagem híbrida permite captura de valor imediato enquanto preserva a qualidade consultiva da marca.

## 5.8. Direções futuras e roadmap de melhorias

### 5.8.1. Expansão e refinamento do dataset

&emsp;A primeira prioridade constitui expansão significativa do dataset, targeting **mínimo de 5.000 exemplos** bem distribuídos por categoria conforme recomendações da literatura. Estratégias de **data augmentation** específicas para o domínio de moda devem ser implementadas, incluindo geração sintética de variações linguísticas e paráfrases contextuais. Esta abordagem pode aumentar a acurácia em até 16% conforme evidenciado em estudos similares.

### 5.8.2. Integração com análise de sentimentos por aspecto

&emsp;Implementação de capacidades de **análise de sentimentos por aspecto** permitirá personalização mais refinada das recomendações. Esta funcionalidade deve considerar aspectos específicos do domínio (caimento, tecido, cor, ocasião de uso) e estados emocionais do cliente, alinhando-se com evidências de que "integração de sentimentos melhora precisão/explicabilidade" conforme documentado por Gajula [[3]](#ref-3).

### 5.8.3. Fine-tuning do modelo BERT para o domínio

&emsp;O desenvolvimento futuro deve explorar **fine-tuning específico** do modelo BERT português no corpus de moda e atendimento do Curadobia. Esta abordagem, inspirada em sucessos documentados com modelos especializados, pode resultar em melhorias substanciais de performance, potencialmente alcançando os benchmarks de 96%+ observados em domínios otimizados.

### 5.8.4. Implementação de métricas híbridas e monitoramento contínuo

&emsp;Estabelecimento de sistema de métricas que combine **indicadores técnicos** (acurácia, F1-score) com **métricas de experiência do usuário** (satisfação, taxa de conversão, tempo de resolução). Esta abordagem holística, alinhada com recomendações da literatura sobre a importância de "métricas operacionais de suporte como AHT, CSAT e FCR", permitirá otimização contínua baseada em impacto real nos resultados de negócio.

&emsp;...

# 6. Conclusão

&emsp;...

# Referências

<a id="ref-1"></a>
[1] LANDIM, A. R. D. B. et al. Analysing the effectiveness of chatbots as recommendation systems in fashion e-commerce: a cross-cultural comparison. **Computers in Human Behavior**, v. 142, 107659, 2024.

<a id="ref-2"></a>
[2] HUI, Kuek Shu. The Role of Natural Language Processing in Improving Customer Service and Support in E-Commerce. 15 dez. 2023. Disponível em: <http://eprints.utar.edu.my/6295/1/202306-51_Kuek_Shu_Hui_KUEK_SHU_HUI.pdf>. Acesso em: 11 ago. 2025.

<a id="ref-3"></a>
[3] GAJULA, Yogesh. Sentiment-Aware Recommendation Systems in E-Commerce: A Review from a Natural Language Processing Perspective. 3 maio 2025. Disponível em: <https://arxiv.org/abs/2505.03828>. Acesso em: 11 ago. 2025.

<a id="ref-4"></a>
[4] ISMAIL, Walaa Saber; GHAREEB, Marwa M.; YOUSSRY, Howida. Enhancing Customer Experience through Sentiment Analysis and Natural Language Processing in E-commerce. 30 set. 2024. Disponível em: <https://jowua.com/wp-content/uploads/2024/10/2024.I3.005.pdf>. Acesso em: 11 ago. 2025.

<a id="ref-5"></a>
[5] FASTAPI. FastAPI framework, high performance, easy to learn, fast to code, ready for production. Disponível em: <https://fastapi.tiangolo.com/>. Acesso em: 28 ago. 2025.

</div>
