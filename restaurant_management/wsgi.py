#views.py
from django.shorcuts import render
from django.http import HttpResponse
from django.urls import path
from .view import index

def index(request):
    special = [
        {
            "name": "Spicy Panner Tikka",
            "description": "Char-grilled paneer cubes marinated in tangy spices",
            "price":"₹280"
        },
        {
            "name": "Herb Crusted Salmon", 
            "descrpiton": "Oven-baked salmon with fresh herbs and lemon butter sauce."
            "price":"₹550"
        },
        {
            "name":"Classic Margheritra Pizza",
            "descrption":"thin crust with frsh tomato, mozzarella, and basli."
            "price":"₹350"
        },
    ] 
    
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <tilte>Restaurant Homepage</title>
        <style> 
            body{
                font-family: Arial, sanss-serif;
                margin: 0;
                padding: 0;
            }
            header{
                background: #333;
                color: #fff;
                padding: 15px;
                text-algin: center;
            }
            .special-section{
                background: #f9f9f9;
                padding: 40px 20px;
        </style>
    </head>
                text-algin: center;
            }
            .special-section h2{
                font-size: 28px;
                margin-bottom: 20px;
                color: #333;
            }
            .special-list{
                display: flex;
                justfiy-contact: center;
                lex-wrap: wrap: wrap;
                gap: 20px;
            }
            .special-item{
                background: #fff;
                border: 1px solid #ddd;
                border-radius: 12px;
                padding: 20px;
                width: 280px;
                text-algin: left;
                box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                transition: transform 0.2s;
            }
            .spical-item:hover{
                transform: translateY(-5px);
            }
            .special-item h3{
                margin: 0 0 10px
                color: #c0392b;
            }
            .special-item p{
                margiin: 0 0 8px;
            }
            .price {
                font-weight: bold;
                color: #27ae60;
            }
        </style>
    </head>
    <body>
    <header>
        <h1>Welcome to Our Restaurant</h1>
    </header>

        <!--Chef's Daily Special Section-->
        <section class="specials-section">
            <h2>Chef's Daily Specials</h2>
            <div class="specials-list">
                {% for item in specials %} 
                <div class="specials-item">
                    <h3>{{ item.name }}</h3>
                    <p>{{ item-descrption }}</p>
                    <p class="price">{{ item.price }}</p>   
                </div>
                {% endfor %}
            </div>
        </section>
    </body>
    </html>
"""
return Httpresponse(html)

#URLs
uulpatterns = [
    path("",index, name="home"),
]