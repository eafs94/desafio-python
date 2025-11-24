from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.documentos_router import router as documentos_router
from app.utils.logger import get_logger


logger = get_logger()
logger.info("Iniciando aplicacao FastAPI...")

Base.metadata.create_all(bind=engine)
logger.info("Tabelas verificadas/criadas com sucesso.")

# Instancia principal da aplicacao
app = FastAPI(
    title="Desafio Tecnico DBServer - Documentos",
    version="1.0.0",
    description="Microsservico para criacao e busca de documentos por palavra-chave."
)

logger.info("Carregando rotas...")
app.include_router(documentos_router)
logger.info("Rotas de documentos carregadas.")

@app.get("/")
def root():
    logger.info("Rota raiz '/' acessada.")
    return {
        "message": "API do Desafio Python da DBServer esta no ar!",
        "status": "online"
    }
