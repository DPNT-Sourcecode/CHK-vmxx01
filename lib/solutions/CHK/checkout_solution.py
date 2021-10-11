# noinspection PyUnusedLocal
# skus = unicode string
from .price_table import PRICE_TABLE
import math

def checkout(skus: str) -> int:
    """Main function to calculate checkout value"""
    try:
        basket = get_sku_count(skus)
        return calculate_total_price(basket)
    except TypeError as e:
        print(e)
        return -1


def get_sku_count(skus: str) -> dict:
    """Get the SKU count as a dict

    Args:
        skus (str): input of shopping items denoted by their SKU

    Raises:
        TypeError: an invalid SKU was entered into the SKUs string

    Returns:
        dict: a basket of SKUs. Keys are SKUs and values are the number of items
    """
    unit_tracker = {}
    for sku in skus:
        price_data = PRICE_TABLE.get(sku)
        if price_data is None:
            raise TypeError("The SKU input is invalid.")

        # Update unit tracker when we find a SKU
        if sku not in unit_tracker:
            unit_tracker[sku] = 0
        
        unit_tracker[sku] += 1

    return unit_tracker


def calculate_total_price(basket: dict) -> int:
    """Generate the total price of goods in the basket

    This function calculates the total price based on a basket of goods.
    It uses two trackers: total_added and total_subtracted, to determine the value of goods and relevant offers to apply.
    
    Offers are tracked in the discount_tracker dict, which maps the SKUs with a list of offers available.

    For each SKU, we loop through to find the "best" offer available (determined by the discount value).
    This is then applied to the SKU with a check on the number of SKUs available to discount.

    Args:
        basket (dict): basket of goods checked out

    Returns:
        int: total value of the basket after discounts
    """
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
            # Assume that discounts are better as source_units increases
            sorted_offers = sorted(offers, key=lambda d: d['source_units'], reverse=True)
                
            for offer in sorted_offers:
                source_units = offer['source_units']
                target_units = offer['target_units']
                offer_discount = offer['offer_discount']

                times_to_apply_offer = math.floor(quantity / source_units)
                quantity %= source_units
                if times_to_apply_offer > 0:
                    target_sku = offer['target_sku']
                    if discount_tracker.get(target_sku) is None:
                        discount_tracker[target_sku] = []
                    
                    discount_tracker[target_sku].append((times_to_apply_offer, offer_discount, target_units))
        
    for target_sku in discount_tracker:
        if basket.get(target_sku) is None:
            continue

        sorted_discounts = sorted(
            discount_tracker[target_sku], 
            key=lambda d: d[1], 
            reverse=True
        )
        for (d_quantity, d_value) in sorted_discounts:
            if d_quantity >= basket[target_sku]:
                total_subtracted += d_value * basket[target_sku]
                basket[target_sku] = 0
            else:
                total_subtracted += d_value * d_quantity
                basket[target_sku] -= d_quantity

    return total_added - total_subtracted


