# ------------------------------------------------
# 🪙 Currency Formatting Utility
# ------------------------------------------------
def format_currency(amount):
    """
    Returns a string formatted as currency with a dollar sign
    and two decimal places.
    
    Example:
        format_currency(12.5)  -> "$12.50"
        format_currency(100)   -> "$100.00"
    """
    return f"${amount:.2f}"


# ------------------------------------------------
# 💡 Example Usage (for testing)
# ------------------------------------------------
if __name__ == "__main__":
    # Sample test cases
    print(format_currency(12.5))     # Output: $12.50
    print(format_currency(100))      # Output: $100.00
    print(format_currency(99.999))   # Output: $100.00
    print(format_currency(0))        # Output: $0.00
