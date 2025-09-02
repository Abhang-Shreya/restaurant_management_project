#views.py
from django.shorcuts import render
from django.http import HttpResponse
from django.urls import path
from .view import views

def thank_you(request):
    return render(request, 'thank_you.html')
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <tilte>Thank You</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                padding: 0;
                text-align: center;
            }

            .thank-you {
                background: #f9f9f9;
                padding: 20px 30px;
                border-radius: 10px;
                display: 30px;
                box: inline-block;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            }

            h1 {
                color: green;
            }
        </style>
    </head>
    <body>

        <div class="thank-you">
            <h1>Thank You!</h1>
            <p>Your order has been placed successfully.</p>
            <a href="/">Back to Home</a>
        </div>
    </body>
    </html>
"""
return Httpresponse(html)

#URLs
uulpatterns = [
    path("thank-you/",views.thank_you, name="thank-you"),
]