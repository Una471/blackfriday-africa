async def scrape_hificorp():
    """
    Returns a list of sample products for HiFi Corp for MVP testing.
    This function provides hardcoded data instead of actual scraping.
    """
    sample_products = [
        {
            "name": "JBL Flip 7 Bluetooth Speaker",
            "price": 2999.00,
            "retailer": "HiFi Corp",
            "category": "Audio",
            "image_url": "https://www.hificorp.co.za/api/catalog/product/j/b/jbl_flip_7_3_4_right_blue_108_x1_1_ecommerce_9fc4.png?width=700&height=700&store=hificorporation&image-type=image",
            "affiliate_link": "https://www.hificorp.co.za/jbl-flip-7-portable-bluetooth-speaker-blue",
        },
        {
            "name": "Acer Aspire Lite 16 Intel®",
            "price": 10999.00,
            "retailer": "HiFi Corp",
            "category": "Laptops",
            "image_url": "https://i.im.ge/2025/11/25/4LHBdx.aspire.jpeg",
            "affiliate_link": "https://www.hificorp.co.za/acer-aspire-lite-16-intel-core-i5-1334u-8gb-ram-512gb-ssd-laptop",
        },
        {
            "name": "Canon EOS 4000D DSLR Camera",
            "price": 8299.00,
            "retailer": "HiFi Corp",
            "category": "Cameras",
            "image_url": "https://i.im.ge/2025/11/25/4LHz80.camera.jpeg",
            "affiliate_link": "https://www.hificorp.co.za/canon-eos-4000d-starter-bundle",
        },
    ]
    return sample_products


if __name__ == "__main__":
    import asyncio

    async def main():
        products = await scrape_hificorp()
        print(f"Generated {len(products)} dummy products from HiFi Corp.")
        for product in products:
            print(product)

    asyncio.run(main())