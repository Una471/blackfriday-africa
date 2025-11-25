async def scrape_builders():
    """
    Returns a list of sample products for Builders Warehouse for MVP testing.
    This function provides hardcoded data instead of actual scraping.
    """
    sample_products = [
        {
            "name": "Bosch GSB 18V-50 Cordless Drill",
            "price": 2999.00,
            "retailer": "Builders",
            "category": "Power Tools",
            "image_url": "https://i.im.ge/2025/11/25/4Lp4U4.bosch.jpeg",
            "affiliate_link": "https://www.builders.co.za/search/?text=Bosch%20GSB%2018V-50%20Cordless%20Drill",
        },
        {
            "name": "Dulux Weatherguard 20L Paint",
            "price": 999.00,
            "retailer": "Builders",
            "category": "Paint",
            "image_url": "https://i.im.ge/2025/11/25/4LpcWS.paint.jpeg",
            "affiliate_link": "https://www.builders.co.za/Paint/PVA-Paint/Fine-Texture/Dulux-Weatherguard-Fine-Textured-Paint-White-20-L--ndash--Exterior-Wall-Coating-with-Maxiflex-for-Crack-Resistance-and-Weatherproof-Protection/p/000000000010370012",
        },
        {
            "name": "Ryobi 2000W Lawnmower",
            "price": 2499.00,
            "retailer": "Builders",
            "category": "Gardening",
            "image_url": "https://i.im.ge/2025/11/25/4LpUnp.ryobi.jpeg",
            "affiliate_link": "https://www.builders.co.za/search/?text=Ryobi%202000W%20Lawnmower",
        },
    ]
    return sample_products


if __name__ == "__main__":
    import asyncio

    async def main():
        products = await scrape_builders()
        print(f"Generated {len(products)} dummy products from Builders.")
        for product in products:
            print(product)

    asyncio.run(main())