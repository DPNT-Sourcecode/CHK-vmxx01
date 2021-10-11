# noinspection PyUnusedLocal
# skus = unicode string
PRICE_TABLE = {
    "A": {
        "price": 50,
        "offer": {
            "offer_unit": 3,
            "offer_price": 30
        }
    },
    "B": {
        "price": 30,
        "offer": {
            "offer_unit": 2,
            "offer_price": 15
        }
    },
    "C": {
        "price": 20
    },
    "D": {
        "price": 15
    }
}

def checkout(skus: str):
    for sku in skus:
        print(sku)

