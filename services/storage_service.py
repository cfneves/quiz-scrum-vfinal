"""Armazenamento local em CSV — fonte primária de dados (sem dependências externas)."""

import csv
import pandas as pd
from pathlib import Path
from datetime import datetime
from config import BASE_DIR, PONTOS_POR_ACERTO, NOTA_APROVACAO

RESPOSTAS_FILE = BASE_DIR / "data" / "respostas.csv"
_COLUMNS = ["usuario", "questao", "resposta", "correta", "data_hora"]


def salvar_respostas(usuario: str, respostas: list[dict]) -> bool:
    try:
        RESPOSTAS_FILE.parent.mkdir(exist_ok=True)
        escrever_header = not RESPOSTAS_FILE.exists() or RESPOSTAS_FILE.stat().st_size == 0
        data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        linhas = [
            [usuario, i, r["resposta"], "Sim" if r["correta"] else "Não", data_hora]
            for i, r in enumerate(respostas, start=1)
        ]
        with open(RESPOSTAS_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            if escrever_header:
                writer.writerow(_COLUMNS)
            writer.writerows(linhas)
        return True
    except Exception:
        return False


def ler_resultados() -> pd.DataFrame:
    """Retorna resultados agregados (última submissão por aluno)."""
    if not RESPOSTAS_FILE.exists() or RESPOSTAS_FILE.stat().st_size == 0:
        return pd.DataFrame()

    df = pd.read_csv(RESPOSTAS_FILE, encoding="utf-8")
    if df.empty:
        return pd.DataFrame()

    df["correta_bool"] = df["correta"].str.strip() == "Sim"
    df["data_hora_dt"] = pd.to_datetime(
        df["data_hora"], format="%d/%m/%Y %H:%M:%S", errors="coerce"
    )

    # Mantém apenas a submissão mais recente por aluno
    mais_recente = df.groupby("usuario")["data_hora_dt"].transform("max")
    df_latest = df[df["data_hora_dt"] == mais_recente].copy()

    resumo = (
        df_latest.groupby("usuario")
        .agg(total=("correta_bool", "count"), acertos=("correta_bool", "sum"))
        .reset_index()
    )
    resumo["erros"] = resumo["total"] - resumo["acertos"]
    resumo["nota"] = (resumo["acertos"] * PONTOS_POR_ACERTO).round(1)
    resumo["percentual"] = ((resumo["acertos"] / resumo["total"]) * 100).round(1)
    resumo["aprovado"] = resumo["nota"] >= NOTA_APROVACAO
    resumo["status"] = resumo["aprovado"].map({True: "✅ Aprovado", False: "❌ Reprovado"})

    return resumo.sort_values("nota", ascending=False).reset_index(drop=True)
