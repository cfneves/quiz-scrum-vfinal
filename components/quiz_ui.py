import streamlit as st
from perguntas import carregar_perguntas
from services.quiz_service import verificar_resposta, embaralhar_perguntas
from services import storage_service
from components.results_ui import render as render_results
from components.signature import render as render_signature
from config import SESSION_DEFAULTS


def _render_sidebar(total: int) -> None:
    with st.sidebar:
        st.markdown(f"""
        <div style="padding: 1.5rem 0 1rem; text-align:center;">
            <div style="width:52px; height:52px; border-radius:50%;
                        background:linear-gradient(135deg,#00BFFF,#0080FF);
                        display:flex; align-items:center; justify-content:center;
                        margin:0 auto 0.7rem; font-size:1.4rem;">
                👤
            </div>
            <div style="font-size:0.8em; color:#888; word-break:break-all; line-height:1.4;">
                {st.session_state.usuario}
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        respondidas = st.session_state.index
        st.markdown(f"""
        <div style="font-size:0.8em; color:#888; text-align:center; margin-bottom:0.5rem;">
            Progresso: <b style="color:#00BFFF;">{respondidas}/{total}</b> perguntas
        </div>
        """, unsafe_allow_html=True)
        st.progress(respondidas / total if total > 0 else 0)

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🚪 Sair", use_container_width=True):
            for k, v in SESSION_DEFAULTS.items():
                st.session_state[k] = v
            st.rerun()


def render() -> None:
    # Inicializa embaralhamento na primeira renderização do quiz
    if not st.session_state.perguntas_embaralhadas:
        st.session_state.perguntas_embaralhadas = embaralhar_perguntas(
            carregar_perguntas(),
            st.session_state.usuario,
        )

    perguntas = st.session_state.perguntas_embaralhadas
    total = len(perguntas)
    idx = st.session_state.index

    _render_sidebar(total)

    if idx < total:
        _render_questao(perguntas, idx, total)
    elif not st.session_state.quiz_finalizado:
        _render_confirmacao_envio()
    else:
        render_results()
        render_signature()


def _render_questao(perguntas: list, idx: int, total: int) -> None:
    pergunta = perguntas[idx]
    progresso = idx / total

    st.markdown(f"""
    <div style="display:flex; justify-content:space-between; align-items:center;
                margin-bottom:0.6rem;">
        <span style="color:#888; font-size:0.85em; font-weight:500;">
            Pergunta {idx + 1} de {total}
        </span>
        <span style="background:rgba(0,191,255,0.1); color:#00BFFF;
                     border-radius:99px; padding:0.15rem 0.7rem;
                     font-size:0.8em; font-weight:600;">
            {round(progresso * 100)}%
        </span>
    </div>
    """, unsafe_allow_html=True)

    st.progress(progresso)

    st.markdown(f"""
    <div style="background:rgba(0,191,255,0.04); border:1px solid rgba(0,191,255,0.15);
                border-radius:14px; padding:1.3rem 1.5rem; margin:1rem 0 1.2rem;">
        <p style="font-size:1.05rem; font-weight:500; margin:0; line-height:1.6;
                  color:#E8E8E8;">
            {pergunta['pergunta']}
        </p>
    </div>
    """, unsafe_allow_html=True)

    escolha = st.radio(
        "Selecione uma opção:",
        pergunta["opcoes"],
        key=f"escolha_{idx}",
        label_visibility="collapsed",
    )

    if st.button("Próxima →", use_container_width=True):
        indice = pergunta["opcoes"].index(escolha)
        st.session_state.respostas.append({
            "resposta": escolha,
            "correta": verificar_resposta(pergunta, indice),
        })
        st.session_state.index += 1
        st.rerun()


def _render_confirmacao_envio() -> None:
    st.markdown("""
    <div style="text-align:center; padding: 2rem 1rem;">
        <div style="font-size:3rem; margin-bottom:0.8rem;">🎉</div>
        <h2 style="margin:0; color:#50fa7b;">Todas as perguntas respondidas!</h2>
        <p style="color:#888; margin:0.6rem 0 1.5rem;">
            Clique em <b>Enviar</b> para registrar seu resultado.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("📤 Enviar Respostas", use_container_width=True):
        with st.spinner("Salvando resultados..."):
            sucesso = storage_service.salvar_respostas(
                st.session_state.usuario,
                st.session_state.respostas,
            )
            # Sincronização opcional com Google Sheets (falha em silêncio)
            if sucesso:
                try:
                    from services.sheets_service import enviar_respostas
                    enviar_respostas(st.session_state.usuario, st.session_state.respostas)
                except Exception:
                    pass

        if sucesso:
            st.session_state.quiz_finalizado = True
            st.rerun()
        else:
            st.error("❌ Erro ao salvar respostas. Tente novamente.")
