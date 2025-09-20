# orders/models.py
from decimal import Decimal, ROUND_HALF_UP
from django.db import models
from django.conf import settings


# ---------------------------
# Utility (inline for demo)
# ---------------------------
def calculate_discount(order_item, order=None):
    """
    Example discount utility.
    Returns the discounted line total.
    Rule: If menu item name contains 'promo', apply 10% off.
    """
    base = (order_item.unit_price or order_item.menu_item.price) * order_item.quantity
    if "promo" in order_item.menu_item.name.lower():
        return (base * Decimal("0.90")).quantize(Decimal("0.01"))
    return base.quantize(Decimal("0.01"))


# ---------------------------
# Models
# ---------------------------
class Order(models.Model):
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="orders",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=32, default="pending")

    def __str__(self):
        return f"Order #{self.id} ({self.status})"

    def calculate_total(self) -> Decimal:
        """
        Calculate the total price of the order after applying discounts.
        Uses the calculate_discount utility for each order item.
        """
        total = Decimal("0.00")
        for oi in self.items.all():
            try:
                line_total = calculate_discount(oi, self)
                line_total = Decimal(line_total)
            except Exception:
                line_total = (oi.unit_price or Decimal("0.00")) * oi.quantity
            total += line_total
        return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    menu_item = models.ForeignKey("home.MenuItem", on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item} (Order #{self.order_id})"

    @property
    def line_total(self):
        return (self.unit_price or Decimal("0.00")) * self.quantity

# Example in Django shell
from orders.models import Order, OrderItem
from home.models import MenuItem
from django.contrib.auth import get_user_model

User = get_user_model()
user = User.objects.first()

# Create order
order = Order.objects.create(customer=user)

# Create menu items
m1 = MenuItem.objects.create(name="Regular Dish", price=100)
m2 = MenuItem.objects.create(name="Promo Dish", price=200)

# Add items to order
OrderItem.objects.create(order=order, menu_item=m1, unit_price=m1.price, quantity=2)
OrderItem.objects.create(order=order, menu_item=m2, unit_price=m2.price, quantity=1)

# Calculate total (applies discount for "Promo Dish")
order.calculate_total()
# -> Decimal('380.00')  # (2*100) + (200 * 0.9)
