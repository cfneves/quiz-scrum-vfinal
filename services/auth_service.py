import json
import streamlit as st
from config import ALUNOS_FILE


def _carregar_usuarios() -> dict:
    """Retorna todos os usuários válidos (pré-configurados + registrados)."""
    base = _carregar_base()
    registrados = _carregar_registrados()
    return {**registrados, **base}  # base tem prioridade em caso de conflito


def _carregar_base() -> dict:
    """Usuários pré-configurados: st.secrets (cloud) ou alunos.json (local)."""
    try:
        if "alunos" in st.secrets:
            return dict(st.secrets["alunos"])
    except Exception:
        pass

    try:
        with open(ALUNOS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)["alunos"]
    except FileNotFoundError:
        return {}
    except Exception:
        return {}


def _carregar_registrados() -> dict:
    """Alunos auto-cadastrados via tela de cadastro (cloud: Sheets, local: já em alunos.json)."""
    try:
        if "gcp_service_account" in st.secrets:
            from services.register_service import carregar_registrados_sheets
            return carregar_registrados_sheets()
    except Exception:
        pass
    return {}


def autenticar(username: str, senha: str) -> bool:
    try:
        usuarios = _carregar_usuarios()
        # Lookup case-insensitive
        usuarios_lower = {k.lower(): v for k, v in usuarios.items()}
        return usuarios_lower.get(username.lower()) == senha
    except Exception as e:
        st.error(f"❌ Erro ao validar login: {e}")
        return False
