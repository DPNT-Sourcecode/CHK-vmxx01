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


def get_group_value(basket: dict, group_offer: dict) -> int:
    """Get the value of items on group offer

    This function assumes that there are no additional offers for members of the target group offer.

    Args:
        basket (dict): basket of goods checked out
        group_offer (dict): dict containing details of the group offer

    Returns:
        int: total value of group offer items after applying group discounts
    """
    total_value = 0
    target_group = group_offer['target_group']
    target_units = group_offer['target_units']
    group_price = group_offer['group_price']
    sorted_prices = sorted(
        [(t, PRICE_TABLE.get(t)['price']) for t in target_group],
        key=lambda d: d[1], 
        reverse=True
    )

    total_items = 0
    for (sku, _) in sorted_prices:
        sku_quantity = basket.get(sku, 0)
        total_items += sku_quantity

    total_value += math.floor(total_items / target_units) * group_price

    remainder = total_items % target_units

    for (sku, price) in reversed(sorted_prices):
        if remainder <= 0:
            break
        sku_quantity = basket[sku]
        if sku_quantity >= remainder:
            total_value += remainder * price
            remainder = 0
        else:
            total_value += sku_quantity * price
            remainder -= sku_quantity

    return total_value


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
    groups_checked = []
    for sku in basket:
        # Here we assume that the price data already exists
        price_data = PRICE_TABLE.get(sku)
        price = price_data.get("price")
        offers = price_data.get("offers", [])
        
        # We assume that no other offers exist for group offers
        target_group = offers[0].get("target_group")

        # Check if this SKU is part of a group offer
        if target_group is not None:
            if target_group not in groups_checked:
                total_added += get_group_value(
                    basket, 
                    offers[0]
                )
                groups_checked.append(target_group)
            continue

        sku_quantity = basket[sku]
        total_added += sku_quantity * price

        if offers is not None:
            # Assume that discounts are better as source_units increases
            sorted_offers = sorted(offers, key=lambda d: d['source_units'], reverse=True)
                
            for offer in sorted_offers:
                source_units = offer['source_units']
                target_units = offer['target_units']
                offer_discount = offer['offer_discount']

                times_to_apply_offer = math.floor(sku_quantity / source_units)
                sku_quantity %= source_units
                if times_to_apply_offer > 0:
                    target_sku = offer['target_sku']
                    if discount_tracker.get(target_sku) is None:
                        discount_tracker[target_sku] = []
                    
                    discount_tracker[target_sku].append((times_to_apply_offer, offer_discount, target_units))
        
    for target_sku in discount_tracker:
        sku_units = basket.get(target_sku)
        if sku_units is None:
            continue

        sorted_discounts = sorted(
            discount_tracker[target_sku], 
            key=lambda d: d[1], 
            reverse=True
        )
        for (d_offers, d_value, d_units) in sorted_discounts:
            while d_offers > 0:
                # If remaining SKU units are too few, don't apply the offer
                if sku_units < d_units:
                    break
                sku_units -= d_units
                total_subtracted += d_value
                d_offers -= 1

    return total_added - total_subtracted


