import pandas as pd
from typing import List

# Define the path to the CSV file, assuming the script is run from the project root
CSV_PATH = 'csv_upload/real_products.csv'

def get_products_df():
    """Reads the CSV file and returns a pandas DataFrame."""
    try:
        # This path works when the app is run from the 'backend' directory
        return pd.read_csv(f'../{CSV_PATH}')
    except FileNotFoundError:
        # This path works when tests or scripts are run from the project root
        return pd.read_csv(CSV_PATH)

def get_products(skip: int = 0, limit: int = 100):
    df = get_products_df()
    return df.iloc[skip:skip+limit].to_dict('records')

def get_products_by_category(category: str, skip: int = 0, limit: int = 100):
    df = get_products_df()
    # Case-insensitive matching for category
    df_category = df[df['category'].str.lower() == category.lower()]
    return df_category.iloc[skip:skip+limit].to_dict('records')

def get_retailers() -> List[str]:
    df = get_products_df()
    return [r for r in df['retailer'].unique() if r and pd.notna(r)]

def get_categories() -> List[str]:
    df = get_products_df()
    return [c for c in df['category'].unique() if c and pd.notna(c)]

# The create_product function is no longer needed as we're not writing to a CSV here.
# from . import schemas
# def create_product(product: schemas.ProductCreate):
#     # This function would need to append to the CSV, which can be complex
#     # and is not required by the user's request.
#     pass

