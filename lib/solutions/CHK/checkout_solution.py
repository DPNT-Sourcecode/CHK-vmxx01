# noinspection PyUnusedLocal
# skus = unicode string
from .price_table import PRICE_TABLE

def checkout(skus: str) -> int:
    unit_tracker = {}
    for sku in skus:
        price_data = PRICE_TABLE.get(sku)
        if price_data is None:
            return -1

        # Update unit tracker when we find a SKU
        if sku not in unit_tracker:
            unit_tracker[sku] = 0
        
        unit_tracker[sku] += 1

    # Manipulate the unit_tracker dict to calculate price, rather than sum in-line
    return calculate_total_price(unit_tracker)

        # # Use PRICE_TABLE's sub-dict to determine how much to add to total_price
        # offer = price_data.get("offer")
        # price = price_data.get("price")

        # if offer is None:
        #     total_price += price
        # else:
        #     if unit_tracker[sku] % offer.get("offer_unit") == 0:
        #         total_price += offer.get("offer_price")
        #     else:
        #         total_price += price


def calculate_total_price(basket: dict) -> int:
    total_added = 0
    total_subtracted = 0
    discount_tracker = {}
    for sku in basket:
        # Here we assume that the price data already exists
        price_data = PRICE_TABLE.get(sku)
        price = price_data.get("price")
        offers = price_data.get("offers")
        quantity = basket[sku]

        total_added += quantity * price

        if offers is not None:
            sorted_offers = sorted(offers, key=lambda d: d['source_units'], reverse=True)
                
            print(sorted_offers)
            # if discount_tracker[sku] is None:
            #     discount_tracker[sku] = []
            
            # discount_tracker[sku].append()
        


    return total_added - total_subtracted
