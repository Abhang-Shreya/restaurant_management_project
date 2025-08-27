# view.py
from django.shorcuts import render

# Examplae menu item 
MENU_ITEMS = [
    {"name": "Margherita Pizza", "price": "$9},
    {"name": "Pasta Alfredo", "price":"$10"},
    {"name": "Caesar salad", "price":"$7"},
    {"name": "panner Tikka", "price":"$8"},
]

def menu(request):
    query = request.GET.get("q", "")
    if query:
        filtered_items = [item for item in MENU_ITEMS if query.lower()in item["name"].lower()]
    else:
        filtered_items = MENU_ITEMS
    
    return render(request, "menu.html", {"menu_items": filtered_items, "query": query})

def menu_view(request):
    template_code ="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title> Menu</tilte>
    <style>
        body{
            font-family: Arial, sans-serif;
            background-color: #fafafa;
            padding: 20px;
        }
        h2{
            text-align: center;
            margin-bottom: 30px;
        }
        .menu-container{
            display: grid;
            grid-template-coloums: repect(auto-fill, minmax(250px, 1fr));
            gap: 20px;
        }
        .menu-item{
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: transform 0.2s ease;
        }
        .menu-item:hover{
            transform: scale(1.03);
        }
        .menu-item h2{
            margin-top: 0;
            font-size: 1.4em;
            color: #333;
        }
        .menu-item p {
            margin:5px;
            color: #666;
        }
        .price{
            font-wegiht:bold;
            color: #000;
            margin-top: 10px;
            display: inline-block;
            background: #f8f8f8;
            padding: 5px 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <h1>Our Menu</h1>
    <div class="menu-container">
        {% for item in menu-items %}
            <div class="menu-item">
                <h2>{{ item.name }}</h2>
                <p>{{ item.description }}</p>
                <span class="price">{{ item.price }}</span>
            </div>
        {% endfor %}
    </div>
</body>
</html>
"""
django_engine = engine['django']
template = django_engine.form_strings(template_code)
return HttpResponse(template.render({"menu_item": MENU_ITEMS}))