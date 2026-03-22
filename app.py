import streamlit as st
from config import APP_TITLE, APP_ICON, SESSION_DEFAULTS, PROFESSOR_USUARIOS
from components.styles import PREMIUM_CSS
from components import landing_ui, login_ui, quiz_ui, professor_ui, register_ui

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="auto",
)

st.markdown(PREMIUM_CSS, unsafe_allow_html=True)

for _k, _v in SESSION_DEFAULTS.items():
    if _k not in st.session_state:
        st.session_state[_k] = _v

# ── Roteamento principal ──────────────────────────────────────────────────────

if not st.session_state.autenticado:
    if st.session_state.get("cadastrando"):
        _, col, _ = st.columns([1, 2, 1])
        with col:
            register_ui.render()
    elif st.session_state.role is None:
        _, col, _ = st.columns([1, 2, 1])
        with col:
            landing_ui.render()
    else:
        _, col, _ = st.columns([1, 2, 1])
        with col:
            login_ui.render()
        if st.session_state.autenticado:
            st.rerun()

else:
    role = st.session_state.role
    usuario = st.session_state.usuario

    if role == "professor":
        if usuario not in PROFESSOR_USUARIOS:
            _, col, _ = st.columns([1, 2, 1])
            with col:
                st.error("🚫 Usuário não autorizado como professor.")
                if st.button("← Voltar ao início"):
                    for k, v in SESSION_DEFAULTS.items():
                        st.session_state[k] = v
                    st.rerun()
        else:
            professor_ui.render()
    else:
        _, col, _ = st.columns([1, 2, 1])
        with col:
            quiz_ui.render()
