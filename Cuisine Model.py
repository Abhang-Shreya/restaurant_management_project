from django.db import models
from django.utils import timezone

# -----------------------------
# Cuisine Model
# -----------------------------
class Cuisine(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# -----------------------------
# MenuItem Model
# -----------------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.CASCADE, related_name='menu_items', null=True, blank=True)

    def __str__(self):
        return self.name

    def is_daily_special(self):
        """
        Check if this menu item is a special for today's date.
        Returns True if the item is listed in DailySpecial for today.
        """
        today = timezone.now().date()
        return DailySpecial.objects.filter(menu_item=self, date=today).exists()


# -----------------------------
# DailySpecial Model
# -----------------------------
class DailySpecial(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='daily_specials')
    date = models.DateField()

    class Meta:
        unique_together = (('menu_item', 'date'),)
        verbose_name = 'Daily Special'
        verbose_name_plural = 'Daily Specials'

    def __str__(self):
        return f"{self.menu_item.name} - {self.date}"
