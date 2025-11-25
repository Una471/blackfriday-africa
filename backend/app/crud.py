from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas

def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_products_by_category(db: Session, category: str, skip: int = 0, limit: int = 100):
    return db.query(models.Product).filter(func.lower(models.Product.category) == func.lower(category)).offset(skip).limit(limit).all()

def get_retailers(db: Session):
    rows = db.query(models.Product.retailer).distinct().all()
    return [r[0] for r in rows if r[0]]


def get_categories(db: Session):
    rows = db.query(models.Product.category).distinct().all()
    return [r[0] for r in rows if r[0]]


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product
