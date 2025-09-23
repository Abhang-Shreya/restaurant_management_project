
# home/models.py

from django.db import models
from django.utils import timezone
from datetime import timedelta

class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"Table {self.number} (seats {self.capacity})"


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="reservations")
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    customer_name = models.CharField(max_length=100)

    def __str__(self):
        return f"Reservation for {self.customer_name} at {self.table} from {self.start_time} to {self.end_time}"

    # -----------------------------
    # BUSINESS LOGIC
    # -----------------------------
    @classmethod
    def find_available_slots(cls, table_id, range_start, range_end, slot_length=timedelta(hours=1)):
        """
        Find available time slots for a given table within a date/time range.
        
        Args:
            table_id (int): Table ID to check reservations for.
            range_start (datetime): Start of the search window.
            range_end (datetime): End of the search window.
            slot_length (timedelta): Length of each available slot to suggest.

        Returns:
            list of (datetime, datetime): Available slot start and end times.
        """
        # Get existing reservations for this table within the range
        reservations = cls.objects.filter(
            table_id=table_id,
            end_time__gt=range_start,
            start_time__lt=range_end
        ).order_by("start_time")

        # Track available slots
        available_slots = []
        current_start = range_start

        for res in reservations:
            if current_start + slot_length <= res.start_time:
                available_slots.append((current_start, res.start_time))
            current_start = max(current_start, res.end_time)

        # Final slot after last reservation
        if current_start + slot_length <= range_end:
            available_slots.append((current_start, range_end))

        return available_slots
