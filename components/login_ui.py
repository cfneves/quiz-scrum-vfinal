import streamlit as st
from services.auth_service import autenticar
from components.signature import render as render_signature


def render() -> None:
    role = st.session_state.role
    is_professor = role == "professor"
    icone = "👨‍🏫" if is_professor else "🎓"
    titulo = "Área do Professor" if is_professor else "Área do Aluno"
    cor = "rgba(189,147,249,0.15)" if is_professor else "rgba(0,191,255,0.15)"
    cor_borda = "rgba(189,147,249,0.3)" if is_professor else "rgba(0,191,255,0.3)"

    # Botão voltar
    if st.button("← Voltar", key="btn_voltar"):
        st.session_state.role = None
        st.rerun()

    st.markdown(f"""
    <div style="text-align:center; padding: 1.5rem 0 1.2rem;">
        <div style="font-size:3rem; margin-bottom:0.5rem;">{icone}</div>
        <h2 style="margin:0; font-size:1.5rem; color:#E0E0E0;">{titulo}</h2>
        <p style="color:#666; font-size:0.82em; margin:0.3rem 0 0;">
            <i>Prof. Cláudio Ferreira Neves</i>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="background:{cor}; border:1px solid {cor_borda};
                border-radius:14px; padding:1.5rem; margin-bottom:0.5rem;">
    """, unsafe_allow_html=True)

    username = st.text_input("Usuário", placeholder="Digite seu usuário")
    senha = st.text_input("Senha", type="password", placeholder="Digite sua senha")

    if st.button("Entrar", use_container_width=True):
        if not username or not senha:
            st.warning("⚠️ Preencha usuário e senha.")
        elif autenticar(username, senha):
            st.session_state.usuario = username
            st.session_state.autenticado = True
            st.success("✅ Login realizado com sucesso.")
        else:
            st.error("❌ Usuário ou senha incorretos.")

    st.markdown("</div>", unsafe_allow_html=True)

    render_signature()
