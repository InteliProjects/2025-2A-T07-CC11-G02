<div align="justify">

# 2025-1B-T07-CC11-G02

Repositório do grupo 2025-1B-T07-CC11-G02

<table width="100%">
  <tr>
    <td width="50%" align="center">
      <a href="https://curadobia.com.br/">
        <img src="https://s3.wasabisys.com/curadobia.smserver.com.br/logo-safe-env.png" alt="Curadobia" height="80px">
      </a>
    </td>
    <td width="50%" align="center">
      <a href="https://www.inteli.edu.br/">
        <img src="https://www.inteli.edu.br/wp-content/uploads/2024/06/logo-inteli-3-768x420-1.png" alt="Inteli – Instituto de Tecnologia e Liderança" height="80px">
      </a>
    </td>
  </tr>
</table>

# Introdução

Este repositório consolida o projeto de um **sistema de processamento de linguagem natural para atendimento automatizado**, desenvolvido em parceria entre a Curadobia e o Inteli. A Curadobia enfrentava o desafio de oferecer atendimento personalizado, humanizado e consultivo de forma automatizada e escalável, sem comprometer a qualidade e o tom de voz próximos que fidelizam suas clientes. Como marketplace com forte curadoria e consultoria de moda, percebia que um atendimento genérico não entregava a orientação real que suas clientes buscam: dicas práticas, combinação de peças, informações sobre modelagem e caimento, e apoio para entender quais produtos fazem sentido para seu estilo de vida. O grupo Nsync desenvolveu uma solução de chatbot inteligente baseada em algoritmos de PLN e recomendações personalizadas, que responde dúvidas frequentes, sugere produtos e guia o processo de compra, mantendo o tom de voz próximo, humano e consultivo que é a essência da Curadobia. 

---

## Projeto: Chatbot para Recomendação de Produtos com PLN

## Descrição

O projeto propõe um **MVP** composto por:

- Um **sistema de chatbot baseado em PLN** que responde perguntas frequentes e oferece suporte consultivo automatizado
- **Engine de recomendação** que sugere produtos com base no perfil e histórico do cliente
- **Interface conversacional** que mantém o tom próximo, humano e consultivo da marca Curadobia

---

## Grupo 2: Nsync

# 👨‍🎓 Integrantes

