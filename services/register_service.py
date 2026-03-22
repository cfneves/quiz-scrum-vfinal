"""Cadastro de novos alunos.

Local  → grava em alunos.json
Cloud  → grava na aba "Usuarios" da planilha RespostasAlunos (Google Sheets)
"""

import json
import re
import streamlit as st
from config import ALUNOS_FILE, SHEETS_NAME

_SHEET_TAB = "Usuarios"


# ── Detecção de ambiente ────────────────────────────────────────────────────

def _is_cloud() -> bool:
    try:
        return "gcp_service_account" in st.secrets
    except Exception:
        return False


# ── API pública ─────────────────────────────────────────────────────────────

def registrar(email: str, senha: str) -> tuple[bool, str]:
    """Registra novo aluno. Retorna (sucesso, mensagem_erro)."""
    email = email.strip().lower()

    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
        return False, "E-mail inválido."
    if len(senha) < 4:
        return False, "A senha deve ter pelo menos 4 caracteres."
    if _usuario_existe(email):
        return False, "Este e-mail já está cadastrado."

    if _is_cloud():
        return _registrar_sheets(email, senha)
    return _registrar_local(email, senha)


def carregar_registrados_sheets() -> dict:
    """Retorna {email: senha} dos alunos registrados via Sheets (cloud)."""
    try:
        from services.sheets_service import _get_client
        aba = _get_client().open(SHEETS_NAME).worksheet(_SHEET_TAB)
        rows = aba.get_all_values()
        return {r[0].lower(): r[1] for r in rows[1:] if len(r) >= 2}
    except Exception:
        return {}


# ── Helpers internos ────────────────────────────────────────────────────────

def _usuario_existe(email: str) -> bool:
    from services.auth_service import _carregar_usuarios
    return email in {k.lower() for k in _carregar_usuarios()}


def _registrar_local(email: str, senha: str) -> tuple[bool, str]:
    try:
        if ALUNOS_FILE.exists():
            with open(ALUNOS_FILE, "r", encoding="utf-8") as f:
                dados = json.load(f)
        else:
            dados = {"alunos": {}}

        dados["alunos"][email] = senha

        with open(ALUNOS_FILE, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)

        return True, ""
    except Exception as e:
        return False, f"Erro ao salvar: {e}"


def _registrar_sheets(email: str, senha: str) -> tuple[bool, str]:
    try:
        from services.sheets_service import _get_client
        planilha = _get_client().open(SHEETS_NAME)
        try:
            aba = planilha.worksheet(_SHEET_TAB)
        except Exception:
            aba = planilha.add_worksheet(_SHEET_TAB, rows=1000, cols=2)
            aba.append_row(["email", "senha"])

        aba.append_row([email, senha])
        return True, ""
    except Exception as e:
        return False, f"Erro ao registrar: {e}"
