from datetime import date
from django.db.models import Sum
from .models import Order  # Import your Order model


# ------------------------------------------------
# Utility Function: Calculate Daily Sales Total
# ------------------------------------------------
def get_daily_sales_total(specific_date):
    """
    Returns the total sales (sum of total_price) for all orders created on a specific date.

    Args:
        specific_date (datetime.date): The date for which to calculate total sales.

    Returns:
        Decimal or float: The total sales for the given date. Returns 0 if no orders exist.
    """

    # Filter orders created on the given date
    orders = Order.objects.filter(created_at__date=specific_date)

    # Aggregate the total sum of total_price
    result = orders.aggregate(total_sum=Sum('total_price'))

    # Get the total or 0 if no orders found
    total_sales = result['total_sum'] or 0

    return total_sales


# ------------------------------------------------
# (Optional) Test the function manually
# ------------------------------------------------
if __name__ == "__main__":
    # Example usage for testing purposes
    today = date.today()
    total = get_daily_sales_total(today)
    print(f"Total sales for {today}: ₹{total}")
