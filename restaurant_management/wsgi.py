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
        <tilte>Newsletter Signup</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                background: #fafafa;
                margin: 0;
                padding: 0;
                display: 0;
                display: flex;
                justify-contact: center;
                algin-items: center;
                hegiet: 100vh;
            }

            .newsletter {
                background: white;
                padding: 20px 30px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                text-algin: center;
                width: 300px;
            }

            .newsletter h2{
                margin-bottom: 15px;
            }

            .newsletter input[type="email]{
                width: 100%;
                padding: 10px;
                margin-bottom: 15px;
                border: 1px solid #ccc;
                border-radius: 6px;
                font-size: 14px;
            }

            .newsletter button {
                width: 100px;
                padding: 10px;
                background: #007BFF;
                color: white;
                border: none;
                border-radius: 6px;
                font-size: 16px;
                cusrsor: pointer;
                transition: background 0.3s; 
            }

            .newsletter button:hover{
                background: #0056b3;
            }
        </style>
    </head>
    <body>

        <div class="newsletter">
            <h2>Subscribe to our Newsletter</h2>
            <form>
                <input type="email" placeholder="Enter your email" required>
                <button type="submit">Subscribe</button>
            </form>
        </div>
    </body>
    </html>
"""
return Httpresponse(html)

#URLs
uulpatterns = [
    path("",index, name="home"),
]