def calculate_discount(original_price, discount_percentage):
    """
    Calculate the discounted price based on original price and discount percentage.

    Args:
        original_price (float): The original price of the item (must be >= 0).
        discount_percentage (float): The discount percentage (0 - 100).

    Returns:
        float: Discounted price rounded to 2 decimal places.
        str: Error message if invalid input.
    """
    try:
        # Convert inputs safely
        original_price = float(original_price)
        discount_percentage = float(discount_percentage)

        # Validate input
        if original_price < 0:
            return "Error: Original price cannot be negative."
        if not (0 <= discount_percentage <= 100):
            return "Error: Discount percentage must be between 0 and 100."

        # Apply discount
        discount_amount = (original_price * discount_percentage) / 100
        discounted_price = original_price - discount_amount

        return round(discounted_price, 2)

    except (ValueError, TypeError):
        return "Error: Invalid input. Please provide numeric values."
