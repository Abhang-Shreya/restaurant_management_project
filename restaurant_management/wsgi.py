# contact_page.py

from django.http import HttpRespone
from django.urls import path

def contact_us(request): 
    html_content = """   
    <!DOCTYPE html>
    <html="en">
    <head>
        <meta charest="UTF-8">
        <title>
            Contact Us
        </title>
        <style>
            body{
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                margin: 0;
                padding: 0;
            }

            .container {
                max-width: 600px;
                margin: 50px auto;
                background-color: white
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                text-align: center;
            }

            h1 {
                margin-top: center;
                color: #333; 
            }

            .info {
                margin-top: 20px;
            }

            .info p {
                margin: 8px 0;
                font-size: 16px;
                color: #555;
            }

            .info strong{
                color: #000;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Contact Us</h1>
            <div class="info">
                <p><strong>Address:</strong>123 Food street, pune, India<p>
                <p><strong>Phone:</strong> +91 98765 43210</p>
                <p><strong>Email:</strong>contact@myrestaurant.com</p>
            </div>
        </div>
    </body>
    </html>
    """
    return HttpRespone(html_content)

urlpatterns = [
    path('contact/', contact_us)
]