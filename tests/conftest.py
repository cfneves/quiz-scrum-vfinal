"""
Configura mocks globais antes de qualquer import do projeto.
O Streamlit usa decoradores (@st.cache_data) avaliados em tempo de import,
então o mock deve ser instalado antes que qualquer módulo do projeto seja carregado.
"""
import sys
from unittest.mock import MagicMock

# Suporta @st.cache_data (sem args) e @st.cache_data(ttl=60) (com kwargs)
def _cache_data_mock(func=None, **kwargs):
    if func is not None:
        return func          # @st.cache_data → decorador direto
    return lambda f: f       # @st.cache_data(ttl=60) → retorna decorador

_st_mock = MagicMock()
_st_mock.cache_data = _cache_data_mock
_st_mock.cache_resource = lambda f: f
_st_mock.error = MagicMock()
_st_mock.warning = MagicMock()
_st_mock.stop = MagicMock()

sys.modules["streamlit"] = _st_mock
