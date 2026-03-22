import json
import streamlit as st
from config import ALUNOS_FILE


@st.cache_data
def _carregar_usuarios() -> dict:
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
