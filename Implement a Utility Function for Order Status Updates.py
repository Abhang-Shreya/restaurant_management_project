# orders/utils.py

import logging
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from orders.models import Order   # make sure this path is correct

# Configure logger for this module
logger = logging.getLogger(__name__)

def update_order_status(order_id: int, new_status: str) -> bool:
    """
    Utility function to update the status of an order.
    
    Args:
        order_id (int): The ID of the order to update.
        new_status (str): The new status to set (must be a valid choice).
    
    Returns:
        bool: True if the update was successful, False otherwise.
    """
    try:
        with transaction.atomic():
            order = Order.objects.get(id=order_id)
            old_status = order.status

            order.status = new_status
            order.save(update_fields=["status"])

            logger.info(
                f"Order {order_id} status changed from '{old_status}' to '{new_status}'."
            )

        return True

    except ObjectDoesNotExist:
        logger.error(f"Order with ID {order_id} does not exist.")
        return False

    except Exception as e:
        logger.exception(
            f"Unexpected error while updating order {order_id} to status '{new_status}': {e}"
        )
        return False
