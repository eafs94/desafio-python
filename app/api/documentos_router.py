from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.documento_schema import DocumentoCreate, DocumentoResponse
from app.services.documento_service import DocumentoService
from app.core.database import get_db


router = APIRouter(prefix="/documentos", tags=["Documentos"])


@router.post("/", response_model=DocumentoResponse, status_code=201)
def criar_documento(documento: DocumentoCreate, db: Session = Depends(get_db)):
    return DocumentoService.criar_documento(db, documento)


@router.get("/", response_model=list[DocumentoResponse])
def buscar_documentos(palavraChave: str, db: Session = Depends(get_db)):
    return DocumentoService.buscar_por_palavra_chave(db, palavraChave)
