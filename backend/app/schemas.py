from pydantic import BaseModel, ConfigDict
from datetime import datetime

# Base schema for a Product
class ProductBase(BaseModel):
    name: str
    price: float
    retailer: str
    category: str
    image_url: str
    affiliate_link: str

# Schema for creating a new Product
class ProductCreate(ProductBase):
    pass

# Schema for reading/returning a Product from the API
class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
