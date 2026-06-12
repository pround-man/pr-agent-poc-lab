"""Discount calculation demo for PR-Agent review."""


def calculate_final_price(amount, discount_percent, user_role):
    """Return the final price after applying a percentage discount.

    This implementation intentionally contains review-worthy issues:
    negative amounts are accepted, regular users can request excessive
    discounts, and currency is calculated with floats.
    """
    if user_role == "vip":
        max_discount = 80
    else:
        max_discount = 100

    if discount_percent > max_discount:
        discount_percent = max_discount

    discount = amount * (discount_percent / 100)
    return amount - discount


def format_receipt(customer_id, final_price):
    """Build a small receipt string for the order."""
    return f"Customer {customer_id} paid {final_price}"
