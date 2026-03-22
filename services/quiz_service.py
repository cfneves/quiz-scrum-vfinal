import random
from config import PONTOS_POR_ACERTO, NOTA_APROVACAO


def verificar_resposta(pergunta: dict, indice_escolha: int) -> bool:
    return indice_escolha == pergunta["resposta_correta"]


def calcular_resultado(respostas: list[dict]) -> dict:
    total = len(respostas)
    acertos = sum(1 for r in respostas if r["correta"])
    erros = total - acertos
    nota = round(acertos * PONTOS_POR_ACERTO, 1)
    percentual = round((acertos / total) * 100, 1) if total > 0 else 0.0
    aprovado = nota >= NOTA_APROVACAO
    return {
        "total": total,
        "acertos": acertos,
        "erros": erros,
        "nota": nota,
        "percentual": percentual,
        "aprovado": aprovado,
    }


def embaralhar_perguntas(perguntas: list[dict], seed: str) -> list[dict]:
    """Embaralha perguntas de forma determinística por usuário.

    O mesmo `seed` (username) sempre produz a mesma ordem, garantindo
    consistência entre rerenders. Seeds diferentes produzem ordens diferentes.
    A lista original (possivelmente cacheada) nunca é modificada.
    """
    copia = list(perguntas)
    random.Random(seed).shuffle(copia)
    return copia
