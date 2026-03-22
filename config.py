from pathlib import Path

BASE_DIR = Path(__file__).parent

# Arquivos de dados
ALUNOS_FILE = BASE_DIR / "alunos.json"

# Credenciais Google OAuth2 (fora do projeto — nunca commitar)
GSPREAD_CREDENTIALS = Path.home() / ".config" / "gspread" / "credentials.json"
GSPREAD_TOKEN = Path.home() / ".config" / "gspread" / "authorized_user.json"
SHEETS_NAME = "RespostasAlunos"

# Regras de negócio do quiz
PONTOS_POR_ACERTO = 0.5
NOTA_APROVACAO = 7.0

# Identidade da aplicação
APP_TITLE = "Quiz Scrum"
APP_ICON = "🏆"
APP_AUTHOR = "Cláudio Ferreira Neves"
APP_ROLE  = "Especialista em Business Intelligence, Big Data & Analytics - Ciência de Dados"
APP_ROLE2 = "Especialista em Ciência de Dados e Inteligência Artificial"
APP_ROLE3 = "MBA em Gestão de Projetos"
APP_INSTITUTION = "SENAI/SC - CentroWEG"

# Controle de acesso ao painel do professor
PROFESSOR_USUARIOS: list[str] = [
    "claudio",
    "claudio.neves@edu.sc.senai.br",
]

# Estado inicial da sessão
SESSION_DEFAULTS: dict = {
    "autenticado": False,
    "usuario": "",
    "role": None,              # 'aluno' | 'professor'
    "cadastrando": False,      # True quando tela de cadastro está aberta
    "index": 0,
    "respostas": [],
    "quiz_finalizado": False,
    "perguntas_embaralhadas": [],  # populado no início do quiz por usuario
}
