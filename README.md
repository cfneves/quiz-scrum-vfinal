<div align="center">

# 🏆 Quiz Scrum

**Plataforma interativa de avaliação em Metodologias Ágeis**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.47+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-2.3+-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-6.2+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

### [🚀 Acessar o App ao Vivo](https://quiz-scrum-vfinal-cfn.streamlit.app/)

*Desenvolvido para o curso de Metodologias Ágeis com Versionamento — SENAI/SC · CentroWEG*

</div>

---

## 📌 Sobre o Projeto

O **Quiz Scrum** é uma aplicação web interativa que permite que professores avaliem o conhecimento de alunos sobre o **framework Scrum** de forma prática, visual e gamificada.

A plataforma conta com três ambientes:

- 📝 **Cadastro** — alunos criam sua própria conta com e-mail e senha, sem depender do professor
- 🎓 **Área do Aluno** — realiza o quiz, recebe feedback imediato e visualiza o ranking da turma
- 👨‍🏫 **Área do Professor** — acompanha desempenho individual e coletivo, exporta relatórios

> **Motivação:** substituir avaliações estáticas por uma experiência digital engajante, com ranking em tempo real e gabarito comentado, promovendo o aprendizado ativo.

---

## ✨ Funcionalidades

### 📝 Cadastro de Alunos
- Auto-cadastro com e-mail e senha (sem precisar pedir ao professor)
- Validação de e-mail, senha mínima de 4 caracteres e confirmação
- Armazenamento local (`alunos.json`) ou em nuvem (Google Sheets) — automático

### 🎓 Área do Aluno
- Login seguro com e-mail e senha
- Quiz com **20 perguntas sobre Scrum** embaralhadas por aluno (cada um vê uma ordem diferente)
- Barra de progresso em tempo real durante o quiz
- Resultado imediato com nota, acertos, erros e percentual
- **Gabarito comentado** com explicação de cada questão
- **Ranking da turma** em gráfico de barras com posição destacada

### 👨‍🏫 Área do Professor
- Acesso exclusivo por lista de usuários autorizados (`config.py`)
- KPIs da turma: média geral, taxa de aprovação, total de alunos avaliados
- Gráfico de barras com nota por aluno (verde = aprovado, vermelho = reprovado)
- Histograma de distribuição de notas
- Ranking completo com tabela interativa e colunas de progresso
- **Exportação em CSV** para análise no Excel ou Google Sheets
- Botão de atualização manual dos dados

---

## 🛠️ Stack Tecnológica

| Tecnologia | Versão | Função |
|---|---|---|
| **Python** | 3.11+ | Linguagem principal |
| **Streamlit** | 1.47+ | Framework de interface web |
| **Pandas** | 2.3+ | Manipulação e agregação de dados |
| **Plotly** | 6.2+ | Gráficos interativos |
| **gspread** | 6.2+ | Integração com Google Sheets |
| **google-auth** | 2.40+ | Autenticação Google (service account) |

---

## 📁 Estrutura do Projeto

```
quiz-scrum/
│
├── app.py                      # Ponto de entrada — roteamento principal
├── config.py                   # Constantes, settings e SESSION_DEFAULTS
├── perguntas.py                # Banco de 20 questões sobre Scrum
├── setup_oauth.py              # Script auxiliar de verificação OAuth2 local
│
├── services/                   # Camada de negócio (sem UI)
│   ├── auth_service.py         # Autenticação (secrets + alunos.json + Sheets)
│   ├── register_service.py     # Cadastro de novos alunos
│   ├── quiz_service.py         # Regras do quiz (nota, resultado, embaralhamento)
│   ├── storage_service.py      # Armazenamento local em CSV (primário)
│   └── sheets_service.py       # Sincronização Google Sheets (cloud/opcional)
│
├── components/                 # Componentes de interface
│   ├── styles.py               # CSS premium centralizado
│   ├── signature.py            # Assinatura do desenvolvedor
│   ├── landing_ui.py           # Tela inicial (Aluno / Professor)
│   ├── login_ui.py             # Tela de login (contextual por papel)
│   ├── register_ui.py          # Tela de cadastro de alunos
│   ├── quiz_ui.py              # Tela do quiz + sidebar
│   ├── results_ui.py           # Tela de resultados + ranking
│   └── professor_ui.py         # Painel do professor
│
├── tests/                      # Testes automatizados
│   ├── conftest.py             # Mock do Streamlit para testes
│   ├── test_quiz_service.py    # 18 testes de lógica de quiz
│   └── test_auth_service.py    # 8 testes de autenticação
│
├── data/
│   └── respostas.csv           # Respostas salvas localmente (gerado em runtime)
│
├── .streamlit/
│   ├── config.toml             # Tema dark premium
│   └── secrets.toml.example   # Modelo de configuração de secrets
│
├── alunos.example.json         # Modelo de arquivo de usuários
├── .gitignore                  # Segurança — credenciais nunca commitadas
└── requirements.txt            # Dependências (6 pacotes)
```

---

## 🚀 Execução Local

### Pré-requisitos

- Python 3.11 ou superior
- pip

