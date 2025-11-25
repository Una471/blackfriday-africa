import sys
from pathlib import Path

# Add project root to sys.path to allow imports from the 'scrapers' directory
project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware
from .database import engine
from . import models
from .routes import router
from csv_upload.import_script import import_products_from_csv # Import our function

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
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.post("/admin/populate-database", tags=["Admin"], status_code=status.HTTP_201_CREATED)
def populate_database():
    """
    One-time endpoint to populate the database from the committed products.csv file.
    """
    try:
        csv_path = project_root / "csv_upload" / "products.csv"
        if not csv_path.is_file():
            return Response(content="products.csv not found on the server.", status_code=status.HTTP_404_NOT_FOUND)
        
        import_products_from_csv(str(csv_path))
        return {"message": "Database populated successfully!"}
    except Exception as e:
        return Response(content=f"An error occurred: {str(e)}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get("/")
def read_root():
    return {"message": "Welcome to the BlackFriday.Africa API"}
