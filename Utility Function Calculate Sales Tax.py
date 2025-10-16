from decimal import Decimal, ROUND_HALF_UP

def calculate_sales_tax(amount, tax_rate):
    """
    Calculate the sales tax based on the given amount and tax rate.

    Parameters:
        amount (Decimal): The subtotal before tax.
        tax_rate (Decimal): The tax rate as a decimal (e.g., 0.05 for 5%).

    Returns:
        Decimal: The calculated sales tax amount.
    """
    if not isinstance(amount, Decimal):
        amount = Decimal(str(amount))
    if not isinstance(tax_rate, Decimal):
        tax_rate = Decimal(str(tax_rate))

    tax = amount * tax_rate

    # Round to 2 decimal places (like typical currency)
    tax = tax.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return tax
