from pathlib import Path

class Settings:
    # Caminho para o banco SQLite (arquivo local)
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATABASE_URL = f"sqlite:///{BASE_DIR / 'documentos.db'}"

settings = Settings()
