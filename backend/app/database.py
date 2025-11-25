from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from pathlib import Path
import os

# Detect if running on Render
IS_RENDER = os.environ.get("RENDER") == "true"

if IS_RENDER:
    # Render uses this directory for writable storage
    DB_DIR = Path("/opt/render/project/src/.data")
    DB_DIR.mkdir(parents=True, exist_ok=True)
    DB_PATH = DB_DIR / "database.db"
else:
    # Local environment (Windows/macOS/Linux)
    DB_PATH = Path(__file__).resolve().parent.parent / "database.db"

SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
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
