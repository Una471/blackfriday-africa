async def scrape_makro():
    """
    Returns a list of sample products for Makro for MVP testing.
    This function provides hardcoded data instead of actual scraping.
    """
    sample_products = [
        {
            "name": "`Dell Intel Core i5 13th Gen 1334U",
            "price": 10898.00,
            "retailer": "Makro",
            "category": "Laptops",
            "image_url": "https://www.makro.co.za/asset/rukmini/fccp/832/832/ng-fkpublic-ui-user-fbbe/laptop/9/r/j/512-gb-13th-gen-i3530i58512w11h-8-gb-15-6-inspiron-15-3530-na-no-original-imahcrmp4bvccths.jpeg?q=70",
            "affiliate_link": "https://www.makro.co.za/dell-intel-core-i5-13th-gen-1334u-8-gb-512-gb-ssd-windows-11-home-inspiron-15-3530-laptop/p/itm718c731052468?pid=LTPHCRMPQYWQHNNC&lid=LSTLTPHCRMPQYWQHNNCILNVLA&q=Dell+Inspiron+15+Laptop&store=6bo%2Fb5g&srno=s_1_1&otracker=search&otracker1=search&fm=organic&iid=ab2b3314-226b-4d24-b2fd-16fcc467b8aa.LTPHCRMPQYWQHNNC.SEARCH&ppt=hp&ppn=homepage&ssid=p1te2e49800000001764015489134&qH=c61edf495969c952",
        },
        {
            "name": "Weber Master-Touch Braai",
            "price": 8999.00,
            "retailer": "Makro",
            "category": "Outdoor",
            "image_url": "https://i.im.ge/2025/11/25/4LHqec.braai.jpeg",
            "affiliate_link": "https://www.makro.co.za/weber-master-touch-57-c-5750-ocean-blue-14716004-charcoal-braai/p/itm15588bb984670?pid=BGLH53ZEBJFPTA2X&lid=LSTBGLH53ZEBJFPTA2XOKBUAH&q=Weber+Master-Touch+Braai&store=upp&srno=s_1_2&otracker=search&otracker1=search&fm=organic&iid=1bb662b9-2fdb-4ead-a09e-cddcb1642b61.BGLH53ZEBJFPTA2X.SEARCH&ppt=pp&ppn=pp&ssid=3wdjkg7e9s0000001764015672287&qH=40180551a6bac818",
        },
        {
            "name": "Hisense 508 L Side by Side Fridge",
            "price": 14999.00,
            "retailer": "Makro",
            "category": "Appliances",
            "image_url": "https://i.im.ge/2025/11/25/4Lzn6M.fridge.jpeg",
            "affiliate_link": "https://www.makro.co.za/hisense-508-l-side-fridge/p/itm4753e362fe820?pid=RFRH2FVNRYTRPZ7Z&lid=LSTRFRH2FVNRYTRPZ7ZFRJHDM&q=fridge&store=j9e%2Fabm%2Fhzg&srno=s_1_11&otracker=search&otracker1=search&fm=Search&iid=b15d73e4-5c8f-4b3c-8d96-081f7658e7bc.RFRH2FVNRYTRPZ7Z.SEARCH&ppt=sp&ppn=sp&ssid=bt488t348w0000001764015873256&qH=2be977f3ff92dd10",
        },
        {
            "name": "Camp Master 5-Person Tent",
            "price": 2499.00,
            "retailer": "Makro",
            "category": "Camping",
            "image_url": "https://www.makro.co.za/asset/rukmini/fccp/832/832/ng-fkpublic-ui-user-fbbe/tent/n/j/4/-original-imah2f52axytrdfu.jpeg?q=70",
            "affiliate_link": "https://www.makro.co.za/camp-master-family-cabin-tent-5-person/p/itm3982b48a1e4b0?pid=TNTHFZZEWVPKACHP&lid=LSTTNTHFZZEWVPKACHPOBSSOJ&q=Camp+Master+8-Person+Tent&store=abc%2Ffvf%2Fs9a&spotlightTagId=BlackFriday_abc%2Ffvf%2Fs9a&srno=s_1_11&otracker=search&otracker1=search&fm=Search&iid=fc1d1c64-f2da-4561-a985-606ae10880f6.TNTHFZZEWVPKACHP.SEARCH&ppt=sp&ppn=sp&ssid=j0ss40w2zk0000001764016005525&qH=412616a3c4e66446",
        },
    ]
    return sample_products


if __name__ == "__main__":
    import asyncio

    async def main():
        products = await scrape_makro()
        print(f"Generated {len(products)} dummy products from Makro.")
        for product in products:
            print(product)

    asyncio.run(main())