### 1. Clone o repositório

```bash
git clone https://github.com/cfneves/quiz-scrum-vfinal.git
cd quiz-scrum-vfinal
```

### 2. Crie e ative um ambiente virtual

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure os usuários (professores)

Copie o arquivo de exemplo e edite com as credenciais do professor:

```bash
cp alunos.example.json alunos.json
```

Edite `alunos.json`:

```json
{
  "alunos": {
    "professor": "sua_senha_aqui"
  }
}
```

> ⚠️ **Segurança:** `alunos.json` está no `.gitignore` — nunca é commitado.
> Novos alunos se cadastram diretamente pela tela de cadastro do app.

### 5. Execute a aplicação

```bash
streamlit run app.py
```

Acesse em: **http://localhost:8501**

---

## ☁️ Deploy no Streamlit Cloud

O app está publicado em: **https://quiz-scrum-vfinal-cfn.streamlit.app/**

### Passo a passo para publicar sua própria instância

1. Faça fork deste repositório para sua conta GitHub
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. **New app** → selecione seu repositório → **Main file path:** `app.py`
4. Antes de publicar, configure os **Secrets** (veja abaixo)
5. Clique em **Deploy**

### Configuração de Secrets no Streamlit Cloud

Acesse **App → ⋮ → Settings → Secrets** e cole o seguinte conteúdo (substitua com seus dados reais):

```toml
# Usuários com acesso garantido (professor e qualquer aluno pré-cadastrado)
# Novos alunos que se cadastrarem pelo app são salvos automaticamente no Google Sheets
[alunos]
"professor" = "senha_do_professor"
"seu.email@instituicao.edu.br" = "sua_senha"

# Service Account do Google Cloud — necessário para persistência dos dados e cadastros
# Sem isso, os dados são perdidos a cada restart do servidor
[gcp_service_account]
type = "service_account"
project_id = "seu-projeto-id"
private_key_id = "id-da-chave"
private_key = """
-----BEGIN PRIVATE KEY-----
SUA_CHAVE_PRIVADA_AQUI
-----END PRIVATE KEY-----
"""
client_email = "nome@projeto.iam.gserviceaccount.com"
client_id = "000000000000"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/nome%40projeto.iam.gserviceaccount.com"
universe_domain = "googleapis.com"
```

> **Importante:** use aspas triplas `"""` para a `private_key` — é o formato TOML correto para chaves multilinhas.

---

## 🔑 Configuração do Google Sheets (para persistência em nuvem)

Sem o Google Sheets, os dados são perdidos sempre que o servidor do Streamlit Cloud reinicia. Com ele, os cadastros e resultados ficam persistentes.

### 1. Criar o projeto no Google Cloud

