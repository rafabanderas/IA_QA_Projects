# Importa a função que será testada
from gerador_casos_teste.gerar_casos import gerar_casos


def test_gerar_casos_contem_fluxo_principal():
    """
    Testa se a palavra 'Login - Fluxo Principal' está no resultado.
    """
    resultado = gerar_casos("Login")
    assert "Login - Fluxo Principal" in resultado


def test_gerar_casos_comprimento_da_lista():
    """
    Verifica se o gerador retorna exatamente 4 casos para 'Login'.
    """
    resultado = gerar_casos("Login")
    assert len(resultado) == 4
