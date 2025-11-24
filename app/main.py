from fastapi import FastAPI

# Instância principal da aplicação
app = FastAPI(
    title="Desafio Técnico DBServer - Documentos",
    version="1.0.0",
    description="Microsserviço para criação e busca de documentos por palavra-chave."
)

@app.get("/")
def root():
    return {
        "message": "API do Desafio Python da DBServer está no ar!",
        "status": "online"
    }
