from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.documento import Documento
from app.schemas.documento_schema import DocumentoCreate
from app.utils.logger import get_logger


logger = get_logger()


class DocumentoRepository:

    @staticmethod
    def criar(db: Session, documento: DocumentoCreate) -> Documento:
        logger.info(f"Criando documento no repositorio: titulo='{documento.titulo}', autor='{documento.autor}'")
        novo_documento = Documento(
            titulo=documento.titulo,
            autor=documento.autor,
            conteudo=documento.conteudo,
            data=documento.data
        )
        db.add(novo_documento)
        db.commit()
        db.refresh(novo_documento)
        logger.info(f"Documento persistido com sucesso no banco: id={novo_documento.id}")

        return novo_documento


    @staticmethod
    def buscar_por_palavra_chave(db: Session, palavra: str) -> list[Documento]:
        logger.info(f"Executando busca no repositorio pela palavra-chave: '{palavra}'")
        stmt = select(Documento).where(
            Documento.titulo.ilike(f"{palavra} %") |
            Documento.titulo.ilike(f"% {palavra} %") |
            Documento.titulo.ilike(f"% {palavra}") |
            Documento.autor.ilike(f"{palavra} %") |
            Documento.autor.ilike(f"% {palavra} %") |
            Documento.autor.ilike(f"% {palavra}") |
            Documento.conteudo.ilike(f"{palavra} %") |
            Documento.conteudo.ilike(f"% {palavra} %") |
            Documento.conteudo.ilike(f"% {palavra}")
        )
        resultados = db.scalars(stmt).all()
        logger.info(f"Busca no repositorio retornou {len(resultados)} resultado(s) para palavra='{palavra}'")

        return resultados
