<div align="center">

# 🏆 Quiz Scrum

**Plataforma de avaliação de conhecimentos em Metodologias Ágeis**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.47+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-2.3+-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-6.2+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

*Desenvolvido para o curso de Metodologias Ágeis com Versionamento — SENAI/SC · CentroWEG*

</div>

---

## 📌 Sobre o Projeto

O **Quiz Scrum** é uma aplicação web interativa que permite que professores avaliem o conhecimento de alunos sobre o **framework Scrum** de forma prática, visual e gamificada.

A plataforma conta com dois ambientes distintos:

- 🎓 **Área do Aluno** — realiza o quiz, recebe feedback imediato e visualiza o ranking da turma
- 👨‍🏫 **Área do Professor** — acompanha o desempenho individual e coletivo, exporta relatórios em CSV

> **Motivação:** substituir avaliações estáticas por uma experiência digital engajante, com ranking em tempo real e gabarito comentado, promovendo o aprendizado ativo.

---

## ✨ Funcionalidades

### Para o Aluno
- 🔐 Login seguro com usuário e senha
- 📋 Quiz com **20 perguntas sobre Scrum** embaralhadas por aluno (cada um vê uma ordem diferente)
- 📊 Barra de progresso em tempo real durante o quiz
- ✅ Resultado imediato com nota, acertos, erros e percentual
- 📘 **Gabarito comentado** com explicação de cada questão
- 🏆 **Ranking da turma** em gráfico de barras — veja sua posição entre os colegas

### Para o Professor
- 🔑 Acesso exclusivo ao painel de controle
- 📈 KPIs da turma: média geral, taxa de aprovação, total de alunos
- 📊 Gráfico de barras com nota de cada aluno (aprovados em verde, reprovados em vermelho)
- 📉 Histograma de distribuição de notas
- 🏅 Ranking completo da turma com tabela interativa
- ⬇️ **Exportação em CSV** para análise externa (Excel, Google Sheets)
- 🔄 Atualização manual dos dados

---

## 🛠️ Stack Tecnológica

| Tecnologia | Versão | Função |
|---|---|---|
| **Python** | 3.11+ | Linguagem principal |
| **Streamlit** | 1.47+ | Framework de interface web |
| **Pandas** | 2.3+ | Manipulação e agregação de dados |
| **Plotly** | 6.2+ | Gráficos interativos |
| **gspread** | 6.2+ | Integração opcional com Google Sheets |
| **google-auth-oauthlib** | 1.2+ | Autenticação OAuth2 Google |

---

## 📁 Estrutura do Projeto

```
quiz-scrum/
│
├── app.py                      # ✅ Ponto de entrada — roteamento principal
├── config.py                   # ⚙️  Constantes, settings e SESSION_DEFAULTS
├── perguntas.py                # 📚 Banco de 20 questões sobre Scrum
├── setup_oauth.py              # 🔧 Script de verificação das credenciais Google
│
├── services/                   # 🧠 Camada de negócio (sem UI)
│   ├── auth_service.py         #    Autenticação de usuários
│   ├── quiz_service.py         #    Regras do quiz (nota, resultado, embaralhamento)
│   ├── storage_service.py      #    Armazenamento local em CSV (primário)
│   └── sheets_service.py       #    Sincronização Google Sheets (opcional)
│
├── components/                 # 🖥️  Componentes de interface
│   ├── styles.py               #    CSS premium centralizado
│   ├── signature.py            #    Assinatura do desenvolvedor
│   ├── landing_ui.py           #    Tela inicial (Aluno / Professor)
│   ├── login_ui.py             #    Tela de login (contextual por papel)
│   ├── quiz_ui.py              #    Tela do quiz + sidebar
│   ├── results_ui.py           #    Tela de resultados + ranking
│   └── professor_ui.py         #    Painel do professor
│
├── tests/                      # 🧪 Testes automatizados
│   ├── conftest.py             #    Mock do Streamlit para testes
│   ├── test_quiz_service.py    #    18 testes de lógica de quiz
│   └── test_auth_service.py    #    8 testes de autenticação
│
├── data/
│   └── respostas.csv           # 📄 Respostas salvas localmente (gerado em runtime)
│
├── .streamlit/
│   └── config.toml             # 🎨 Tema dark premium
│
├── alunos.example.json         # 👥 Modelo de arquivo de usuários
├── .gitignore                  # 🔒 Segurança — credenciais nunca commitadas
└── requirements.txt            # 📦 Dependências mínimas (6 pacotes)
```

---

## 🚀 Instalação e Configuração

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

### 4. Configure os usuários

Copie o arquivo de exemplo e edite com os dados da sua turma:

```bash
cp alunos.example.json alunos.json
```

Edite `alunos.json` conforme o formato:

```json
{
  "alunos": {
    "professor": "sua_senha_aqui",
    "nome.aluno@email.com": "matricula_ou_senha"
  }
}
```

> ⚠️ **Segurança:** `alunos.json` está no `.gitignore` e **nunca deve ser commitado** — contém senhas.

### 5. Execute a aplicação

```bash
streamlit run app.py
```

Acesse em: **http://localhost:8501**

---

## ⚙️ Configuração Avançada

### Usuários com acesso ao Painel do Professor

Edite `config.py` e adicione os usernames autorizados:

