from src.gerador_casos_teste.gerar_casos import gerar_casos

def test_gerar_casos():
    resultado = gerar_casos("Login")
    assert "Login - Fluxo Principal" in resultado
    assert len(resultado) == 4
