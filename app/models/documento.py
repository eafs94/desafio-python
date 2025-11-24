from sqlalchemy import Column, Integer, String, Date, Float
from app.core.database import Base

class Documento(Base):
    __tablename__ = "documentos"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, nullable=False)
    autor = Column(String, nullable=False)
    conteudo = Column(String, nullable=False)
    data = Column(Date, nullable=False)

    # Campos bônus
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
