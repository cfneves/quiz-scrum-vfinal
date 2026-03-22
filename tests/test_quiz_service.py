import pytest
from services.quiz_service import (
    verificar_resposta,
    calcular_resultado,
    embaralhar_perguntas,
)


# ── Fixtures ────────────────────────────────────────────────────────────────

def _pergunta(resposta_correta: int = 0) -> dict:
    return {
        "pergunta": "Pergunta de teste?",
        "opcoes": ["A", "B", "C", "D"],
        "resposta_correta": resposta_correta,
        "explicacao": "Explicação.",
    }


def _respostas(acertos: int, total: int) -> list[dict]:
    return (
        [{"correta": True}] * acertos
        + [{"correta": False}] * (total - acertos)
    )


# ── verificar_resposta ───────────────────────────────────────────────────────

class TestVerificarResposta:
    def test_resposta_correta(self):
        assert verificar_resposta(_pergunta(2), 2) is True

    def test_resposta_incorreta(self):
        assert verificar_resposta(_pergunta(2), 0) is False

    def test_primeira_opcao_correta(self):
        assert verificar_resposta(_pergunta(0), 0) is True

    def test_ultima_opcao_correta(self):
        assert verificar_resposta(_pergunta(3), 3) is True

    def test_opcao_errada_quando_ultima_e_correta(self):
        assert verificar_resposta(_pergunta(3), 2) is False


# ── calcular_resultado ───────────────────────────────────────────────────────

class TestCalcularResultado:
    def test_tudo_certo_20_questoes(self):
        r = calcular_resultado(_respostas(20, 20))
        assert r["acertos"] == 20
        assert r["erros"] == 0
        assert r["nota"] == 10.0
        assert r["percentual"] == 100.0
        assert r["aprovado"] is True

    def test_tudo_errado(self):
        r = calcular_resultado(_respostas(0, 20))
        assert r["acertos"] == 0
        assert r["nota"] == 0.0
        assert r["percentual"] == 0.0
        assert r["aprovado"] is False

    def test_metade_certa(self):
        r = calcular_resultado(_respostas(10, 20))
        assert r["acertos"] == 10
        assert r["erros"] == 10
        assert r["nota"] == 5.0
        assert r["percentual"] == 50.0
        assert r["aprovado"] is False

    def test_aprovacao_no_limiar_exato(self):
        # 14 acertos × 0.5 = nota 7.0 → aprovado
        r = calcular_resultado(_respostas(14, 20))
        assert r["nota"] == 7.0
        assert r["aprovado"] is True

    def test_reprovacao_abaixo_do_limiar(self):
        # 13 acertos × 0.5 = nota 6.5 → reprovado
        r = calcular_resultado(_respostas(13, 20))
        assert r["nota"] == 6.5
        assert r["aprovado"] is False

    def test_total_correto(self):
        r = calcular_resultado(_respostas(8, 20))
        assert r["total"] == 20
        assert r["acertos"] + r["erros"] == r["total"]

    def test_percentual_arredondado(self):
        # 7 de 20 = 35%
        r = calcular_resultado(_respostas(7, 20))
        assert r["percentual"] == 35.0


# ── embaralhar_perguntas ─────────────────────────────────────────────────────

class TestEmbaralharPerguntas:
    @pytest.fixture
    def banco(self):
        return [_pergunta(i % 4) for i in range(20)]

    def test_mesmo_seed_mesma_ordem(self, banco):
        a = embaralhar_perguntas(banco, "claudio")
        b = embaralhar_perguntas(banco, "claudio")
        assert [p["resposta_correta"] for p in a] == [p["resposta_correta"] for p in b]

    def test_seeds_diferentes_ordens_diferentes(self, banco):
        a = embaralhar_perguntas(banco, "claudio")
        b = embaralhar_perguntas(banco, "aluno_xyz_diferente")
        assert [p["resposta_correta"] for p in a] != [p["resposta_correta"] for p in b]

    def test_nao_modifica_lista_original(self, banco):
        originais = [p["resposta_correta"] for p in banco]
        embaralhar_perguntas(banco, "qualquer")
        assert [p["resposta_correta"] for p in banco] == originais

    def test_retorna_mesma_quantidade(self, banco):
        resultado = embaralhar_perguntas(banco, "teste")
        assert len(resultado) == len(banco)

    def test_retorna_mesmos_elementos(self, banco):
        resultado = embaralhar_perguntas(banco, "teste")
        assert sorted(p["resposta_correta"] for p in resultado) == sorted(
            p["resposta_correta"] for p in banco
        )

    def test_seed_vazio_nao_quebra(self, banco):
        resultado = embaralhar_perguntas(banco, "")
        assert len(resultado) == len(banco)
