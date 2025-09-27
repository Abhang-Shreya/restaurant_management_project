# utils.py

import re

def format_phone_number(phone_number):
    """
    Formats a phone number string into the format: (XXX) XXX-XXXX
    Handles invalid inputs gracefully by returning None.

    Examples:
        '1234567890' -> '(123) 456-7890'
        '+11234567890' -> '(123) 456-7890'
        '123-456-7890' -> '(123) 456-7890'
    """
    try:
        # Remove all non-digit characters
        digits = re.sub(r'\D', '', phone_number)
        
        # Remove leading country code (optional, e.g., 1 for US)
        if len(digits) == 11 and digits.startswith('1'):
            digits = digits[1:]
        
        # Must have exactly 10 digits now
        if len(digits) != 10:
            raise ValueError("Phone number must have 10 digits after removing country code")

        # Format as (XXX) XXX-XXXX
        formatted = f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
        return formatted

    except Exception as e:
        # Handle invalid input gracefully
        print(f"Error formatting phone number '{phone_number}': {e}")
        return None


# -------------------
# Test cases
# -------------------
if __name__ == "__main__":
    test_numbers = [
        "1234567890",
        "+11234567890",
        "123-456-7890",
        "(123)4567890",
        "1 (234) 567-8901",
        "invalid_number",
        "12345"
    ]

    for number in test_numbers:
        formatted = format_phone_number(number)
        print(f"Original: {number} -> Formatted: {formatted}")
