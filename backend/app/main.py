import sys
from pathlib import Path

# Add project root to sys.path to allow imports from the 'scrapers' directory
project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models
from .routes import router

# Create the database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BlackFriday.Africa API",
    description="API for BlackFriday.Africa MVP",
    version="0.1.0",
)

# Set up CORS
origins = [
    "http://localhost",
    "http://localhost:5173",
    "https://blackfriday-africa.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the BlackFriday.Africa API"}