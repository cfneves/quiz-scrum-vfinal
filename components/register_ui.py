import streamlit as st
from services.register_service import registrar
from components.signature import render as render_signature


def render() -> None:
    st.markdown("""
    <div style="text-align:center; padding: 2rem 0 1.5rem;">
        <div style="font-size:3rem; margin-bottom:0.5rem;">📝</div>
        <h2 style="margin:0; font-size:1.6rem; font-weight:700;
                   background: linear-gradient(90deg, #00BFFF, #0080FF);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Cadastro de Aluno
        </h2>
        <p style="color:#888; margin:0.3rem 0 0; font-size:0.9rem;">
            Crie sua conta para acessar o Quiz Scrum
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Após cadastro bem-sucedido, mostra só a confirmação + botão de login
    if st.session_state.get("_cadastro_ok"):
        st.success("✅ Cadastrado com sucesso! Faça seu login.")
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🎓 Ir para o login", use_container_width=True, type="primary"):
            st.session_state._cadastro_ok = False
            st.session_state.cadastrando = False
            st.session_state.role = "aluno"
            st.rerun()
        render_signature()
        return

    # Formulário de cadastro
    st.markdown("""
    <div style="background:rgba(0,191,255,0.04); border:1px solid rgba(0,191,255,0.15);
                border-radius:16px; padding:2rem 1.5rem; margin-bottom:1rem;">
    """, unsafe_allow_html=True)

    email = st.text_input(
        "E-mail",
        placeholder="seu.email@exemplo.com",
        key="cadastro_email",
    )
    senha = st.text_input(
        "Senha",
        type="password",
        placeholder="Mínimo 4 caracteres",
        key="cadastro_senha",
    )
    confirmar = st.text_input(
        "Confirmar senha",
        type="password",
        placeholder="Repita a senha",
        key="cadastro_confirmar",
    )

    st.markdown("</div>", unsafe_allow_html=True)

    col_cadastrar, col_voltar = st.columns([2, 1])

    with col_cadastrar:
        if st.button("Cadastrar", use_container_width=True, type="primary", key="btn_cadastrar"):
            if not email or not senha or not confirmar:
                st.warning("Preencha todos os campos.")
            elif senha != confirmar:
                st.error("❌ As senhas não coincidem.")
            else:
                sucesso, erro = registrar(email, senha)
                if sucesso:
                    st.session_state._cadastro_ok = True
                    st.rerun()
                else:
                    st.error(f"❌ {erro}")

    with col_voltar:
        if st.button("← Voltar", use_container_width=True, key="btn_voltar_cadastro"):
            st.session_state.cadastrando = False
            st.rerun()

    render_signature()
