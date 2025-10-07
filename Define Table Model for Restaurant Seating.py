from django.db import models


# -----------------------------
# Cuisine Model
# -----------------------------
class Cuisine(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Cuisines"

    def __str__(self):
        return self.name


# -----------------------------
# MenuItem Model
# -----------------------------
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    # Link to Cuisine
    cuisine = models.ForeignKey(
        Cuisine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="menu_items"
    )

    def __str__(self):
        return self.name


# -----------------------------
# Table Model
# -----------------------------
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"
