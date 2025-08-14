# view.py 
from django.http import HttpRespone
from django.urls import path 
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    restaurant_name = "The Gourmet spot"
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{restaurant_name}</title>
    </head>
    <body>
        <h1>{restaurant_name}</h1>
        <p>Welcome to {restaurant_name}! We're glad to have you here.</p>
    </body>
    </html>
    """
    return HttpRespone(html)

urlpatterns = [
    path('',home),
] + static(settings.SATATIC_URL, document_root=settings.SATATIC_ROOT)