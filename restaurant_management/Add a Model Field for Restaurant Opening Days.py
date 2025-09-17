# home/models.py
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    operating_days = models.CharField(
        max_length=100,
        help_text="Comma-separated list of operating days (e.g., Mon,Tue,Wed,Thu,Fri)"
    )

    def __str__(self):
        return self.name
