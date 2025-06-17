# Importa o roteador do FastAPI
from fastapi import APIRouter

# Importa a função responsável por gerar os casos de teste
from gerador_casos_teste.gerar_casos import gerar_casos

# Cria uma instância do roteador da API
router = APIRouter()


@router.get("/gerar-casos")
def gerar(cenario: str):
    """
    Endpoint GET que gera casos de teste para um cenário informado via query.
    🔗 Exemplo: /gerar-casos?cenario=Login
    """
    return {"result": gerar_casos(cenario)}


@router.get("/healthcheck")
def healthcheck():
    """
    Endpoint simples para verificar se a API está no ar.
    🔗 Exemplo: /healthcheck
    """
    return {"status": "API funcionando corretamente 🚀"}
