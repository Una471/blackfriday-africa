import sys
import csv
from pathlib import Path

# Add the project root to the Python path to allow imports from the backend
project_root = Path(__file__).resolve().parents[1]
sys.path.append(str(project_root))

from backend.app import crud, schemas
from backend.app.database import SessionLocal, engine
from backend.app.models import Base

def import_products_from_csv(csv_filepath: str):
    """
    Reads product data from a CSV file and inserts it into the database.
    Assumes the CSV has headers: name, price, retailer, category, image_url, affiliate_link
    """
    db = SessionLocal()
    print(f"Importing products from: {csv_filepath}")
    try:
        with open(csv_filepath, mode='r', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    product_data = schemas.ProductCreate(
                        name=row["name"],
                        price=float(row["price"]),
                        retailer=row["retailer"],
                        category=row["category"],
                        image_url=row["image_url"],
                        affiliate_link=row["affiliate_link"],
                    )
                    crud.create_product(db=db, product=product_data)
                    print(f"  + Inserted: {product_data.name}")
                except (ValueError, KeyError) as e:
                    print(f"  - Skipping row due to error: {e}. Row: {row}")
    finally:
        db.close()
        print("Database session closed.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python csv_upload/import_script.py <path_to_csv_file>")
        sys.exit(1)

    csv_file_path = sys.argv[1]

    if not Path(csv_file_path).is_file():
        print(f"Error: File not found at '{csv_file_path}'")
        sys.exit(1)

    # Ensure database and tables are created
    print("Initializing database...")
    Base.metadata.create_all(bind=engine)
    print("Database initialized.")

    import_products_from_csv(csv_file_path)

    print("\nImport process finished.")
