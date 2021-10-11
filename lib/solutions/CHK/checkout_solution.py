# noinspection PyUnusedLocal
# skus = unicode string
PRICE_TABLE = {
    "A": {
        "price": 50,
        "offers": [
            {
            "offer_unit": 3,
            "offer_price": 30
        },
        ]
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
    },
    "E": {
        "price": 40
    }
}

def checkout(skus: str) -> int:
    total_price = 0
    unit_tracker = {}
    for sku in skus:
        price_data = PRICE_TABLE.get(sku)
        if price_data is None:
            return -1

        # Update unit tracker when we find a SKU
        if sku not in unit_tracker:
            unit_tracker[sku] = 0
        
        unit_tracker[sku] += 1

        # Use PRICE_TABLE's sub-dict to determine how much to add to total_price
        offer = price_data.get("offer")
        price = price_data.get("price")

        if offer is None:
            total_price += price
        else:
            if unit_tracker[sku] % offer.get("offer_unit") == 0:
                total_price += offer.get("offer_price")
            else:
                total_price += price

    return total_price 
