<div align="justify">

# Chatbot Consultivo para E-commerce de Moda: Aplicação de PLN e IA Generativa em Sistema de Recomendação Personalizada

Ana Luisa Goes Barbosa, Gabriel Coletto Silva, Gabriel Farias, Hugo Noyma, João Paulo Santos, Lucas Nogueira Nunes, Mauro das Chagas Junior, Vitto Mazeto

# Abstract

...

# 1. Introdução

&emsp;O *e-commerce* de moda tem experimentado transformações aceleradas, especialmente após a pandemia de COVID-19, que forçou a migração de serviços tradicionalmente presenciais para o ambiente digital. Neste cenário, empresas enfrentam o complexo desafio de equilibrar personalização e escalabilidade no atendimento ao cliente, precisando automatizar o suporte sem comprometer a qualidade consultiva. O segmento de moda apresenta particularidades únicas, pois as decisões de compra envolvem aspectos subjetivos como estilo pessoal, ocasião de uso e preferências estéticas que demandam orientação especializada. *Chatbots* baseados em Processamento de Linguagem Natural (PLN) e técnicas de Inteligência Artificial Generativa emergem como solução promissora para conciliar eficiência operacional com experiência personalizada, oferecendo potencial para revolucionar o atendimento no *e-commerce* de moda (LANDIM et al., 2024) [[1]](#ref-1).

&emsp;O Curadobia, *marketplace* focado em curadoria especializada de moda, exemplifica perfeitamente essa necessidade emergente do mercado. A empresa, que se posiciona como consultoria de moda integrada ao varejo digital, busca escalar seu atendimento consultivo sem perder o diferencial competitivo fundamental: oferecer orientação personalizada sobre combinações, modelagem, caimento e estilo de vida. Com mais de 20 marcas parceiras e um ano de operação, o Curadobia enfrenta a limitação de manter seu DNA de "peças com história" e experiência de compra guiada conforme cresce. O desafio central é automatizar processos de atendimento mantendo o tom próximo, empático e humanizado que caracteriza a consultoria de moda tradicional, sem recorrer a respostas genéricas ou robóticas que comprometeriam a proposta de valor da marca.

&emsp;Este trabalho propõe o desenvolvimento de um sistema de *chatbot* inteligente capaz de responder dúvidas frequentes e oferecer recomendações de produtos de forma consultiva e personalizada. O objetivo é criar uma solução baseada em PLN e IA generativa que preserve a identidade conversacional e o expertise em curadoria da marca, enquanto permite escalabilidade operacional através de algoritmos de recomendação contextualizados. A implementação busca integrar *machine learning* com o conhecimento especializado em moda, possibilitando interações naturais que mantenham o padrão de qualidade do atendimento humano. Espera-se que a solução contribua tanto para a otimização de recursos da empresa quanto para o avanço do conhecimento em sistemas conversacionais aplicados ao varejo especializado.

# 2. Trabalhos Relacionados

&emsp;A revisão de literatura foi conduzida entre julho e agosto de 2025, utilizando como base o **Google Scholar**. As consultas foram realizadas com combinações de termos em inglês e português, tais como: *“fashion e-commerce chatbot recommendation system”*, *“sentiment analysis personalized recommendation”*, *“generative AI conversational agent retail”* e *“chatbot consultivo moda”*, entre outras variações. Foi priorizado artigos publicados entre 2024 e 2025, de modo a refletir o estado da arte sobre PLN e IA generativa aplicados ao atendimento digital em varejo.

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

| Trabalho | Escopo/Tipo | Metodologia/Dados | Principais resultados | Métricas/Relatos | Pontos positivos | Limitações |
| --- | --- | --- | --- | --- | --- | --- |
| [[2]](#ref-2) Hui – The Role of NLP… | Modelo de aceitação e experiência em atendimento com PLN (quantitativo) | Hipóteses H1–H6; testes de confiabilidade e significância | Facilidade de uso, influência social e aprendizagem por observação → experiência; experiência → satisfação; utilidade e autoeficácia não significativas | Alfas de confiabilidade elevados; efeitos significativos reportados | Implicações gerenciais claras (priorizar usabilidade e prova social) | Pouca métrica operacional (AHT, FCR); foco perceptual; generalização para domínios específicos |
| [[3]](#ref-3) Gajula – Sentiment-aware Recommendation Systems… | Revisão (2023–2025) de recomendação com sentimentos | Síntese de estado da arte: transformadores, grafos, LLMs; boas práticas de reprodutibilidade | Integração de sentimentos melhora precisão/explicabilidade; desafios: sarcasmo, aspectos, tempo, *cold start*, escalabilidade, *fairness*/privacidade | Ênfase em padrões de *benchmarks*, *seeds*, protocolos e métricas além de acurácia | Direciona práticas transparentes e comparáveis; visão ampla do estado da arte | Falta de evidências de testes A/B em produção; foco menor em suporte conversacional |
| [[4]](#ref-4) Ismail et al. – Enhancing Customer Experience… | Estudo empírico de impacto de PLN/sentimentos | Descritivo + regressão; variáveis de lealdade, vendas, satisfação, privacidade | r≈0,78 (sentimento↔lealdade); +5,28% vendas por incremento de personalização; ROI≈400%; 85% satisfeitos com privacidade | Estatísticas descritivas; t-values/p-values reportados | Quantifica impacto de negócio e aborda ética/privacidade | Generalização e suposições de ROI; necessidade de mais detalhes metodológicos |

<sup>Fonte: Material produzido pelos próprios autores (2025)</sup>
</div>

## 2.4. Implicações para o projeto

&emsp;Haja vista a análise supracitada, é possível determinar importantes ações e diretrizes que podem ser aplicadas a este projeto. Dentre elas, destacam-se:  

- Priorizar a Experiência do Usuário (UX) do *chatbot* (clareza, tempo de resposta, linguagem da marca);  
- Alavancar evidência social (avaliações/fotos de clientes) no diálogo;  
- Usar análise de sentimentos para personalizar recomendações e explicações por aspecto (ex.: caimento, tecido, tamanho);  
- Adotar práticas robustas de reprodutibilidade (versionamento de dados, *seeds*, rastreamento de experimentos, contêineres);  
- Monitorar métricas de produto e suporte (deflexão, **Satisfação do Cliente (CSAT)**, **Tempo Médio de Atendimento (AHT)**, taxa de conversão e repetição de compra);  
- Tratar privacidade/consentimento e vieses linguísticos/culturais do domínio de moda;  
- Considerar implicações do uso de IA generativa, como controle de alucinações, calibragem de respostas consultivas e alinhamento com a identidade da marca, garantindo transparência e confiabilidade no atendimento.  

</div>

# 3. Materiais e Métodos

### 3.1. Aquisição e tratamento dos dados

&emsp;Os dados foram obtidos a partir de um arquivo CSV consolidado contendo mensagens de atendimento do Curadobia oriundas de WhatsApp e Instagram. A coluna `message` foi renomeada para `original`. Foram removidos valores nulos e os registros foram reindexados. Além do texto das mensagens, o conjunto incluía campos auxiliares como identificador da interação, data/hora, canal de origem e categoria inicial, que foram mantidos para apoiar etapas posteriores de análise e rastreabilidade. A taxonomia de *intents* que orienta o escopo do *chatbot* está presente no código de taxonomia e foi utilizada como referência para delimitar as categorias conversacionais.  

&emsp;Essas decisões asseguram padronização do campo-alvo ao longo do *pipeline*, evitam a propagação de registros vazios, preservam a rastreabilidade entre etapas e delimitam o escopo de *intents* que guiará a curadoria do corpus.

### 3.2. Análise exploratória de dados (AED)

&emsp;A AED foi conduzida nos notebooks de exploração e de pré-processamento com o objetivo de caracterizar o corpus e apoiar decisões de pré-processamento e modelagem, sem apresentação de resultados nesta seção. As atividades metodológicas incluíram: (i) cálculo do comprimento das mensagens em tokens, com estatísticas descritivas e histogramas, para orientar limites de truncamento e memória de diálogo; (ii) inspeção do vocabulário após normalização (remoção de *stopwords* e *stemming*) para identificar termos característicos do domínio e apoiar a definição de *intents*/*slots*; (iii) mapeamento das categorias temáticas para verificar cobertura e orientar estratégias de balanceamento; e (iv) organização dos artefatos da AED (tabelas e gráficos) diretamente a partir dos notebooks, garantindo reprodutibilidade e rastreabilidade.

### 3.3. Pré-processamento textual

&emsp;Foi implementado um *pipeline* leve e reprodutível no notebook de pré-processamento, composto pelas etapas:  

- **lower**: conversão para minúsculas — normaliza a capitalização e reduz a sparsidade lexical;  
- **strip_accents**: normalização Unicode e remoção de acentos — unifica variantes ortográficas (p.ex., “ação”/“acao”);  
- **remove_punctuation**: remoção de pontuação e símbolos — reduz ruído não lexical em representações baseadas em termos;  
- **tokenize**: tokenização simples por espaço — viabiliza filtragem e transformações subsequentes por termo;  
- **remove_stopwords**: remoção de *stopwords* em português — atenua termos de alta frequência com baixo poder discriminativo;  
- **stem**: redução lexical com RSLPStemmer — agrupa flexões e variações morfológicas, favorecendo a generalização inicial.  

&emsp;O *pipeline* é composto por funções puras e orquestrado por uma rotina de execução que produz um conjunto de colunas por etapa (de `original` até `stems`), mantendo rastreabilidade das transformações. A Figura 1 ilustra o fluxo aplicado.  

<div align="center">

<sub>Figura 01: Fluxo Pipeline de Pré-processamento</sub>

![Fluxo do pipeline de pré-processamento](imagens/figura-pipeline-pre-processamento.png)

<sup>Fonte: Material produzido pelos próprios autores por meio do Mermaid (2025).</sup>

</div>

&emsp;Em síntese, as etapas de aquisição, AED e pré-processamento constituem um *pipeline* padronizado, rastreável e reprodutível para sustentar as fases de modelagem e avaliação.

## 3.4. Resultados do processamento com o pipeline de pré-processamento

&emsp;Para evidenciar os efeitos do *pipeline* sobre o corpus, foram gerados gráficos a partir do *notebook* de pré-processamento. As Figuras 02 e 03 representam o impacto das transformações, acompanhadas de descrições textuais.

<div align="center">

<sub>Figura 02: Estatísticas de comprimento por etapa do pipeline</sub>

![Tabela síntese por etapa do pipeline](imagens/tabela-comprimento-por-etapa.png)

<sup>Fonte: Produzido pelos autores a partir do notebook de pré-processamento (2025).</sup>

</div>

&emsp;Observa-se redução gradual do comprimento das mensagens entre as etapas, com menor variabilidade após a normalização e a remoção de *stopwords*. Esse comportamento é desejável, pois simplifica a vetorização inicial e orienta a definição de limites de janelamento para diálogos.

&emsp;A Figura 3 apresenta um gráfico de barras com os 20 termos/stems mais frequentes após a remoção de *stopwords* e aplicação de *stemming*. Esse vocabulário evidencia o domínio de moda e atendimento e subsidia a definição de *intents* e *slots*, além de auxiliar na calibração de dicionários/ontologias para manter o tom consultivo da marca.  

&emsp;Até o presente momento, esses termos identificados foram utilizados na curadoria inicial de *intents*, permitindo mapear categorias de diálogo (ex.: dúvidas de produto, trocas, sugestões de combinação) e orientar a construção do escopo conversacional do *chatbot*. Essa etapa inicial garante que as intenções reflitam o vocabulário real do cliente, preservando a naturalidade das interações.

<div align="center">

<sub>Figura 03: Top-20 termos/stems após pré-processamento</sub>

![Top-20 stems após pré-processamento](imagens/top20-stems.png)

<sup>Fonte: Produzido pelos autores a partir do notebook de pré-processamento (2025).</sup>

</div>

&emsp;O conjunto de termos/stems mais frequentes evidencia o vocabulário característico do domínio de moda e atendimento. Esses termos subsidiam a definição de *intents* e *slots* e ajudam a calibrar dicionários/ontologias, mantendo o tom consultivo da marca.  

&emsp;Os resultados do processamento demonstram que o *pipeline* adotado reduz ruído superficial, normaliza o texto e preserva sinais semânticos relevantes. Esses artefatos já foram aplicados à curadoria inicial de *intents*, permitindo estruturar categorias de diálogo como dúvidas de produto, trocas, devoluções e sugestões de combinação. Dessa forma, orientam escolhas práticas do projeto, como limites de *tokens*, políticas de memória de diálogo e priorização de *features* iniciais, além de garantirem reprodutibilidade por meio do *notebook* de processamento.

# 4. Resultados

&emsp;...

# 5. Análise e Discussão

&emsp;...

# 6. Conclusão

&emsp;...

# Referências

<a id="ref-1"></a>
[1] LANDIM, A. R. D. B. et al. Analysing the effectiveness of chatbots as recommendation systems in fashion e-commerce: a cross-cultural comparison. **Computers in Human Behavior**, v. 142, 107659, 2024. Disponível em: <https://discovery.researcher.life/article/analysing-the-effectiveness-of-chatbots-as-recommendation-systems-in-fashion-e-commerce-a-crosscultural-comparison/8f0aebee9855310fa6db39654f2957a1>. Acesso em: 11 ago. 2025.

<a id="ref-2"></a>
[2] HUI, Kuek Shu. The Role of Natural Language Processing in Improving Customer Service and Support in E-Commerce. 15 dez. 2023. Disponível em: <http://eprints.utar.edu.my/6295/1/202306-51_Kuek_Shu_Hui_KUEK_SHU_HUI.pdf>. Acesso em: 11 ago. 2025.

<a id="ref-3"></a>
[3] GAJULA, Yogesh. Sentiment-Aware Recommendation Systems in E-Commerce: A Review from a Natural Language Processing Perspective. 3 maio 2025. Disponível em: <https://arxiv.org/abs/2505.03828>. Acesso em: 11 ago. 2025.

<a id="ref-4"></a>
[4] ISMAIL, Walaa Saber; GHAREEB, Marwa M.; YOUSSRY, Howida. Enhancing Customer Experience through Sentiment Analysis and Natural Language Processing in E-commerce. 30 set. 2024. Disponível em: <https://jowua.com/wp-content/uploads/2024/10/2024.I3.005.pdf>. Acesso em: 11 ago. 2025.

</div>
