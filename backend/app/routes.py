from fastapi import APIRouter
from typing import List, Optional

from . import crud

router = APIRouter()

@router.get("/products", tags=["Products"])
def read_products(category: Optional[str] = None, skip: int = 0, limit: int = 100):
    if category:
        products = crud.get_products_by_category(category=category, skip=skip, limit=limit)
    else:
        products = crud.get_products(skip=skip, limit=limit)
    return products


@router.get("/retailers", response_model=List[str], tags=["Retailers"])
def read_retailers():
    return crud.get_retailers()


@router.get("/categories", response_model=List[str], tags=["Categories"])
def read_categories():
    return crud.get_categories()

