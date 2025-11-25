from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from pathlib import Path

# Construct a path to the database file in the `backend` directory.
# This makes the path relative to this file's location, which is more robust.
DB_PATH = Path(__file__).resolve().parent.parent / "database.db"
SQLALCHEMY_DATABASE_URL = DB_PATH.as_uri().replace("file:///", "sqlite:///")

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