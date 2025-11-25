async def scrape_game():
    """
    Returns a list of sample products for Game for MVP testing.
    This function provides hardcoded data instead of actual scraping.
    """
    sample_products = [
        {
            "name": "HISENSE SMART UHD TV 65A6Q",
            "price": 7999.00,
            "retailer": "Game",
            "category": "TVs",
            "image_url": "https://i.im.ge/2025/11/25/4LkcR4.hisense-tv.jpeg",
            "affiliate_link": "https://www.game.co.za/Electronics-Entertainment/Television/TVs/p/000000000850028687",
        },
        {
            "name": "BENNETT READ 20L Digital Microwave KMW112",
            "price": 1399.00,
            "retailer": "Game",
            "category": "Appliances",
            "image_url": "https://i.im.ge/2025/11/25/4LzDmY.Microwavez.jpeg",
            "affiliate_link": "https://www.game.co.za/Home-Appliances/Kitchen-Large-Appliances/Microwaves-Convection-Ovens/p/000000000000836643",
        },
        {
            "name": "PlayStation 5 Console",
            "price": 13999.00,
            "retailer": "Game",
            "category": "Gaming",
            "image_url": "https://i.im.ge/2025/11/25/4Lz9aP.PS5.jpeg",
            "affiliate_link": "https://www.game.co.za/Electronics-Entertainment/Gaming/Consoles/p/000000000850009513",
        },
    ]
    return sample_products


if __name__ == "__main__":
    import asyncio

    async def main():
        products = await scrape_game()
        print(f"Generated {len(products)} dummy products from Game.")
        for product in products:
            print(product)

    asyncio.run(main())