import os
import datetime # Import datetime specifically for the now_iso function

def now_iso():
    """Returns the current UTC time in ISO format."""
    return datetime.datetime.now().isoformat()

# NOTE: The function name is 'scrape_takealot' to match the import requirements.
async def scrape_takealot(limit=20):
    
    print("Scraping Takealot (using DUMMY data for MVP)...")
    
    # We are using high-quality, royalty-free stock image URLs for visual fidelity.
    sample_products = [
        {
            "name": "Lenovo ThinkBook 14-inch 2 in 1 Intel Core Ultra 7 155U 16GB RAM 512GB SSD",
            "price": 22999.00,
            "retailer": "Takealot",
            "category": "Laptops",
            "image_url": "https://media.takealot.com/covers_images/8b3c257fa08149489d317be9d810566f/s-zoom.file",
            "affiliate_link": "https://www.takealot.com/all?_sb=1&_r=1&_si=edca49fd73244df45d22907b8513796a&qsearch=ZenBook%2014%20Ultra%20(16GB%20RAM)",
            "created_at": now_iso(),
        },
        {
            "name": "Apple iPhone 17 256GB",
            "price": 20799.00,
            "retailer": "Takealot",
            "category": "Smartphones",
            "image_url": "https://media.takealot.com/covers_images/db3b3307594646deb200df3dbb3ffd03/s-zoom.file",
            "affiliate_link": "https://www.takealot.com/apple-iphone-17-256gb/PLID99469601",
            "created_at": now_iso(),
        },
        {
            "name": "Audio Headphone bluetooth 5.4 Headphones Noise Cancellation Over Ear",
            "price": 1299.00,
            "retailer": "Takealot",
            "category": "Audio",
            "image_url": "https://media.takealot.com/covers_images/9624a4b761f84ede92cca61819071983/s-zoom.file",
            "affiliate_link": "Audio Headphone bluetooth 5.4 Headphones Noise Cancellation Over Ear",
            "created_at": now_iso(),
        },
        {
            "name": "Acer Predator Helios Neo 16 Core i5 16GB 1TB SSD RTX 4060 16' Gaming laptop",
            "price": 36820.99,
            "retailer": "Takealot",
            "category": "Laptops",
            "image_url": "https://media.takealot.com/covers_images/6104115370134ec8a967fbcade8710ec/s-zoom.file",
            "affiliate_link": "https://www.takealot.com/acer-predator-helios-neo-16-core-i5-16gb-1tb-ssd-rtx-4060-16-gam/PLID95102106",
            "created_at": now_iso(),
        },
    ]
    
    # Trim to limit if needed (though limit=20 is fine here)
    products_to_return = sample_products[:limit]
    
    print(f"✅ Dummy scraping complete. Generated {len(products_to_return)} products.")
    return products_to_return


if __name__ == "__main__":
    import asyncio

    async def main():
        products = await scrape_takealot()
        print(f"Generated {len(products)} dummy products.")
        for product in products:
            print(product)

    asyncio.run(main())