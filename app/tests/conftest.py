import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.main import app
from app.core.database import Base, get_db

# Banco SQLite apenas para os testes
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_db.sqlite"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Override no FastAPI
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    # cria tudo antes dos testes
    Base.metadata.create_all(bind=engine)
    yield
    # limpa depois
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    return TestClient(app)
