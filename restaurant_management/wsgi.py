# myapp/views.py
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render 

#Homepage view
def home(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Restaurant Homepage</tile>
        <style>
            body {
                font-family: Arial, san-serif;
                text-align: center;
                margin-top: 100px;
                background: #f9f9f9;
            }
            h1{
                color: #333;
            }
            .order-btn{
                display: inline-block;
                padding: 15px 30px;
                font-size: 18px;
                font-weight: bold;
                color: white;
                background: liner-gradient(135eg, #ff6600, #ff3300);
                border: none;
                border-radius: 30px;
                text-decoration: none;
                box-shadow: 0px 4px 6px rgba(0,0,0,0.2);
                transition: all 0.3s ease;
            }
            .order-btn:hover {
                background: linear-gradient(135eg, #ff3300, #cc0000);
                transfrom: scale(1.05);
                box-shadow: 0px 6px 10px rgba(0,0,0,0.3);
            }
        </style>
    </head>
    <body>
            <h1>Welcome to Our Restaurant</h1>
            <a href="/order/" class ="order-btn">Order Now</a>
    </body>
    </html>
    """)

#Order placement page view 
def order_page(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title> Place Your Order</title>
    </head>
    <body style="font-family: Arial; text-align:center; margin-top:100px;">
        <h2>Order Placement Page</h2>
        <p>This is where customer will place their order.</p>
        <a href="/" style="text-decoration:none; color:blue;">⬅️ Back to Home</a>
    </body>
    </html>
    """)

# URLS
urlpatterns = [
    path("",home, name="home"),
    path("order/", order_page, name="order"),
]