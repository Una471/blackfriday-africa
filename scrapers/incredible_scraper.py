async def scrape_incredible():
    """
    Returns a list of sample products for Incredible Connection for MVP testing.
    This function provides hardcoded data instead of actual scraping.
    """
    sample_products = [
        {
            "name": "Apple MacBook Air 13-inch M4",
            "price": 18999.00,
            "retailer": "Incredible Connection",
            "category": "Laptops",
            "image_url": "https://www.incredible.co.za/api/catalog/product/m/a/macbook_air_13_in_m4_chip_starlight_pure_front_screen__usen_ecommerce_9ad6.png?store=incredibleconnection&image-type=image",
            "affiliate_link": "https://www.incredible.co.za/apple-macbook-air-13-m4-10-core-cpu-8-core-gpu-16gb-ram-256gb-ssd-starlight",
        },
        {
            "name": "`Logitech MX Master 3S Mouse",
            "price": 1499.00,
            "retailer": "Incredible Connection",
            "category": "Peripherals",
            "image_url": "https://i.im.ge/2025/11/25/4LHwDK.mouse.jpeg",
            "affiliate_link": "`https://www.incredible.co.za/logitech-mx-master-3s-performance-wireless-mouse-graphite",
        },
        {
            "name": "`Epson EcoTank L3250 Printer",
            "price": 3999.00,
            "retailer": "Incredible Connection",
            "category": "Printers",
            "image_url": "https://www.incredible.co.za/api/catalog/product/l/3/l3250._article_10282854__1__ecommerce_b104.png?store=incredibleconnection&image-type=image",
            "affiliate_link": "https://www.incredible.co.za/epson-ecotank-l3250-printer",
        },
        {
            "name": "Toshiba Canvio Basic 2.5inch 4TB Ext HDD",
            "price": 2499.00,
            "retailer": "Incredible Connection",
            "category": "Storage",
            "image_url": "https://www.incredible.co.za/api/catalog/product/1/0/10118275_inc_ecommerce_dfad.png?width=700&height=700&store=incredibleconnection&image-type=image",
            "affiliate_link": "https://www.incredible.co.za/toshiba-canvio-basic-2-5inch-4tb-ext-hdd",
        },
    ]
    return sample_products


if __name__ == "__main__":
    import asyncio

    async def main():
        products = await scrape_incredible()
        print(f"Generated {len(products)} dummy products from Incredible Connection.")
        for product in products:
            print(product)

    asyncio.run(main())