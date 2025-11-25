from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from pathlib import Path
import os

# Render-safe writable directory
RUNTIME_DIR = Path("/opt/render/project/src/.data")
RUNTIME_DIR.mkdir(exist_ok=True)  # Ensure folder exists

DB_PATH = RUNTIME_DIR / "database.db"

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
