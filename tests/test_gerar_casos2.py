from src.gerador_casos_teste.gerar_casos import gerar_casos

def test_gerar_casos_retorna_lista():
    resultado = gerar_casos("Login")
    assert isinstance(resultado, list)  # ✅ Verifica se o retorno é uma lista

def test_gerar_casos_contem_fluxo_principal():
    resultado = gerar_casos("Login")
    assert "Login - Fluxo Principal" in resultado  # ✅ Verifica se existe o caso de fluxo principal

def test_gerar_casos_comprimento_da_lista():
    resultado = gerar_casos("Login")
    assert len(resultado) == 4  # ✅ Verifica se a lista tem exatamente 4 casos
