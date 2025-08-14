# view.py 

from django.conf import settings
from django.shortcuts import render
from django.db import models

#Model
class RestaurantInfo(models.Model):
    name = models.CharField(max_lenght=100)
    phone = models.CharField(max_lenght=15)

    def __str__(self):
        return self.name
    
#View
def home(request):
    #Try geeting phone from settings
    phone_number = getattr(settings, "RESTAURANT_PHONE", nONE)

    # If not in setting, try database
    if not phone_number:
        restaurnt_info = RestaurantInfo.objects.first()
        phone_number= restaurnt_info.phone if restaurnt_info else "Not available"

    return render(request, "home.html", {"phone_number": phone_number})

#setting.py
#Add in your setting file (this is just for refernce)
#RESTAURANT_PHONE ="+91 98765 43210"

# Template(home.html)
"""
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Hompage</title>
</head>
<body>
    <h1>Welcome to Our Resturant</h1>
    </p>Phone: {{ phone_number }}</p>
</body>
</html>