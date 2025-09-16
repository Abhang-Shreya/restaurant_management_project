import logging
import re
from email.utils import parseaddr
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

# Configure logger
logger = logging.getLogger(__name__)

# Regex to validate email structure
EMAIL_REGEX = re.compile(r"^[^@]+@[^@]+\.[^@]+$")


def is_valid_email(email: str) -> bool:
    """
    Validate an email address using Python's built-in email parsing utilities.
    Returns True if valid, False otherwise.
    """
    try:
        if not email or not isinstance(email, str):
            return False

        # Parse the email into (name, address)
        name, addr = parseaddr(email)

        # Check if address part matches typical email structure
        if EMAIL_REGEX.match(addr):
            return True
        return False

    except Exception as e:
        # Log any unexpected errors
        logger.error(f"Error validating email '{email}': {e}")
        return False


@csrf_exempt
@require_POST
def submit_email(request):
    """
    Example view to demonstrate using the is_valid_email utility function.
    """
    email = request.POST.get('email')

    if not is_valid_email(email):
        return JsonResponse({'error': 'Invalid email address'}, status=400)

    # Here you would normally process or save the email
    # ...

    return JsonResponse({'message': 'Email accepted'})

