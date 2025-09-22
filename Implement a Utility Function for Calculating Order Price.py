def calculate_order_total(order_items):
    """
    Calculate the total cost of an order.

    Args:
        order_items (list of dict): A list where each item is a dictionary
                                    containing 'quantity' (int) and 'price' (float/decimal).
                                    Example: [{"quantity": 2, "price": 10.0}, {"quantity": 1, "price": 5.5}]
    Returns:
        float: The total cost of the order. Returns 0.0 if the list is empty.
    """
    if not order_items:
        return 0.0  # Handle empty order list gracefully

    total = 0.0
    for item in order_items:
        # Ensure valid keys exist and handle missing/invalid data safely
        quantity = item.get("quantity", 0)
        price = item.get("price", 0.0)

        # Only add if both quantity and price are valid numbers
        try:
            total += float(quantity) * float(price)
        except (ValueError, TypeError):
            continue  # Skip invalid entries without breaking the function

    return round(total, 2)  # Round to 2 decimal places (like currency)


# ----------------------------
# Example Usage
# ----------------------------
if __name__ == "__main__":
    order = [
        {"quantity": 2, "price": 10.0},   # 2 x 10.0 = 20.0
        {"quantity": 1, "price": 5.5},    # 1 x 5.5 = 5.5
        {"quantity": 3, "price": 7.25}    # 3 x 7.25 = 21.75
    ]
    print("Total Order Price:", calculate_order_total(order))  
    # Output: Total Order Price: 47.25
