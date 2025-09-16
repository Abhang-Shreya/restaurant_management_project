import string
import secrets
from .models import Coupon  # Assuming you have a Coupon model with a `code` field

def generate_coupon_code(length=10):
    """
    Generate a unique alphanumeric coupon code of the given length.
    Checks existing Coupon records to ensure uniqueness.
    """
    characters = string.ascii_uppercase + string.digits

    while True:
        # Generate a random alphanumeric string
        code = ''.join(secrets.choice(characters) for _ in range(length))

        # Check if this code already exists in the database
        if not Coupon.objects.filter(code=code).exists():
            return code