- [Ana Luisa Goes Barbosa](https://www.linkedin.com/in/ana-luisa-goes-barbosa/)
- [Gabriel Coletto Silva](https://www.linkedin.com/in/gabrielcolettosilva/)
- [Gabriel Farias](https://www.linkedin.com/in/gabriel-farias-alves/)
- [Hugo Noyma](https://www.linkedin.com/in/hugo-noyma/)
- [João Paulo Santos](https://www.linkedin.com/in/jo%C3%A3o-paulo-santos-872753264/)
- [Lucas Nogueira Nunes](https://www.linkedin.com/in/lucas-nogueira-nunes/)
- [Mauro das Chagas Junior](https://www.linkedin.com/in/mauro-das-chagas-junior/)
- [Vitto Mazeto](https://www.linkedin.com/in/vitto-mazeto/)

### 👩‍🏫 Professores e Instrutores

## Orientador  

- [Tomaz Mikio Sasaki](https://www.linkedin.com/in/tmsasaki/)

## Instrutores

- [Jefferson Silva - Professor de Programação](https://www.linkedin.com/in/jefferson-o-silva/)
- [Filipe Gonçalves - Professor de Liderança](https://www.linkedin.com/in/filipe-gon%C3%A7alves-08a55015b/)
- [Cristina Gramani - Professora de Matemática](https://www.linkedin.com/in/cristinagramani/)
- [Pedro Teberga - Professor de Negócios](https://www.linkedin.com/in/pedroteberga/)
- [Rodolfo Goya - Professor de Programação](https://www.linkedin.com/in/rodolfo-goya-6ab187/)

---

## 📁 Estrutura do Repositório

O repositório segue uma organização padronizada:

```
/
├── README.md                    # Este arquivo
├── .gitignore                   # Arquivos ignorados pelo git
├── apps/                        # Aplicações do projeto
│   ├── back-chatbot/           # Backend do chatbot
│   └── front-chatbot/          # Frontend do chatbot
├── docs/                        # Documentação do projeto
├── notebooks/                   # Jupyter notebooks de desenvolvimento
├── slides/                      # Slides das apresentações
└── assets/                      # Imagens e recursos visuais
```

---

## 🛠️ Configuração para Desenvolvimento

### Pré-requisitos

- **Python 3.11.9+**  
- **Node.js 18+** (para frontend)
- **Git**  
- **Docker** (para executar via containers)

### Requisitos de Hardware

**Mínimo recomendado:**
- **RAM:** 8GB (16GB recomendado para treinamento de modelos)
- **CPU:** 4 cores (8 cores recomendado)
- **Armazenamento:** 10GB livres
- **GPU:** Opcional, mas recomendada para treinamento de modelos ML

**Para desenvolvimento:**
- **RAM:** 16GB+
- **CPU:** 8 cores+
- **GPU:** NVIDIA com CUDA (opcional, mas recomendada)

### Requisitos de Serviços

Para executar completamente o projeto, são necessários os seguintes serviços externos:

- **Google Colab Pro+** - Para execução dos notebooks de desenvolvimento e treinamento de modelos
- **Hugging Face** - Para acesso aos modelos de linguagem e embeddings (requer token de acesso)
- **GitHub** - Para versionamento e colaboração no código
- **Docker Hub** - Para pull das imagens base necessárias (opcional, mas recomendado)

### Backend (Chatbot)

```bash
cd apps/back-chatbot
pip install -r requirements.txt
python run_server.py
```

### Frontend

```bash
cd apps/front-chatbot
npm install
npm run dev
```

---

## Tags

**Sprint 1:**

- Pipeline de Processamento e Base de Dados
- Análise de Dados e Taxonomia de Intenções
- Draft do Artigo (Introdução + Trabalhos Relacionados + Materiais e Métodos)
  
**Sprint 2:**

- Implementação de Modelos de Embeddings
- Artigo com Avaliação de Embeddings

**Sprint 3:**

- Implementação de Modelo LLM ou BERT
- Artigo com Avaliação de Modelo LLM ou BERT
  
**Sprint 4:**

- Implementação de Classificadores para Mapeamento de Produtos
- Artigo com Implementação e Avaliação da Classificação de Produtos
- Apresentação Sprint

**Sprint 5:**

- Implementação Final do Repositório
- Artigo Final Completo
- Apresentação FINAL

---

## 📌 Como Rodar o Projeto

Para executar o projeto e testar o chatbot desenvolvido, siga os passos abaixo:

### 🔧 Executando com Docker (Recomendado)

1. **Clone o repositório:**

   ```bash
   git clone <url-do-repositorio>
   cd 2025-2A-T07-CC11-G02
   ```

2. **Configure as variáveis de ambiente:**

   ```bash
   # Crie um arquivo .env na raiz do projeto
   echo "HF_TOKEN=seu_token_huggingface" > .env
   ```

3. **Execute o projeto completo:**

   ```bash
   # Inicia backend e frontend com cache do Hugging Face
   docker-compose up --build
   ```

4. **Acesse as aplicações:**
   - **Frontend:** <http://localhost:5173>
   - **Backend API:** <http://localhost:8000>
   - **Documentação da API:** <http://localhost:8000/docs>

### 🛠️ Executando Manualmente

#### Backend

```bash
# Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

cd apps/back-chatbot
pip install -r requirements.txt
python run_server.py
```

#### Frontend

```bash
cd apps/front-chatbot
npm install
npm run dev
```

### 🐳 Comandos Docker Úteis

```bash
# Parar os serviços
docker-compose down

# Rebuild apenas um serviço
docker-compose build backend
docker-compose build frontend

# Ver logs em tempo real
docker-compose logs -f

# Executar em background
docker-compose up -d

# Limpar cache do Hugging Face (se necessário)
docker-compose down -v
```

### 🦖 Servidor Shrek (Desenvolvimento)

Para desenvolvimento local com hot-reload e debugging:

```bash
# Backend com Shrek (desenvolvimento)
cd apps/back-chatbot
python run_server.py

# Frontend com Vite (desenvolvimento)
cd apps/front-chatbot
npm run dev
```

**Nota:** O servidor Shrek é usado para desenvolvimento local, oferecendo melhor debugging e hot-reload comparado ao Docker.

### 🔧 Troubleshooting

**Problemas comuns e soluções:**

1. **Erro de token Hugging Face:**
   ```bash
   # Verifique se o token está configurado
   echo $HF_TOKEN
   # Ou no arquivo .env
   cat .env
   ```

2. **Problemas com dependências Python:**
   ```bash
   # Reinstale as dependências
   pip install --upgrade pip
   pip install -r apps/back-chatbot/requirements.txt
   ```

3. **Erro de porta em uso:**
   ```bash
   # Verifique processos usando as portas
   lsof -i :8000  # Backend
   lsof -i :5173  # Frontend
   ```

4. **Problemas com Docker:**
   ```bash
   # Limpe containers e volumes
   docker-compose down -v
   docker system prune -f
   ```

5. **Cache do Hugging Face:**
   ```bash
   # Limpe cache se necessário
   rm -rf ~/.cache/huggingface/
   ```

---

## 📋 Licença

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/">
<a property="dct:title" rel="cc:attributionURL">Nsync</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName">Inteli, Ana Luisa Goes Barbosa, Gabriel Coletto Silva, Gabriel Farias, Hugo Noyma, João Paulo Santos, Lucas Nogueira Nunes, Mauro das Chagas Junior, Vitto Mazeto, Curadobia</a> is licensed under <a href="https://creativecommons.org/licenses/by/4.0/" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.
</p>

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1">

---

**Contato:** Em caso de dúvidas ou sugestões, entre em contato com os integrantes do projeto ou com o professor orientador.

</div>
