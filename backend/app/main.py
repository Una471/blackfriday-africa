import sys
from pathlib import Path
import asyncio

# Add project root to sys.path
project_root = Path(__file__).resolve().parents[2]
sys.path.append(str(project_root))

from fastapi import FastAPI, Response, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Local app imports
from .database import engine, get_db
from . import models, crud, schemas

# Scraper imports
# Assuming each file has a function like 'scrape_takealot', 'scrape_game', etc.
from scrapers import (
    builders_scraper,
    game_scraper,
    hificorp_scraper,
    incredible_scraper,
    makro_scraper,
    takealot_scraper,
)

# API router
from .routes import router

# Create DB tables on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BlackFriday.Africa API",
    description="API for BlackFriday.Africa MVP",
    version="0.1.0",
)

# CORS Middleware
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

# Include API routes
app.include_router(router, prefix="/api")

@app.post("/admin/populate-database", tags=["Admin"], status_code=status.HTTP_201_CREATED)
async def populate_database(db: Session = Depends(get_db)):
    """
    Clears the database and repopulates it with fresh data from all scrapers.
    """
    try:
        # 1. Clear existing products to prevent duplicates
        print("Clearing old data from the database...")
        num_deleted = db.query(models.Product).delete()
        db.commit()
        print(f"Deleted {num_deleted} old products.")

        # 2. Run all scrapers concurrently
        print("Starting all scrapers...")
        scraper_tasks = [
            builders_scraper.scrape_builders(),
            game_scraper.scrape_game(),
            hificorp_scraper.scrape_hificorp(),
            incredible_scraper.scrape_incredible(),
            makro_scraper.scrape_makro(),
            takealot_scraper.scrape_takealot(),
        ]
        all_results = await asyncio.gather(*scraper_tasks, return_exceptions=True)
        print("All scrapers finished.")

        # 3. Process results and add to database
        total_products_added = 0
        for result in all_results:
            if isinstance(result, Exception):
                print(f"A scraper failed with an error: {result}")
                continue

            for product_dict in result:
                try:
                    product_schema = schemas.ProductCreate(**product_dict)
                    crud.create_product(db=db, product=product_schema)
                    total_products_added += 1
                except Exception as e:
                    print(f"Could not add product: {product_dict.get('name')}. Error: {e}")
        
        db.commit() # Commit all new products

        message = f"Database populated successfully! Cleared {num_deleted} old products and added {total_products_added} new products."
        print(message)
        return {"message": message}

    except Exception as e:
        error_message = f"An unexpected error occurred during database population: {str(e)}"
        print(error_message)
        return Response(content=error_message, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

@app.get("/")
def read_root():
    return {"message": "Welcome to the BlackFriday.Africa API"}