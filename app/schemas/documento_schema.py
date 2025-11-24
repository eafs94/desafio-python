from pydantic import BaseModel
from datetime import date


class DocumentoCreate(BaseModel):
    titulo: str
    autor: str
    conteudo: str
    data: date


class DocumentoResponse(BaseModel):
    id: int
    titulo: str
    autor: str
    conteudo: str
    data: date

    class Config:
        from_attributes = True  # Permite retornar objetos ORM do SQLAlchemy
