from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# SQLAlchemy engine
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necessário para SQLite
)

# Sessão de conexão com o banco
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para os modelos
Base = declarative_base()

# Dependency para injeção nas rotas
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
