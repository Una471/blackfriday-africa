import asyncio
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional

from . import crud, models, schemas
from .database import get_db

# Correct scraper imports
from scrapers.takealot_scraper import scrape_takealot
from scrapers.game_scraper import scrape_game
from scrapers.makro_scraper import scrape_makro
from scrapers.hificorp_scraper import scrape_hificorp
from scrapers.incredible_scraper import scrape_incredible
from scrapers.builders_scraper import scrape_builders

router = APIRouter()


@router.post("/seed-db", status_code=201, tags=["Database"])
async def seed_db(db: Session = Depends(get_db)):
    """
    Seeds the database with dummy data from all scrapers.
    This is a temporary endpoint for development purposes.
    It will not insert duplicate products (based on name and retailer).
    """

    scrapers_to_run = [
        scrape_takealot(),
        scrape_game(),
        scrape_makro(),
        scrape_hificorp(),
        scrape_incredible(),
        scrape_builders(),
    ]

    all_products = await asyncio.gather(*scrapers_to_run)

    product_count = 0
    for product_list in all_products:
        for product in product_list:
            existing_product = db.query(models.Product).filter(
                models.Product.name == product["name"],
                models.Product.retailer == product["retailer"]
            ).first()

            if not existing_product:
                product_data = schemas.ProductCreate(**product)
                crud.create_product(db=db, product=product_data)
                product_count += 1

    return {"message": f"Successfully inserted {product_count} new products into the database."}


@router.get("/products", response_model=List[schemas.ProductResponse], tags=["Products"])
def read_products(category: Optional[str] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if category:
        products = crud.get_products_by_category(db, category=category, skip=skip, limit=limit)
    else:
        products = crud.get_products(db, skip=skip, limit=limit)
    return products


@router.get("/retailers", response_model=List[str], tags=["Retailers"])
def read_retailers(db: Session = Depends(get_db)):
    return crud.get_retailers(db)


@router.get("/categories", response_model=List[str], tags=["Categories"])
def read_categories(db: Session = Depends(get_db)):
    return crud.get_categories(db)