```python
PROFESSOR_USUARIOS: list[str] = [
    "professor",
    "seu.email@instituicao.edu.br",
]
```

### Regras de aprovação e pontuação

Em `config.py`:

```python
PONTOS_POR_ACERTO = 0.5   # Nota = acertos × 0.5 → máximo 10.0
NOTA_APROVACAO    = 7.0   # Nota mínima para aprovação
```

### Integração opcional com Google Sheets

A aplicação funciona **100% local** sem nenhuma configuração adicional. O Google Sheets é opcional para sincronização em nuvem.

Para habilitá-lo:

1. Acesse [console.cloud.google.com](https://console.cloud.google.com)
2. Crie um projeto → **APIs & Services** → **Credentials**
3. **Create Credentials** → **OAuth 2.0 Client ID** → Desktop App → Baixe o JSON
4. Salve em `~/.config/gspread/credentials.json`
5. Execute o verificador:
   ```bash
   python setup_oauth.py
   ```
6. Autorize o acesso com sua conta Google no navegador
7. Compartilhe a planilha `RespostasAlunos` com sua conta

---

## 📖 Como Usar

### 🎓 Fluxo do Aluno

```
Tela Inicial → [Entrar como Aluno] → Login
    → Quiz (20 perguntas embaralhadas)
    → Resultado com nota e gabarito comentado
    → Ranking da turma em tempo real
```

1. Acesse o sistema e clique em **"Entrar como Aluno"**
2. Faça login com usuário e senha fornecidos pelo professor
3. Responda as 20 perguntas sobre Scrum (barra de progresso no topo e na sidebar)
4. Clique em **"Enviar Respostas"** ao terminar
5. Veja sua nota, o gabarito comentado e sua posição no ranking

### 👨‍🏫 Fluxo do Professor

```
Tela Inicial → [Entrar como Professor] → Login
    → Painel com KPIs, gráficos e ranking completo
    → Exportar CSV (opcional)
```

1. Acesse o sistema e clique em **"Entrar como Professor"**
2. Faça login com uma conta autorizada em `PROFESSOR_USUARIOS`
3. Visualize o painel com:
   - Média da turma, taxa de aprovação, total de alunos
   - Gráfico de notas por aluno
   - Histograma de distribuição
   - Ranking completo com tabela interativa
4. Clique em **"Atualizar dados"** para ver novos resultados
5. Exporte para CSV se necessário

---

## 🔒 Segurança

| Item | Status | Observação |
|---|---|---|
| Credenciais no repositório | ✅ Protegido | `.gitignore` bloqueia `alunos.json` e `credenciais.json` |
| Senhas em texto puro | ⚠️ Melhorar | Adequado para uso educacional local; use bcrypt em produção |
| Google OAuth2 | ✅ Seguro | Token armazenado fora do projeto (`~/.config/gspread/`) |
| Dados dos alunos | ✅ Local | CSV gerado em runtime, fora do controle de versão |
| Acesso ao painel professor | ✅ Controlado | Verificação por `PROFESSOR_USUARIOS` em `config.py` |

> Para ambientes de produção com muitos usuários, recomenda-se implementar hash de senhas (bcrypt) e autenticação via banco de dados.

---

## 🧪 Testes

O projeto possui **26 testes automatizados** cobrindo a lógica de negócio:

```bash
# Instalar pytest (apenas uma vez)
pip install pytest

# Executar todos os testes
pytest tests/ -v
```

### Cobertura dos testes

| Módulo | Testes | O que é testado |
|---|---|---|
| `quiz_service` | 18 | Verificação de resposta, cálculo de nota, embaralhamento |
| `auth_service` | 8 | Login válido, senha errada, usuário inexistente, arquivo ausente |

---

## 📦 Deploy no Streamlit Cloud

1. Faça fork ou clone deste repositório para sua conta GitHub
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte com sua conta GitHub → selecione este repositório
4. **Main file path:** `app.py`
5. Em **Secrets**, adicione os usuários em formato TOML:
   ```toml
   # .streamlit/secrets.toml (não commitar!)
   [alunos]
   professor = "senha"
   aluno1 = "senha"
   ```
6. Adapte `auth_service.py` para ler de `st.secrets` em vez do JSON

---

## 📚 Sobre o Scrum

As 20 questões do quiz cobrem os principais conceitos do **Scrum Guide**:

- Valores e princípios do Scrum
- Papéis: Product Owner, Scrum Master, Time de Desenvolvimento
- Eventos: Sprint, Daily, Planning, Review, Retrospective
- Artefatos: Product Backlog, Sprint Backlog, Incremento
- Definition of Done e Sprint Goal

---

## 👨‍💻 Autor

<div align="center">

**Cláudio Ferreira Neves**

Especialista em Business Intelligence · Data Science · Data Engineer e AI

[![GitHub](https://img.shields.io/badge/GitHub-cfneves-181717?style=flat&logo=github)](https://github.com/cfneves)

*SENAI/SC — CentroWEG*

</div>

---

## 📄 Licença

Distribuído sob a licença MIT. Consulte [LICENSE](LICENSE) para mais informações.

---

<div align="center">

Feito com ❤️ usando **Python** · **Streamlit** · **Pandas** · **Plotly**

</div>
