#views.py
from django.shorcuts import render
from django.http import HttpResponse
from django.urls import path
from .view import index

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, inital-scale=1.0"">
        <tilte>Homepage with News section</title>
        <style> 
            /* Banner Styling*/
            .banner{
                background-color: #d35400; 
                color: white;
                text-algin:center;
                padding: 20px;
                font-size: 24px;
                font-weight: bold;
                font-family: Arail, sans-serif; 
            }
        </style>
    </head>
    <body>

        <!--Banner Section-->
        <div class="banner">
            Welcome to our Restaurant!
        </div>

        <!--Rest of your homepage contact-->
        <p style="text-algin:center; margin-top: 50px;">
            Explore our menu and enjoy delicious meals.
        </p>
    </body>
    </html>
"""
return Httpresponse(html)

#URLs
uulpatterns = [
    path("",index, name="home"),
]