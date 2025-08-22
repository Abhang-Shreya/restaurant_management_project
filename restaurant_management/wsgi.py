# shopping_cart_app.py
# Run this as part of a Django project 

from django.http import Httpresponse, HttpresponseRedirect
from django.shortcuts import render, redirect
from django.urls import path

# Dumppy menu item 
MENU_ITEMS =[
    {"id":1, "name": "Pizza","price":250},
    {"id":2, "name": "burger", "price":150};
    {"id":3, "name": "pasta", "price": 200},
]

#Homepage - menu
def menu(request):
    return render(request, "menu.html", {"menu": MENU_ITEMS})

#Add item to cart 
def add_to_cart(request, item_id):
    cart = request.session.get("cart", {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session["cart"] = cart 
    return redirect("menu")

#View cart
def view_cart(request):
    cart =request.session.get("cart",{})
    cart_items = []
    total = 0

    for item_id, qty in cart.item():
        for menu_item in MENU_ITEMS:
            if menu_item["id"] == int(item_id):
                subtotal = menu_item["price"]* qty
                cart_items.append({
                    "name": menu_item["name"],
                    "price":menu_item["price"],
                    "qyt":qyt,
                    "subtotal":subtotal,
                })

return render(request, "cart.html",{"cart_item": cart_items, "total": total})

#lear cart 
def clear_cart(request):
    request.session["cart"] = {}
    return redirect("view_cart")

#URLS
urlpatterns = [
    path("/", menu, name="menu"),
    path("add/<int:item_id>/", add_to_cart, name="add_to_cart"),
    path("cart/", view_cart, name="view_cart"),
    path("clear/", clear_cart, name="clear_cart"),
]

#Templates
#put these template in "template"folder

#template/menu.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Menu</title>
</head>
<body>
    <h1>Menu</h1>
    <ul>
        {% for item in menu %}
        <li>
            {{ item.name }} - ${{ item.price }}
            <a herf="{% url 'add_to_cart' item.id%}>Add to cart</a>
        </li>
        {% endfor%}
    </ul>
    <a herf="{% url 'view_cart' %}>View Cart </a>
</body>
</html>
"""

# templates/cart.html
"""
<!DOCTYPE html>
<html>
<head>
    <title></title>
</head>
<body>
    <h1>Shopping Cart</h1>
    {% if cart_items %}
        <ul>
        {% for item in cart_items %}
            <li>{{ item.name }} (x{{ item.qty }}) - ${{ item.subtotal }}</li>
        {% endfor %}
        </ul>
        <h3> Total: ${{ total }}</h3>
        <a href="{% url 'clear_cart' %}">Clear Cart </a>
    {% else %}
        <p>Your cart is empty. </p>
    {% endif %}
    <br>
    <a herf="{% url 'menu' %}">Back to Menu</a>
</body>
</html>
"""