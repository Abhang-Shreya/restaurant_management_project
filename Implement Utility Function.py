# home/models_and_utils.py

from django.db import models

# -------------------------
# Table Model
# -------------------------
class Table(models.Model):
    table_number = models.CharField(max_length=10, unique=True)
    capacity = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"


# -------------------------
# Utility Function
# -------------------------
def get_available_tables_by_capacity(num_guests):
    """
    Returns all tables that are available and can accommodate the given number of guests.

    Args:
        num_guests (int): Number of guests to seat.

    Returns:
        QuerySet: A Django QuerySet of available Table objects.
    """
    available_tables = Table.objects.filter(
        is_available=True,
        capacity__gte=num_guests
    )
    return available_tables


# -------------------------
# Example Usage (Django Shell)
# -------------------------
if __name__ == "__main__":
    # This part only works in Django shell after setting up Django environment
    tables = get_available_tables_by_capacity(4)
    for table in tables:
        print(table.table_number, table.capacity)

