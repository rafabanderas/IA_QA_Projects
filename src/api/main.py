# Importa o FastAPI, que é o framework principal
from fastapi import FastAPI

# Importa o roteador que contém os endpoints (casos.py)
from api.routes import casos

# Instancia a aplicação FastAPI
app = FastAPI(
    title="IA QA Projects - Rafael Bandeira",  # Título que aparece na documentação
    description="API para geração de casos de teste utilizando IA aplicada a QA.",
    version="1.0.0"  # Versão da API
)

# Faz o registro das rotas no app
app.include_router(casos.router)
