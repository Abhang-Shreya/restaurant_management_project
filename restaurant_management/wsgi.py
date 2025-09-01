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
        <tilte>Restaurant Website</title>
        <style> 
            body{
                font-family: Arial, sanss-serif;
                margin: 0;
                padding: 0;
            }
            header footer {
                background-color: #333;
                color: white;
                padding: 15px;
                display: flex;
                justify-contact: space-between;
                text-algin: center;
            }
            .search-bar{
                display: flex;
            }
            .search-bar input[type="text"{
                padding: 8px;
                border: none;
                border-radius: 4px 0 0 4px;
                outline: none;
            }
            .search-bar button{
                padding: 8px 12px;
                border: none;
                background-color: #ff6600;
                color: white;
                border-radius: 0 4px 4-x 0;
                cursor: pointer;
            }
            .serch-bar button:hover{
                background-color: #e65c00;
            }
        </style>
    </head>
    <body>

    <!--Header with Search Bar-->
    <header>
        <h1>My Restaurant</h1>
        <form class="serch-bar" action='#' method="get">
            <input tpye="text" placeholder="Search menu...">
            <button type="submit">Search</button>
        </form>
    </header>

    <main style="padding:20px;">
        <h2>Welcome!</h2>
        <p>Explore our delicious menu and daily specials.</p>
    </main>

        <!--Footer with Search Bar-->
        <footer>
            <p>&copy; 2025 My Resaturant</p>
            <form class="search-bar" action="#" method="get">
                <input type="text" placeholder="Search menu...">
                <button type="submit">Search</button>
            </form>
        </footer>
    </body>
    </html>
"""
return Httpresponse(html)

#URLs
uulpatterns = [
    path("",index, name="home"),
]