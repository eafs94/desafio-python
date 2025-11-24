from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.documento import Documento
from app.schemas.documento_schema import DocumentoCreate


class DocumentoRepository:

    @staticmethod
    def criar(db: Session, documento: DocumentoCreate) -> Documento:
        novo_documento = Documento(
            titulo=documento.titulo,
            autor=documento.autor,
            conteudo=documento.conteudo,
            data=documento.data
        )
        db.add(novo_documento)
        db.commit()
        db.refresh(novo_documento)
        return novo_documento


    @staticmethod
    def buscar_por_palavra_chave(db: Session, palavra: str) -> list[Documento]:
        # Busca case-insensitive usando LIKE
        stmt = select(Documento).where(
            Documento.conteudo.ilike(f"%{palavra}%")
        )
        resultados = db.scalars(stmt).all()
        return resultados
