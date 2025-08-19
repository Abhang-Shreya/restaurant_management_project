from django.shortcuts import render
from django.urls import path

#View for About page
def homepage(request):
    # Retrive cart from session (or set empty cart if not exist)
    cart = request from session (or set empty cart if not exist)

    #calculate total quantity of items 
    total_items = sum(cart.values())
    
    context ={
        "restaurant_name": "Delicious Bites",
        "welcome_message": "Welcome to Delicious Bites!",
        "cart_count": total_item,
    }
    return render(request, "home.html", context)

# Example view to add item to cart (for testing/demo)
def add_to_cart(request,item_id):
    cart = request.session.get("cart",{})

    #increase quantity for item_id
    cart[item_id]= cart.get(item_id, 0) + 1

    #Save cart back into session
    request.session["cart"] = cart

    return render(request, "cart_added.html", {"item_id": item_id})

#urls.py
urlpatterns = [
    path("", homepage, name="homepage"),
    path("add-to-cart/<int:item_id>/", add_to_cart, name="add_to_cart"),
]

#templates/about.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ restaurant_name }}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: ##fafafa; }
        .header { display: flex; justify-contact: space-between; align-item: center; }
        .card { background: #b22222; color: white; padding: 8px 12px; border-radius: 6px; }
    </style>
</head>
<body>
    <div class="header">
        <h1> {{ reataurant_name }}</h1>
        <div class="crat">
            🛒 cart: {{ cart_count }} item{{ cart_count|plurslize }}
        </div>
    </div>

    <p>{{ welcome_message }}</p>

    </p>Try adding item to your cart here:</p>
    <ul>
        <li><a herf="{% url 'add_to_cart' 1 %}">Add Item 1 </a></li>
        <li><a href="{% url 'add_to_cart' 2 %}">Add Item 2 </a></li>
    </ul>
</body>
</html>
"""

#template/cart_added.html
"""
<!DOCTYPE html>
<head>
    <title>Item Added</title>
</head>
<body>
    <h2>Item {{ item_id }} added to cart!</h2>
    <a href= "{% url 'homepage' %}">Return to Homepage</a>
</body>
</html>
"""