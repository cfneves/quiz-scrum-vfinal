import streamlit as st
import plotly.express as px
from services import storage_service
from components.signature import render as render_signature
from config import SESSION_DEFAULTS, NOTA_APROVACAO


def _render_sidebar() -> None:
    with st.sidebar:
        st.markdown(f"""
        <div style="padding: 1.5rem 0 1rem; text-align:center;">
            <div style="width:52px; height:52px; border-radius:50%;
                        background:linear-gradient(135deg,#bd93f9,#8b5cf6);
                        display:flex; align-items:center; justify-content:center;
                        margin:0 auto 0.7rem; font-size:1.4rem;">
                👨‍🏫
            </div>
            <div style="font-size:0.8em; color:#888; word-break:break-all; line-height:1.4;">
                {st.session_state.usuario}
            </div>
            <div style="font-size:0.7em; color:#bd93f9; margin-top:0.3rem;">
                Painel do Professor
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.divider()

        if st.button("🔄 Atualizar dados", use_container_width=True):
            st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🚪 Sair", use_container_width=True):
            for k, v in SESSION_DEFAULTS.items():
                st.session_state[k] = v
            st.rerun()


def render() -> None:
    _render_sidebar()

    st.markdown("""
    <div style="padding: 1rem 0 0.5rem;">
        <h1 style="margin:0; font-size:1.8rem; font-weight:700;
                   background: linear-gradient(90deg, #bd93f9, #8b5cf6);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            📊 Painel do Professor
        </h1>
        <p style="color:#888; margin:0.3rem 0 0; font-size:0.9rem;">
            Desempenho e ranking da turma — Quiz Scrum
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    df = storage_service.ler_resultados()

    if df.empty:
        st.info("📭 Nenhum resultado encontrado ainda. Aguarde os alunos realizarem o quiz.")
        render_signature()
        return

    total_alunos = len(df)
    media_nota = df["nota"].mean()
    taxa_aprovacao = df["aprovado"].sum() / total_alunos * 100
    media_acertos = df["acertos"].mean()
    total_questoes = df["total"].iloc[0] if not df.empty else 20

    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👥 Alunos", total_alunos)
    col2.metric("⭐ Média", f"{media_nota:.1f}")
    col3.metric("✅ Aprovação", f"{taxa_aprovacao:.0f}%")
    col4.metric("🎯 Média acertos", f"{media_acertos:.1f}/{total_questoes}")

    st.markdown("<br>", unsafe_allow_html=True)

    # Gráficos
    col_g1, col_g2 = st.columns(2)

    with col_g1:
        st.markdown("#### 📊 Notas por Aluno")
        df_sorted = df.sort_values("nota", ascending=True).copy()
        df_sorted["nome"] = df_sorted["usuario"].apply(lambda u: u.split("@")[0])
        fig_notas = px.bar(
            df_sorted, x="nota", y="nome", orientation="h",
            text="nota",
            color="aprovado",
            color_discrete_map={True: "#50fa7b", False: "#FF5555"},
        )
        fig_notas.update_layout(
            showlegend=False,
            height=max(300, total_alunos * 32),
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font={"color": "#AAAAAA"},
            margin=dict(t=10, b=10, l=0, r=40),
            xaxis=dict(range=[0, 10], gridcolor="rgba(255,255,255,0.05)"),
            yaxis=dict(gridcolor="rgba(0,0,0,0)"),
        )
        fig_notas.add_vline(
            x=NOTA_APROVACAO, line_dash="dash",
            line_color="rgba(255,255,255,0.25)",
            annotation_text=f"Mínimo {NOTA_APROVACAO}",
            annotation_font_color="#666",
        )
        fig_notas.update_traces(textposition="outside")
        st.plotly_chart(fig_notas, use_container_width=True)

    with col_g2:
        st.markdown("#### 📈 Distribuição de Notas")
        fig_hist = px.histogram(
            df, x="nota", nbins=10,
            color_discrete_sequence=["#bd93f9"],
        )
        fig_hist.update_layout(
            showlegend=False, height=350,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            font={"color": "#AAAAAA"},
            margin=dict(t=10, b=10, l=0, r=0),
            bargap=0.05,
            xaxis=dict(range=[0, 10], gridcolor="rgba(255,255,255,0.05)"),
            yaxis=dict(gridcolor="rgba(255,255,255,0.05)", title="Nº de Alunos"),
        )
        fig_hist.add_vline(
            x=NOTA_APROVACAO, line_dash="dash",
            line_color="rgba(255,255,255,0.25)",
            annotation_text=f"Mínimo {NOTA_APROVACAO}",
            annotation_font_color="#666",
        )
        st.plotly_chart(fig_hist, use_container_width=True)

    # Ranking completo
    st.markdown("#### 🏆 Ranking da Turma")
    df_rank = df.copy()
    df_rank.insert(0, "#", range(1, len(df_rank) + 1))
    df_rank["nome"] = df_rank["usuario"].apply(lambda u: u.split("@")[0])
    tabela = df_rank[["#", "nome", "acertos", "erros", "nota", "percentual", "status"]].copy()
    tabela.columns = ["#", "Aluno", "Acertos", "Erros", "Nota", "% Aproveit.", "Status"]

    st.dataframe(
        tabela,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Nota": st.column_config.ProgressColumn(
                "Nota", min_value=0, max_value=10, format="%.1f"
            ),
            "% Aproveit.": st.column_config.ProgressColumn(
                "% Aproveit.", min_value=0, max_value=100, format="%.1f%%"
            ),
        },
    )

    csv = tabela.to_csv(index=False, sep=";", decimal=",").encode("utf-8")
    st.download_button(
        label="⬇️ Exportar CSV",
        data=csv,
        file_name="ranking_quiz_scrum.csv",
        mime="text/csv",
    )

    render_signature()
