from django.db import models

# Cuisine model to categorize menu items
class Cuisine(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Cuisines"

    def __str__(self):
        return self.name


# MenuItem model — now linked to Cuisine
class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

    # Link each MenuItem to a Cuisine type
    cuisine = models.ForeignKey(
        Cuisine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="menu_items"
    )

    def __str__(self):
        return self.name
