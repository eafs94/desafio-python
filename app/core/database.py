from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings
import re

# SQLAlchemy engine
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False}  # Necessário para SQLite
)

# Habilitar REGEXP no SQLite
@event.listens_for(engine, "connect")
def sqlite_regexp(dbapi_connection, connection_record):
    def regexp(expr, item):
        if item is None:
            return False
        return bool(re.search(expr, item, re.IGNORECASE))
    dbapi_connection.create_function("REGEXP", 2, regexp)

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
