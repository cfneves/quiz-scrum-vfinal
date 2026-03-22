import json
import pytest
from pathlib import Path
from unittest.mock import patch

from services.auth_service import autenticar


# ── Fixture: alunos.json temporário ─────────────────────────────────────────

USUARIOS_MOCK = {
    "alunos": {
        "claudio": "60547979215",
        "aluno1": "senha123",
        "professor@senai.br": "prof2024",
    }
}


@pytest.fixture
def alunos_file(tmp_path) -> Path:
    """Cria um alunos.json temporário e aponta ALUNOS_FILE para ele."""
    arquivo = tmp_path / "alunos.json"
    arquivo.write_text(json.dumps(USUARIOS_MOCK), encoding="utf-8")
    return arquivo


# ── autenticar ───────────────────────────────────────────────────────────────

class TestAutenticar:
    def test_credenciais_validas(self, alunos_file):
        with patch("services.auth_service.ALUNOS_FILE", alunos_file):
            with patch("services.auth_service._carregar_usuarios",
                       return_value=USUARIOS_MOCK["alunos"]):
                assert autenticar("claudio", "60547979215") is True

    def test_senha_errada(self, alunos_file):
        with patch("services.auth_service._carregar_usuarios",
                   return_value=USUARIOS_MOCK["alunos"]):
            assert autenticar("claudio", "senha_errada") is False

    def test_usuario_inexistente(self, alunos_file):
        with patch("services.auth_service._carregar_usuarios",
                   return_value=USUARIOS_MOCK["alunos"]):
            assert autenticar("nao_existe", "qualquer") is False

    def test_usuario_email(self, alunos_file):
        with patch("services.auth_service._carregar_usuarios",
                   return_value=USUARIOS_MOCK["alunos"]):
            assert autenticar("professor@senai.br", "prof2024") is True

    def test_senha_case_sensitive(self, alunos_file):
        with patch("services.auth_service._carregar_usuarios",
                   return_value=USUARIOS_MOCK["alunos"]):
            assert autenticar("aluno1", "Senha123") is False  # maiúscula diferente

    def test_usuario_vazio(self, alunos_file):
        with patch("services.auth_service._carregar_usuarios",
                   return_value=USUARIOS_MOCK["alunos"]):
            assert autenticar("", "qualquer") is False

    def test_senha_vazia(self, alunos_file):
        with patch("services.auth_service._carregar_usuarios",
                   return_value=USUARIOS_MOCK["alunos"]):
            assert autenticar("claudio", "") is False

    def test_arquivo_nao_encontrado_retorna_false(self, tmp_path):
        caminho_inexistente = tmp_path / "nao_existe.json"
        with patch("services.auth_service.ALUNOS_FILE", caminho_inexistente):
            # Deve retornar False sem lançar exceção
            resultado = autenticar("claudio", "60547979215")
            assert resultado is False
