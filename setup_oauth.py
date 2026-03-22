"""
Verificação e configuração do OAuth2 para Google Sheets.
Execute uma vez antes de rodar a aplicação:

    python setup_oauth.py
"""

import sys
from pathlib import Path

CREDENTIALS_PATH = Path.home() / ".config" / "gspread" / "credentials.json"
TOKEN_PATH = Path.home() / ".config" / "gspread" / "authorized_user.json"
SHEETS_NAME = "RespostasAlunos"


def _check(label: str, ok: bool, detalhe: str = "") -> bool:
    status = "✅" if ok else "❌"
    print(f"  {status}  {label}")
    if not ok and detalhe:
        print(f"       {detalhe}")
    return ok


def verificar():
    print("\n╔══════════════════════════════════════════════╗")
    print("║   Setup OAuth2 — Quiz Scrum / Google Sheets  ║")
    print("╚══════════════════════════════════════════════╝\n")

    # 1. Pasta de configuração
    pasta = CREDENTIALS_PATH.parent
    if not pasta.exists():
        pasta.mkdir(parents=True)
        print(f"  📁  Pasta criada: {pasta}\n")
    else:
        print(f"  📁  Pasta: {pasta}\n")

    print("── Verificando arquivos ──────────────────────────")

    ok_cred = _check(
        f"credentials.json  →  {CREDENTIALS_PATH}",
        CREDENTIALS_PATH.exists(),
        "Baixe o arquivo OAuth2 do Google Cloud Console e salve nesse caminho.\n"
        "       Passos: console.cloud.google.com → APIs & Services\n"
        "               → Credentials → Create Credentials\n"
        "               → OAuth 2.0 Client ID → Desktop App → Download JSON",
    )

    ok_token = _check(
        f"authorized_user.json  →  {TOKEN_PATH}",
        TOKEN_PATH.exists(),
        "Será gerado automaticamente na primeira execução do app.",
    )

    if not ok_cred:
        print("\n⚠️  Configure as credenciais e execute novamente.\n")
        return False

    print("\n── Testando conexão ──────────────────────────────")

    try:
        import gspread

        gc = gspread.oauth(
            credentials_filename=str(CREDENTIALS_PATH),
            authorized_user_filename=str(TOKEN_PATH),
        )
        _check("Autenticação OAuth2", True)

        planilha = gc.open(SHEETS_NAME)
        _check(f"Planilha '{SHEETS_NAME}' acessível", True)

        aba = planilha.sheet1
        linhas = len(aba.get_all_values())
        _check(f"Registros existentes na aba", True, f"{linhas} linhas encontradas")

        print("\n🎉  Tudo configurado! Execute: streamlit run app.py\n")
        return True

    except gspread.exceptions.SpreadsheetNotFound:
        _check(f"Planilha '{SHEETS_NAME}' acessível", False,
               f"Crie a planilha '{SHEETS_NAME}' no Google Sheets e compartilhe "
               "com a conta autorizada.")
        return False

    except Exception as e:
        _check("Conexão Google Sheets", False, str(e))
        return False


if __name__ == "__main__":
    ok = verificar()
    sys.exit(0 if ok else 1)
