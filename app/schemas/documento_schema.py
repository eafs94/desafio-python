from pydantic import BaseModel
from datetime import date


class DocumentoCreate(BaseModel):
    titulo: str
    autor: str
    conteudo: str
    data: date
    latitude: float
    longitude: float


class DocumentoResponse(BaseModel):
    id: int
    titulo: str
    autor: str
    conteudo: str
    data: date
    latitude: float
    longitude: float

    class Config:
        from_attributes = True  # Permite retornar objetos ORM do SQLAlchemy
