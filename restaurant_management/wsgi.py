# shopping_cart_app.py
# Run this as part of a Django project 

from django.http import Httpresponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import path
from myapp.view import homepage

# Model
class TodaySpecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

#view
def homepage(request):
    specials = TodaySpecial.objects.all()

    # Inline template (instead of a separate HTML file)
    template_string="""
<!DOCTYPE html>
<html>
<head>
    <title>Restaurant Homepage </title>
    <style>
        body {
            font-family: Arial, sans-serif; 
            margin: 20px;
        }
        h1{
            color: darkgreen;
        }
        .specials{
            display: grid;
            grid-template-columns: 1fr 1fr; gsp: 20px;
        }
        .card {
            padding: 15px;
            border: 1px solid #ddd;
            border-radius: 10px;
            box-shadow: 2px 2px 6px rgBA(0,0,0,0.1);
        }
        .price{
            font-weight: bold;
            color: darkred;
        }
    </style>
</head>
<body>
    <h1>Welcome to Our Restaurant</h1>
    <h2>Today's Special</h2>
    <div class="special">
        {% for item in specials %}
        <div class="card">
            <h3>{{ item.name }}</h3>
            <p>{{ item.description }}</p>
            <p class="price">${{ item.price }}</p>
        </div>
    {% empty %}
        <p>No Special available today.</p>
    {% endfor %}
    </div>
</body>
</html>
"""
django_engine = engines['django']
template = django_engine.from_string(template_string)
return HttpResponse(template.render({'special': special}, request))

#URLS
urlpatterns = [
    path('', homepage, name='home'),
]