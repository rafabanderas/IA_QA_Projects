# Importa FastAPI e TestClient para testar a API
from fastapi.testclient import TestClient
from api.main import app  # Importa a app FastAPI criada

# Cria um cliente de teste
client = TestClient(app)


def test_healthcheck():
    """
    Testa se o endpoint /healthcheck responde corretamente.
    """
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "API funcionando corretamente 🚀"}


def test_gerar_casos_endpoint():
    """
    Testa o endpoint /gerar-casos passando 'Login' como cenario.
    """
    response = client.get("/gerar-casos?cenario=Login")
    assert response.status_code == 200
    assert "result" in response.json()
    assert isinstance(response.json()["result"], list)
