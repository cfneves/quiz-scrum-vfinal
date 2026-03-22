import json
import streamlit as st
from config import ALUNOS_FILE


def _carregar_usuarios() -> dict:
    # Cloud: use st.secrets["alunos"] when alunos.json is absent (gitignored)
    try:
        if "alunos" in st.secrets:
            return dict(st.secrets["alunos"])
    except Exception:
        pass

    with open(ALUNOS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)["alunos"]


def autenticar(username: str, senha: str) -> bool:
    try:
        usuarios = _carregar_usuarios()
        return username in usuarios and usuarios[username] == senha
    except FileNotFoundError:
        st.error(f"❌ Arquivo de usuários não encontrado em: {ALUNOS_FILE}")
        return False
    except Exception as e:
        st.error(f"❌ Erro ao validar login: {e}")
        return False
