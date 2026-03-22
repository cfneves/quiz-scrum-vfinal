import streamlit as st
from components.signature import render as render_signature


def render() -> None:
    st.markdown("""
    <div style="text-align:center; padding: 2.5rem 0 2rem;">
        <div style="font-size:4rem; margin-bottom:0.6rem;
                    filter:drop-shadow(0 0 24px rgba(0,191,255,0.5));">
            🏆
        </div>
        <h1 style="margin:0; font-size:2rem; font-weight:700;
                   background: linear-gradient(90deg, #00BFFF, #0080FF);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Quiz Scrum
        </h1>
        <p style="color:#888; margin:0.4rem 0 0; font-size:0.95rem;">
            Metodologias Ágeis com Versionamento
        </p>
        <p style="color:#555; font-size:0.82em; margin:0.2rem 0 0;">
            <i>Prof. Cláudio Ferreira Neves — SENAI/SC · CentroWEG</i>
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div style="background:rgba(0,191,255,0.04); border:1px solid rgba(0,191,255,0.2);
                    border-radius:16px; padding:1.8rem 1.5rem; text-align:center;
                    min-height:180px; display:flex; flex-direction:column;
                    align-items:center; justify-content:center; gap:0.6rem;">
            <div style="font-size:2.8rem;">🎓</div>
            <div style="font-size:1.1rem; font-weight:700; color:#E0E0E0;">Área do Aluno</div>
            <div style="font-size:0.85rem; color:#888; line-height:1.4;">
                Realize o quiz sobre Scrum<br>e veja seu desempenho
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Entrar como Aluno", use_container_width=True, key="btn_aluno"):
            st.session_state.role = "aluno"
            st.rerun()
        if st.button("📝 Cadastrar", use_container_width=True, key="btn_cadastrar_landing"):
            st.session_state.cadastrando = True
            st.rerun()

    with col2:
        st.markdown("""
        <div style="background:rgba(189,147,249,0.04); border:1px solid rgba(189,147,249,0.2);
                    border-radius:16px; padding:1.8rem 1.5rem; text-align:center;
                    min-height:180px; display:flex; flex-direction:column;
                    align-items:center; justify-content:center; gap:0.6rem;">
            <div style="font-size:2.8rem;">👨‍🏫</div>
            <div style="font-size:1.1rem; font-weight:700; color:#E0E0E0;">Área do Professor</div>
            <div style="font-size:0.85rem; color:#888; line-height:1.4;">
                Visualize o desempenho<br>e o ranking da turma
            </div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Entrar como Professor", use_container_width=True, key="btn_professor"):
            st.session_state.role = "professor"
            st.rerun()

    render_signature()
