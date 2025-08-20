# view.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse =("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Restaurant Homepage</title>
        <style>
            body {
                font-family: "Segoe UI", Tahoma, sans-serif;
                margin: 0;
                padding: 0;
                background: #fafafa;
                color: #333;
            }
            header {
                color: white;
                padding: 2rem 1rem;
                background-color: #8B0000;/* deep red */
                text-align: center;
            }
            header h1 {
                margin: 0;
                font-size: 2.5rem;
            }
            .tagline {
                margin-top: 0.5rem;
                font-size: 1.2rem;
                font-style: italic;
                opacity: 0.9;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>Welcome to Our Restaurant</h2>
            <p class="tagline">"where every bite tells a story."</p>
        </header>
    </body>
    </html>
    """)