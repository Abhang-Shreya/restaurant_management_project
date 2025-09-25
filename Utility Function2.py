# File: orders/utils.py

def calculate_discount(order_total, discount_percentage):
    """
    Calculate the discount amount for an order.

    Formula:
        discount_amount = order_total * (discount_percentage / 100)

    Args:
        order_total (float or int): The total amount of the order.
        discount_percentage (float or int): The discount percentage to apply.

    Returns:
        float: The calculated discount amount.

    Raises:
        ValueError: If order_total or discount_percentage are negative.
        TypeError: If inputs are not numeric (int or float).

    Example:
        >>> calculate_discount(1000, 10)
        100.0
        >>> calculate_discount(500, 15)
        75.0
    """
    # Validate input types
    if not isinstance(order_total, (int, float)):
        raise TypeError("order_total must be a number (int or float).")
    if not isinstance(discount_percentage, (int, float)):
        raise TypeError("discount_percentage must be a number (int or float).")

    # Validate values
    if order_total < 0:
        raise ValueError("order_total cannot be negative.")
    if discount_percentage < 0:
        raise ValueError("discount_percentage cannot be negative.")

    # Calculate discount
    discount_amount = order_total * (discount_percentage / 100.0)
    return round(discount_amount, 2)  # rounded to 2 decimals for currency
