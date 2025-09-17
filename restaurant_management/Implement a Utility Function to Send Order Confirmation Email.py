import logging
from django.core.mail import send_mail, BadHeaderError
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.conf import settings
from smtplib import SMTPException

# Configure logger
logger = logging.getLogger(__name__)

def send_order_confirmation_email(order_id, customer_email, customer_name, order_total):
    """
    Sends an order confirmation email to the given customer.

    Args:
        order_id (str or int): The unique ID of the order.
        customer_email (str): The customer's email address.
        customer_name (str): The customer's name.
        order_total (str or float): Total amount of the order.

    Returns:
        bool: True if email sent successfully, False otherwise.
    """
    # Validate the email address
    try:
        validate_email(customer_email)
    except ValidationError:
        logger.error(f"Invalid email address provided: {customer_email}")
        return False

    # Compose email content
    subject = f"Order Confirmation - Order #{order_id}"
    message = (
        f"Hello {customer_name},\n\n"
        f"Thank you for your order!\n"
        f"Your order ID is {order_id}.\n"
        f"Total Amount: ₹{order_total}\n\n"
        "We will notify you once your order is shipped.\n\n"
        "Best regards,\n"
        "Your Company Name"
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [customer_email]

    # Try to send the email
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False
        )
        logger.info(f"Order confirmation email sent to {customer_email} for order {order_id}")
        return True

    except BadHeaderError:
        logger.error(f"Bad header found while sending email to {customer_email}")
    except SMTPException as e:
        logger.error(f"SMTP error while sending email to {customer_email}: {e}")
    except Exception as e:
        logger.error(f"Unexpected error while sending email to {customer_email}: {e}")

    return False
