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
        <style>
            body {{
                font-family: Arial, Helvetica,sans-serif;
                background-color: #faf3e0;
                margin: 0;
                padding: 0;
                color: #333;
            }}
            header{{
                background-color: #c0392b;
                color: white;
                padding: 20px;
                text-align: center;
            }}
            h1 {{
                margin: 0;
                font-size: 2.5rem;
            }}
            main {{
                padding: 20px;
                text-align: center;
            }}
            p{{
                font-size: 1.1rem;
                margin-top: 10px;
            }}
        </style>
    </head>
    <body>
        <header>
            <h1>{restaurant_name}</h1>
        </header>
        <p>Welcome to {restaurant_name}! We're glad to have you here.</p>
    </body>
    </html>
    """
    return HttpRespone(html)

urlpatterns = [
    path('',home),
] + static(settings.SATATIC_URL, document_root=settings.SATATIC_ROOT)