1. Acesse [console.cloud.google.com](https://console.cloud.google.com)
2. Crie um projeto (ex: `quiz-scrum`)
3. Ative as APIs:
   - **Google Sheets API**
   - **Google Drive API**

### 2. Criar uma Service Account

1. Vá em **APIs & Services → Credentials**
2. **+ Create Credentials → Service Account**
3. Nome: `quiz-scrum-app` → Criar
4. Clique na service account criada → aba **Keys** → **Add Key → Create new key → JSON**
5. Salve o arquivo JSON baixado (nunca commite esse arquivo)

### 3. Criar a planilha

1. Acesse [sheets.google.com](https://sheets.google.com)
2. Crie uma nova planilha com o nome exato: **`RespostasAlunos`**
3. Abra o JSON da service account e copie o campo `client_email`
4. Na planilha: **Compartilhar → cole o `client_email` → Editor → Confirmar**

### 4. Configurar os secrets

Cole o conteúdo do JSON na seção `[gcp_service_account]` dos secrets do Streamlit Cloud (conforme modelo acima).

### Como os dados são organizados na planilha

| Aba | Conteúdo |
|---|---|
| **Sheet1** (aba principal) | Respostas do quiz: usuario, questão, resposta, correta, data_hora |
| **Usuarios** | Alunos auto-cadastrados: email, senha |

---

## ⚙️ Configurações do Projeto

### Controle de acesso ao painel do professor

Edite `config.py` e adicione os e-mails autorizados:

```python
PROFESSOR_USUARIOS: list[str] = [
    "professor",
    "seu.email@instituicao.edu.br",
]
```

### Regras de pontuação e aprovação

```python
PONTOS_POR_ACERTO = 0.5   # Nota = acertos × 0.5 → máximo 10.0
NOTA_APROVACAO    = 7.0   # Nota mínima para aprovação
```

### Nome da planilha Google Sheets

```python
SHEETS_NAME = "RespostasAlunos"   # Nome exato da planilha compartilhada
```

### Tema visual

Edite `.streamlit/config.toml`:

```toml
[theme]
primaryColor = "#00BFFF"        # Azul elétrico
backgroundColor = "#0a0e1a"     # Fundo escuro
secondaryBackgroundColor = "#111827"
textColor = "#E0E0E0"
```

---

## 📖 Como Usar

### 📝 Fluxo de Cadastro (novo aluno)

```
Tela Inicial → [Cadastrar] → Preenche e-mail e senha → Cadastrado com sucesso → Login
```

1. Na tela inicial, clique em **"Cadastrar"** (abaixo de "Entrar como Aluno")
2. Preencha e-mail, senha e confirmação de senha
3. Após o cadastro, clique em **"Ir para o login"**
4. Faça login com as credenciais recém-criadas

### 🎓 Fluxo do Aluno

```
Tela Inicial → [Entrar como Aluno] → Login
    → Quiz (20 perguntas embaralhadas)
    → Resultado com nota e gabarito comentado
    → Ranking da turma em tempo real
```

1. Clique em **"Entrar como Aluno"** e faça login
2. Responda as 20 perguntas (barra de progresso no topo e na sidebar)
3. Clique em **"Enviar Respostas"** ao terminar
4. Veja sua nota, o gabarito comentado e sua posição no ranking

### 👨‍🏫 Fluxo do Professor

```
Tela Inicial → [Entrar como Professor] → Login
    → Painel com KPIs, gráficos e ranking completo
    → Exportar CSV (opcional)
```

1. Clique em **"Entrar como Professor"** e faça login com conta autorizada
2. Visualize KPIs, gráfico de notas, histograma e ranking completo
3. Use **"Atualizar dados"** para ver novos resultados
4. Exporte para CSV se necessário

---

## 🔒 Segurança

| Item | Status | Observação |
|---|---|---|
| Credenciais no repositório | ✅ Protegido | `.gitignore` bloqueia `alunos.json`, `*.json` de service account e `secrets.toml` |
| Senhas em texto puro | ⚠️ Educacional | Adequado para uso em sala de aula; use bcrypt em produção |
| Google Service Account | ✅ Seguro | JSON nunca commitado; credenciais via `st.secrets` no cloud |
| Dados dos alunos | ✅ Protegido | CSV local fora do controle de versão; no cloud, somente via Sheets autenticado |
| Acesso ao painel do professor | ✅ Controlado | Verificação dupla: autenticação + lista `PROFESSOR_USUARIOS` em `config.py` |
| Auto-cadastro | ✅ Validado | E-mail, senha mínima e verificação de duplicidade antes de salvar |

> Para produção com muitos usuários, recomenda-se bcrypt para senhas e autenticação via banco de dados.

---

## 🧪 Testes Automatizados

O projeto possui **26 testes** cobrindo toda a lógica de negócio:

```bash
pip install pytest
pytest tests/ -v
```

| Módulo | Testes | Cobertura |
|---|---|---|
| `quiz_service` | 18 | Verificação de resposta, cálculo de nota, embaralhamento determinístico |
| `auth_service` | 8 | Login válido, senha errada, usuário inexistente, arquivo ausente |

---

## 🏗️ Arquitetura e Decisões Técnicas

### Armazenamento em camadas

```
Submissão do quiz
    ↓
CSV local (primário, instantâneo)
    ↓
Google Sheets (secundário, cloud, assíncrono)

Leitura de resultados
    ↓
CSV local (se existir e não vazio)
    ↓
Google Sheets (fallback automático no cloud)
```

### Embaralhamento determinístico

Cada aluno vê as perguntas em uma ordem diferente, mas sempre a **mesma ordem toda vez que faz login**. Isso impede cola por ordem de alternativas sem afetar a reprodutibilidade:

```python
random.Random(username).shuffle(perguntas)
```

### Cadastro local vs. cloud

| Ambiente | Onde cadastros são salvos |
|---|---|
| Local (`alunos.json` presente) | Gravado em `alunos.json` |
| Cloud (Streamlit Cloud) | Gravado na aba `Usuarios` do Google Sheets |

---

## 📚 Conteúdo do Quiz

As 20 questões cobrem os principais conceitos do **Scrum Guide**:

- Valores e pilares do Scrum
- Papéis: Product Owner, Scrum Master, Developers
- Eventos: Sprint, Daily Scrum, Sprint Planning, Sprint Review, Sprint Retrospective
- Artefatos: Product Backlog, Sprint Backlog, Incremento
- Definition of Done e Sprint Goal
- Diferenças entre Scrum e metodologias tradicionais

---

## 👨‍💻 Autor

<div align="center">

**Cláudio Ferreira Neves**

Especialista em Business Intelligence, Big Data & Analytics - Ciência de Dados<br>Especialista em Ciência de Dados e Inteligência Artificial

[![GitHub](https://img.shields.io/badge/GitHub-cfneves-181717?style=flat&logo=github)](https://github.com/cfneves)
[![App](https://img.shields.io/badge/App-quiz--scrum--vfinal-FF4B4B?style=flat&logo=streamlit)](https://quiz-scrum-vfinal-cfn.streamlit.app/)

*SENAI/SC — CentroWEG*

</div>

---

## 📄 Licença

Distribuído sob a licença MIT. Consulte [LICENSE](LICENSE) para mais informações.

---

<div align="center">

Feito com ❤️ usando **Python** · **Streamlit** · **Pandas** · **Plotly** · **Google Sheets**

</div>
