# myapp/views.py
from django.http import HttpResponse
from django.urls import path, reverse
import random

#VIEW
def order_confirmation(request):
    order_number = random.randint(1000,9999)
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF_8">
        <title>Order Order Confirmation</tile>
        <style>
            body {{
                font-family: Arial, san-serif;
                text-align: center;
                margin-top: 80px;
            }}
            .confirmation-box {{
                display: inline-block;
                padding: 20px 40px;
                border: 2px solid #4CAF50;
                border-radius: 10px;
                background: #f9fff9;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            h1{{
                color: #4CAF50
            }}
            p {{
                font-size: 18px;
            }}
        </style>
    </head>
    <body>
        <div class="confirmation-box">
            <h1>✅ Order Confirmed</h1>
            <p>THANK YOU FOE YOUR PURCHASE.</p>
            <p>Your order number is : <strong>#{order_number}</strong></p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)

# URLS
urlpatterns = [
    path("order/confirmation/", order_confirmation, name="order_confirmation"),
]