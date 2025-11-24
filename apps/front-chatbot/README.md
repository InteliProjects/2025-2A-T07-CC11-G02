# Curadobia Chatbot Frontend

Frontend React TypeScript para o chatbot da Curadobia - Curadoria de Moda.

## 🎨 Design

O frontend foi desenvolvido com um design minimalista e elegante, seguindo as cores da marca Curadobia:
- **Primary**: #020202 (preto), #6D7358 (verde escuro)
- **Secondary**: #886338 (dourado)
- **Neutral**: #FFFFFF (branco), #F2F2F2 (cinza claro)

## 🚀 Tecnologias

- **React 18** com TypeScript
- **Vite** para build e desenvolvimento
- **Tailwind CSS** para estilização
- **Axios** para comunicação com a API
- **Lucide React** para ícones

## 📁 Estrutura do Projeto

```
src/
├── components/          # Componentes React
│   ├── ChatInterface.tsx    # Interface principal do chat
│   ├── ChatHeader.tsx       # Cabeçalho do chat
│   ├── Message.tsx          # Componente de mensagem
│   ├── ChatInput.tsx        # Input para envio de mensagens
│   └── TypingIndicator.tsx  # Indicador de digitação
├── hooks/               # Custom hooks
│   └── useChat.ts           # Hook para gerenciar estado do chat
├── services/            # Serviços de API
│   └── api.ts               # Configuração do Axios e endpoints
├── types/               # Definições de tipos TypeScript
│   └── chat.ts              # Tipos relacionados ao chat
├── App.tsx              # Componente principal
├── main.tsx             # Ponto de entrada
└── index.css            # Estilos globais
```

## 🛠️ Instalação e Execução

### Pré-requisitos

- Node.js 18+ 
- npm ou yarn
- Backend da API rodando em http://localhost:8000

### Instalação

```bash
# Instalar dependências
npm install

# Executar em modo de desenvolvimento
npm run dev

# Build para produção
npm run build

# Preview do build
npm run preview
```

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
VITE_API_URL=http://localhost:8000
VITE_DEV_MODE=true
```

## 🔧 Configuração

### API Backend

O frontend se conecta ao backend através da URL configurada em `VITE_API_URL`. Por padrão, espera que o backend esteja rodando em `http://localhost:8000`.

### Endpoints Utilizados

- `POST /chat` - Envio de mensagens
- `GET /healthz` - Verificação de saúde da API
- `GET /users/*` - Gerenciamento de usuários (opcional)

## 🎯 Funcionalidades

### ✅ Implementadas

- **Interface de Chat**: Interface limpa e responsiva
- **Envio de Mensagens**: Input com auto-resize e envio por Enter
- **Histórico de Mensagens**: Persistência durante a sessão
- **Indicador de Digitação**: Feedback visual durante processamento
- **Status de Conexão**: Indicador de conectividade com a API
- **Tratamento de Erros**: Mensagens de erro amigáveis
- **Responsividade**: Design adaptável para mobile e desktop
- **Animações**: Transições suaves e indicadores visuais

### 🔄 Funcionalidades Futuras

- **Anexos**: Upload de imagens e arquivos
- **Histórico Persistente**: Salvar conversas no localStorage
- **Temas**: Modo escuro/claro
- **Notificações**: Alertas sonoros para novas mensagens
- **Comandos Especiais**: Atalhos de teclado
- **Integração com Usuários**: Sistema de autenticação

## 🎨 Design System

### Cores

```css
/* Primary Colors */
--primary-50: #F2F2F2
--primary-500: #6D7358
--primary-900: #020202

/* Secondary Colors */
--secondary-500: #886338

/* Neutral Colors */
--neutral-50: #FFFFFF
--neutral-100: #F2F2F2
--neutral-500: #737373
--neutral-900: #171717
```

### Tipografia

- **Fonte**: Inter (Google Fonts)
- **Pesos**: 300, 400, 500, 600, 700

### Componentes

- **Bordas**: Arredondadas (rounded-full, rounded-2xl)
- **Sombras**: Sutis (shadow-sm, shadow-md, shadow-lg)
- **Transições**: 200ms ease-in-out
- **Animações**: fade-in, slide-up, pulse

## 🔗 Integração com Backend

O frontend se integra com o backend desenvolvido em Python/FastAPI através de:

1. **ChatRequest**: `{ text: string, external_id?: string }`
2. **ChatResponse**: `{ response: string }`
3. **Health Check**: Verificação periódica de conectividade

### Exemplo de Uso

```typescript
// Envio de mensagem
const response = await chatApi.sendMessage({
  text: "Olá, preciso de ajuda com um produto",
  external_id: "user123"
});

// Resposta
console.log(response.response); // "Oi! Como posso ajudar?"
```

## 📱 Responsividade

O design é totalmente responsivo com breakpoints:
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px  
- **Desktop**: > 1024px

## 🧪 Testes

```bash
# Linting
npm run lint

# Type checking
npm run type-check
```

## 🚀 Deploy

### Build de Produção

```bash
npm run build
```

Os arquivos serão gerados na pasta `dist/` e podem ser servidos por qualquer servidor web estático.

### Variáveis de Produção

```env
VITE_API_URL=https://api.curadobia.com.br
VITE_DEV_MODE=false
```

## 📄 Licença

Este projeto é parte do sistema Curadobia e está sob a mesma licença do projeto principal.
