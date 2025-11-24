from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.documento_schema import DocumentoCreate, DocumentoResponse
from app.services.documento_service import DocumentoService
from app.core.database import get_db
from app.utils.logger import get_logger


logger = get_logger()
router = APIRouter(prefix="/documentos", tags=["Documentos"])


@router.post("/", response_model=DocumentoResponse, status_code=201)
def criar_documento(documento: DocumentoCreate, db: Session = Depends(get_db)):
    logger.info(f"POST /documentos recebido (titulo='{documento.titulo}')")
    return DocumentoService.criar_documento(db, documento)


@router.get("/", response_model=list[DocumentoResponse])
def buscar_documentos(
    palavraChave: str | None = None,
    busca: str | None = None,
    latitude: float | None = None,
    longitude: float | None = None,
    db: Session = Depends(get_db)
):
    logger.info(
        f"GET /documentos recebido (palavraChave='{palavraChave}', "
        f"busca='{busca}', latitude='{latitude}', longitude='{longitude}')"
    )

    return DocumentoService.buscar(
        db=db,
        palavra=palavraChave,
        frase=busca,
        latitude=latitude,
        longitude=longitude
    )
