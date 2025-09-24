from django.db import models
from django.urls import path
from django.http import JsonResponse

# ------------------------
# Model
# ------------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    discount_percentage = models.FloatField(default=0.0)  # % discount (0–100)

    def get_final_price(self) -> float:
        """
        Calculate the final price considering discount.
        Example: if price=100 and discount=10, final=90
        """
        if self.discount_percentage > 0:
            discount_amount = (self.discount_percentage / 100) * self.price
            return round(self.price - discount_amount, 2)
        return float(self.price)

    def __str__(self):
        return f"{self.name} - {self.get_final_price()} after discount"


# ------------------------
# Quick Test API (for demo)
# ------------------------
def test_menu_item(request):
    # Example: Create a menu item (not saved in DB, just in memory for demo)
    burger = MenuItem(name="Cheese Burger", price=200.0, discount_percentage=15.0)
    final_price = burger.get_final_price()
    return JsonResponse({
        "item": burger.name,
        "original_price": burger.price,
        "discount": burger.discount_percentage,
        "final_price": final_price
    })


# ------------------------
# URL Pattern
# ------------------------
urlpatterns = [
    path('test-menu-item/', test_menu_item, name='test-menu-item'),
]
