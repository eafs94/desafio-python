from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.schemas.documento_schema import DocumentoCreate, DocumentoResponse
from app.repositories.documento_repository import DocumentoRepository


class DocumentoService:

    @staticmethod
    def criar_documento(db: Session, documento: DocumentoCreate) -> DocumentoResponse:
        if not documento.titulo.strip():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="O título do documento não pode ser vazio."
            )

        novo_doc = DocumentoRepository.criar(db, documento)
        return DocumentoResponse.model_validate(novo_doc)


    @staticmethod
    def buscar_por_palavra_chave(db: Session, palavra: str) -> list[DocumentoResponse]:
        palavra = palavra.strip()

        if not palavra:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A palavra-chave não pode ser vazia."
            )

        documentos = DocumentoRepository.buscar_por_palavra_chave(db, palavra)

        return [DocumentoResponse.model_validate(doc) for doc in documentos]
