import streamlit as st
import pandas as pd
import plotly.express as px
from services.quiz_service import calcular_resultado
from services import storage_service


def render() -> None:
    respostas = st.session_state.respostas
    perguntas = st.session_state.perguntas_embaralhadas

    if not perguntas:
        st.warning("⚠️ Sessão expirada. Faça login novamente.")
        st.stop()
    r = calcular_resultado(respostas)

    # Banner de resultado
    icone = "🏆" if r["aprovado"] else "📊"
    cor_badge = "#50fa7b" if r["aprovado"] else "#FFB86C"
    status_texto = "Aprovado" if r["aprovado"] else "Abaixo da média"

    st.markdown(f"""
    <div style="text-align:center; padding: 1.5rem 0 1rem;">
        <div style="font-size:3rem; margin-bottom:0.4rem;">{icone}</div>
        <h2 style="margin:0; font-size:1.6rem;
                   background: linear-gradient(90deg, #00BFFF, #0080FF);
                   -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
            Resultado Final
        </h2>
        <span style="display:inline-block; background:{cor_badge}22; color:{cor_badge};
                     border:1px solid {cor_badge}55; border-radius:99px;
                     padding:0.2rem 1rem; font-size:0.85em; font-weight:600; margin-top:0.4rem;">
            {status_texto} &mdash; {r['percentual']}% de aproveitamento
        </span>
    </div>
    """, unsafe_allow_html=True)

    # Métricas
    col1, col2, col3 = st.columns(3)
    col1.metric("✅ Acertos", f"{r['acertos']} / {r['total']}")
    col2.metric("❌ Erros", f"{r['erros']} / {r['total']}")
    col3.metric("⭐ Nota", f"{r['nota']:.1f}")

    # Gráfico
    df = pd.DataFrame({
        "Categoria": ["Acertos", "Erros"],
        "Quantidade": [r["acertos"], r["erros"]],
    })
    fig = px.bar(
        df, x="Categoria", y="Quantidade",
        color="Categoria",
        color_discrete_map={"Acertos": "#00BFFF", "Erros": "#FF5555"},
        text="Quantidade",
    )
    fig.update_layout(
        showlegend=False,
        height=280,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font={"color": "#AAAAAA", "size": 13},
        margin=dict(t=10, b=10, l=0, r=0),
    )
    fig.update_traces(textposition="outside", marker_line_width=0)
    st.plotly_chart(fig, use_container_width=True)

    # Gabarito detalhado
    st.markdown("""
    <h3 style="margin-bottom:0.8rem; color:#E0E0E0;">📘 Gabarito</h3>
    """, unsafe_allow_html=True)

    for i, resposta in enumerate(respostas):
        if i >= len(perguntas):
            break
        p = perguntas[i]
        correta = resposta["correta"]
        icone_q = "✅" if correta else "❌"
        cor_borda = "rgba(80,250,123,0.25)" if correta else "rgba(255,85,85,0.25)"
        cor_status = "#50fa7b" if correta else "#FF5555"
        status = "Correto" if correta else "Incorreto"

        st.markdown(f"""
        <div style="background:rgba(255,255,255,0.025); border:1px solid {cor_borda};
                    border-radius:12px; padding:1rem 1.2rem; margin:0.5rem 0;
                    transition: border-color 0.2s;">
            <div style="font-weight:600; color:#E0E0E0; margin-bottom:0.5rem; line-height:1.4;">
                {icone_q} <span style="color:#888; font-size:0.85em;">#{i+1}</span>
                {p['pergunta']}
            </div>
            <div style="font-size:0.88em; line-height:1.7; color:#999;">
                📌 <b style="color:#ccc;">Sua resposta:</b> {resposta['resposta']}<br>
                ✅ <b style="color:#ccc;">Resposta correta:</b>
                    {p['opcoes'][p['resposta_correta']]}<br>
                <span style="color:{cor_status}; font-weight:600;">{status}</span>
                &nbsp;—&nbsp;
                📘 <span style="color:#888;">{p['explicacao']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    _render_ranking(st.session_state.usuario, r["nota"])


def _render_ranking(usuario_atual: str, nota_atual: float) -> None:
    df = storage_service.ler_resultados()
    if df.empty or len(df) < 1:
        return

    st.divider()
    st.markdown("""
    <h3 style="margin-bottom:0.5rem; color:#E0E0E0;">🏆 Ranking da Turma</h3>
    """, unsafe_allow_html=True)

    # Posição do aluno atual
    if usuario_atual in df["usuario"].values:
        posicao = df[df["usuario"] == usuario_atual].index[0] + 1
        total = len(df)
        emoji_pos = "🥇" if posicao == 1 else "🥈" if posicao == 2 else "🥉" if posicao == 3 else "🎯"
        st.markdown(f"""
        <div style="text-align:center; padding:0.8rem 0 1.2rem;">
            <span style="font-size:1.8rem;">{emoji_pos}</span>
            <span style="font-size:1.1rem; font-weight:600; color:#00BFFF; margin-left:0.5rem;">
                {posicao}º lugar
            </span>
            <span style="color:#888; font-size:0.9rem;"> entre {total} aluno{"s" if total > 1 else ""}</span>
        </div>
        """, unsafe_allow_html=True)

    if len(df) < 2:
        st.info("📭 Aguardando mais respostas da turma para exibir o ranking completo.")
        return

    # Prepara dados para o gráfico
    df_plot = df.copy()
    df_plot["destaque"] = df_plot["usuario"].apply(
        lambda u: "Você" if u == usuario_atual else "Turma"
    )
    # Exibe nome curto (antes do @)
    df_plot["nome"] = df_plot["usuario"].apply(lambda u: u.split("@")[0])
    df_plot = df_plot.sort_values("nota", ascending=True)

    fig = px.bar(
        df_plot,
        x="nota",
        y="nome",
        orientation="h",
        color="destaque",
        color_discrete_map={"Você": "#00BFFF", "Turma": "#444"},
        text="nota",
        hover_data={"destaque": False, "nome": True, "nota": True},
    )
    fig.update_layout(
        showlegend=True,
        legend=dict(
            orientation="h", yanchor="bottom", y=1.02,
            font=dict(color="#AAAAAA"),
        ),
        height=max(260, len(df_plot) * 36),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font={"color": "#AAAAAA"},
        margin=dict(t=30, b=10, l=0, r=40),
        xaxis=dict(range=[0, 10], gridcolor="rgba(255,255,255,0.05)", title="Nota"),
        yaxis=dict(gridcolor="rgba(0,0,0,0)", title=""),
    )
    fig.update_traces(textposition="outside", marker_line_width=0)
    st.plotly_chart(fig, use_container_width=True)
