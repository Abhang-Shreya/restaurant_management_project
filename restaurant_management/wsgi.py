from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

#View for About page
def about_view(request):
    context ={
        "restaurant_name": "Delicious Bites",
        "history": "Founded in 2010, Delicious Bites stareted as a small family-owned cafe and grew into a popular restaurant loved by the community",
        "mission": "To serve fresh, high-quality meals made with love and local ingredients.",
        "vision": "To be the go-to place for comfort food and warm hospitality.",
    }
    return render(request, "about.html", context)

#urls.py
urlpatterns = [
    path("about/", about_view, name="about"),
]

#templates/about.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About Us- {{ restaurant_name }}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; background: ##fafafa; color: #333;}
        h1 { color: #b22222; }
        .section { margin-bottom: 20px; }
        .card { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }
    </style>
</head>
<body>
    <h1>About {{ reataurant_name }}</h1>

    <div class="card section">
        <h2>Our Histroy</h2>
        <p>{{ histroy }}</p>
    </div>

    <div class="card section">
        <h2>Our Mission</h2>
        <p>{{ mission }} </p>
    </div>

    <div claa="card section">
        <h2>Our Vision</h2>
        <p>{{ vision }}</p>
</body>
</html>
"""