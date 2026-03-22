import gspread
import streamlit as st
import pandas as pd
from datetime import datetime
from google.oauth2.service_account import Credentials
from config import GSPREAD_CREDENTIALS, GSPREAD_TOKEN, SHEETS_NAME, PONTOS_POR_ACERTO, NOTA_APROVACAO

_SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


@st.cache_resource
def _get_client() -> gspread.Client:
    # Cloud: use service account from st.secrets
    try:
        if "gcp_service_account" in st.secrets:
            creds = Credentials.from_service_account_info(
                dict(st.secrets["gcp_service_account"]), scopes=_SCOPES
            )
            return gspread.authorize(creds)
    except Exception:
        pass

    # Local: use OAuth2 flow (requires browser-based consent once)
    return gspread.oauth(
        credentials_filename=str(GSPREAD_CREDENTIALS),
        authorized_user_filename=str(GSPREAD_TOKEN),
    )


def enviar_respostas(usuario: str, respostas: list[dict]) -> bool:
    """Sincroniza para Google Sheets. Falha silenciosa — CSV é o armazenamento primário."""
    try:
        aba = _get_client().open(SHEETS_NAME).sheet1
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        linhas = [
            [usuario, i, r["resposta"], "Sim" if r["correta"] else "Não", data_hora]
            for i, r in enumerate(respostas, start=1)
        ]
        aba.append_rows(linhas)
        return True
    except Exception:
        return False


@st.cache_data(ttl=60)
def ler_resultados() -> pd.DataFrame:
    """Lê todos os resultados do Google Sheets e retorna DataFrame agregado por aluno.

    Cache de 60s para evitar sobrecarga na API em rerenders do Streamlit.
    Colunas do DataFrame: usuario, acertos, total, erros, nota, percentual, aprovado.
    """
    try:
        aba = _get_client().open(SHEETS_NAME).sheet1
        linhas = aba.get_all_values()
        if not linhas:
            return pd.DataFrame()

        df = pd.DataFrame(linhas, columns=["usuario", "questao", "resposta", "correta", "data_hora"])
        df["correta"] = df["correta"].str.strip() == "Sim"

        resumo = (
            df.groupby("usuario")
            .agg(
                total=("correta", "count"),
                acertos=("correta", "sum"),
            )
            .reset_index()
        )
        resumo["erros"] = resumo["total"] - resumo["acertos"]
        resumo["nota"] = (resumo["acertos"] * PONTOS_POR_ACERTO).round(1)
        resumo["percentual"] = ((resumo["acertos"] / resumo["total"]) * 100).round(1)
        resumo["aprovado"] = resumo["nota"] >= NOTA_APROVACAO
        resumo["status"] = resumo["aprovado"].map({True: "✅ Aprovado", False: "❌ Reprovado"})

        return resumo.sort_values("nota", ascending=False).reset_index(drop=True)

    except Exception:
        return pd.DataFrame()
