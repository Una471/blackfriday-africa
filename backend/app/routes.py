from fastapi import APIRouter
import csv
from pathlib import Path

router = APIRouter(prefix="/api", tags=["Products"])

CSV_PATH = Path(__file__).resolve().parents[2] / "csv_upload" / "real_products.csv"


def read_csv():
    products = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["price"] = float(row["price"])  # convert price to number
            products.append(row)
    return products


@router.get("/products")
def get_all_products():
    return read_csv()


@router.get("/products/category/{category}")
def get_products_by_category(category: str):
    products = read_csv()
    filtered = [p for p in products if p["category"].lower() == category.lower()]
    return filtered
