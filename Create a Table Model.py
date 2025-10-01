# File: home/models.py
from django.db import models

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"Table {self.table_number} ({self.location})"
