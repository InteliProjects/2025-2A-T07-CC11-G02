## Fluxos conversacionais (definição de estados e transições)

Este documento descreve o projeto dos fluxos conversacionais do assistente Curadobia. A definição é orientada a estados, com coleta opcional de slots e transições explícitas entre estados.

### Estrutura de um estado
- **estado**: identificador único do estado/intenção
- **resposta_padrao**: mensagem padrão do bot (opcional)
- **slots_obrigatorios**: lista de informações que o bot precisa coletar (opcional)
- **perguntas_slots**: perguntas para coletar cada slot (opcional)
- **acao_final**: ação executada ao completar o estado (opcional)
- **prox_acao**: próximo estado padrão quando o diálogo segue adiante

### Estados principais e transições

- **mensagem_sistema** → `encerrar_ou_recomendar`
  - Mensagens automáticas de plataforma.

- **nao_identificado** → `encerrar_ou_recomendar`
  - Mensagem ambígua; solicita esclarecimento e oferece encerramento ou continuidade.

- **saudacao** → `encerrar_ou_recomendar`
  - Saudação inicial com tom Curadobia.

- **agradecimento** → `encerrar_ou_recomendar`
  - Reconhece agradecimentos.

- **reacao_emocional** → `encerrar_ou_recomendar`
  - Reações curtas/emoji.

- **confirmacao** → `aplicar_acao_pendente_ou_acusar_recebimento` → `encerrar_ou_recomendar`
  - Confirma procedimentos em andamento.

- **duvida_produto** → `consultar_catalogo_produto` → `encerrar_ou_recomendar`
  - Coleta: `produto`, `tamanho`, `variante`, `quantidade`.

- **solicitacao_informacao** → `responder_solicitacao_informacao` → `encerrar_ou_recomendar`
  - Coleta: `descricao`.

- **rastreamento_pedido** → `consultar_status_pedido_e_enviar_rastreio` → `encerrar_ou_recomendar`
  - Coleta: `identificador_pedido`.

- **reposicao_estoque** → `consultar_reposicao_estoque` → `encerrar_ou_recomendar`
  - Coleta: `produto`, `tamanho`, `variante`.

- **solicitacao_contato** → `registrar_solicitacao_contato` → `encerrar_ou_recomendar`
  - Coleta: `meio_contato`, `descricao` (opcional).

- **parceria_comercial** → `encaminhar_para_comercial` → `encerrar_ou_recomendar`
  - Coleta: `descricao`, `meio_contato`.

- **interesse_produto** → `criar_lead_interesse_produto` → `encerrar_ou_recomendar`
  - Coleta: `produto`, `tamanho`, `variante`.

- **troca_devolucao** → `iniciar_fluxo_troca_ou_devolucao` → `encerrar_ou_recomendar`
  - Coleta: `identificador_pedido`, `produto`, `motivo_troca`, `tamanho`.

- **problema_tecnico** → `abrir_chamado_tecnico` → `encerrar_ou_recomendar`
  - Coleta: `descricao`.

- **evento_presencial** → `informar_evento_presencial` → `encerrar_ou_recomendar`
  - Informa calendário e oferece cadastro de aviso.

- **encerrar_ou_recomendar** → `encerramento` ou para uma intenção específica
  - Mensagem: "Posso te ajudar com mais alguma coisa?". Dependendo da resposta do cliente, segue para:
    - `encerramento` (se "não")
    - Uma das intenções suportadas (se "sim" + intenção mencionada). Exemplos: `duvida_produto`, `solicitacao_informacao`, `rastreamento_pedido`, `troca_devolucao`, etc.

- **encerramento** → `encerrar_atendimento`
  - Mensagem final cordial.

### Como o fluxo avança
- Cada mensagem do cliente é mapeada em um estado/intenção.
- Estados com `slots_obrigatorios` coletam informações via `perguntas_slots` e depois executam `acao_final`.
- Após a ação, o diálogo retorna para `encerrar_ou_recomendar`. Se o cliente disser "não", vamos para `encerramento`. Se disser "sim" e mencionar uma intenção, roteamos para o estado correspondente.

### Possíveis Trajetórias

**Fluxo 1 — Dúvida sobre produto:**
O cliente inicia com uma saudação, o bot responde e pergunta se pode ajudar com mais alguma coisa. Se o cliente mencionar dúvidas sobre um produto, o sistema entra no estado `duvida_produto` e coleta informações essenciais (produto, tamanho, variante, quantidade) através de perguntas específicas. Após coletar os dados, executa a ação `consultar_catalogo_produto` e retorna encerramento/recomendação.

**Fluxo 2 — Rastreamento de pedido:**
Similar ao fluxo anterior, mas quando o cliente menciona interesse em rastrear um pedido, o sistema entra no estado `rastreamento_pedido` e solicita apenas o identificador do pedido (ID, e-mail ou CPF). Com essa informação, executa `consultar_status_pedido_e_enviar_rastreio` e retorna.

**Fluxo 3 — Troca/Devolução:**
Para solicitações de troca ou devolução, o sistema entra no estado `troca_devolucao` e coleta múltiplas informações: identificador do pedido, produto específico, motivo da troca/devolução e detalhes de tamanho. Após coletar todos os slots obrigatórios, executa `iniciar_fluxo_troca_ou_devolucao` e retorna.

**Estados de entrada direta:**
Alguns estados como `agradecimento`, `reacao_emocional`, `confirmacao` e `evento_presencial` não requerem coleta de slots e vão diretamente após executar suas ações ou respostas padrão.

**Estados com slots simples:**
Estados como `solicitacao_informacao` e `problema_tecnico` coletam apenas uma descrição antes de executar suas ações. Outros como `reposicao_estoque`, `solicitacao_contato`, `parceria_comercial` e `interesse_produto` coletam múltiplos slots específicos para suas finalidades.

**Encerramento/recomendação:**
O estado `encerrar_ou_recomendar` funciona como um ponto central que oferece ao cliente a opção de encerrar o atendimento ou continuar com uma nova solicitação. Se o cliente escolher continuar, o sistema identifica a nova intenção e roteia para o estado apropriado, permitindo múltiplas interações em uma única sessão.

