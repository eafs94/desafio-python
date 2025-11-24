from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.schemas.documento_schema import DocumentoCreate, DocumentoResponse
from app.repositories.documento_repository import DocumentoRepository
from app.utils.logger import get_logger
from app.utils.distance import calcular_distancia


logger = get_logger()


class DocumentoService:

    @staticmethod
    def criar_documento(db: Session, documento: DocumentoCreate) -> DocumentoResponse:
        logger.info(f"[SERVICE] Iniciando criacao de documento: titulo='{documento.titulo}'")
        if not documento.titulo.strip():
            logger.warning("[SERVICE] Falha na criacao: titulo vazio")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="O titulo do documento nao pode ser vazio."
            )

        novo_doc = DocumentoRepository.criar(db, documento)
        logger.info(f"[SERVICE] Documento criado com sucesso: id={novo_doc.id}")

        return DocumentoResponse.model_validate(novo_doc)


    @staticmethod
    def buscar_por_palavra_chave(db: Session, palavra: str) -> list[DocumentoResponse]:
        logger.info(f"[SERVICE] Iniciando busca por palavra-chave: '{palavra}'")
        palavra = palavra.strip()

        if not palavra:
            logger.warning("[SERVICE] Falha na busca: palavra-chave vazia")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="A palavra-chave nao pode ser vazia."
            )

        documentos = DocumentoRepository.buscar_por_palavra_chave(db, palavra)
        logger.info(f"[SERVICE] Busca finalizada: {len(documentos)} documento(s) encontrado(s) para '{palavra}'")

        return [DocumentoResponse.model_validate(doc) for doc in documentos]


    @staticmethod
    def buscar(db: Session, palavra: str | None, frase: str | None,
               latitude: float | None, longitude: float | None) -> list[DocumentoResponse]:

        if frase:
            logger.info(f"[SERVICE] Iniciando busca por frase: '{frase}'")
            resultados = DocumentoRepository.buscar_por_frase(db, frase)

        else:
            if not palavra or not palavra.strip():
                logger.warning("[SERVICE] Falha na busca: palavra-chave vazia")
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="A palavra-chave nao pode ser vazia."
                )

            logger.info(f"[SERVICE] Iniciando busca por palavra-chave: '{palavra}'")
            resultados = DocumentoRepository.buscar_por_palavra_chave(db, palavra)

        if latitude is not None and longitude is not None:
            logger.info(f"[SERVICE] Ordenando resultados por proximidade geografica")

            try:
                resultados = sorted(
                    resultados,
                    key=lambda doc: calcular_distancia(
                        latitude, longitude, doc.latitude, doc.longitude
                    )
                )
            except Exception as e:
                logger.error(f"[SERVICE] Erro ao calcular distância: {e}")

        logger.info(f"[SERVICE] Busca finalizada: {len(resultados)} documento(s) retornado(s)")

        return [DocumentoResponse.model_validate(doc) for doc in resultados]
