# restaurant_app.py
from django.db import models
from django.shortcuts import render
from django.urls import path 

#Model
class OpeningHour(models.Model):
    DAY_CHOICES =[
        ("Monday","Monday"),
        ("Teusday", "Teusday"),
        ("Wednesday", "Wednesday"),
        ("Thursady", "Thursday"),
        ("Friday", "Firday"),
        ("Saturday", "Saturday"),
        ("Sunday",  "Sunday"),
    ]

    day = models.CharField(max_length=10, choices = DAY_CHOICES, unique=True)
    open_time= models.TimeField()
    close_time = models.TimeField

    class Meta:
        ordering = ["list(DAY_CHOICES).index(day)"] #maintain weekday order

    def __str__(self):
        return f"{self.day}: {self.open_time} - {self.close_time}"

#View
def home(request):
    opening_hour = OpeningHour.objects.all()
    return render(request,"home.html",{"opening_hour": opening_hours})

#urls.py

urlpatterns = [
    path("" home, name="home"),
]

#Templates (home.html)
"""
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Homepages</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1 {
            color: #333;
        }
        table{
            width: 300px;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border:1px solid #ccc;
            padding: 8px;
            text-align: center;
        }
        th {
            background: #f2f2f2;
        }
    </style>
</head>
<body>
    <h1>Welcome to Our Restaurant</h1>
    <h2>Opening Hours</h2>
    <table>
        <tr>
            <th>Day</th>
            <th>Open</th>
            <th>Close</th>
        </tr>
        {% for hour in opening_hours %}
        <tr>
            <td>{{ hour.day }}</td>
            <td>{{ hour.open_time|time:"H:i" }}</td>
            <td>{{ hour.close_time|time:"H:i" }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""