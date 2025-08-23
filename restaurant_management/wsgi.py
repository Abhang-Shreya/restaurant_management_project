# restaurant_app
from djano.core.paginator import paginator
from django.shortcuts import render
from django.db import models

#Model
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

#View
def menu(request):
    item_list = MenuItem.objects.all().order_by("id")#fetch all items

    paginator = Paginator(item_list, 5) # 5 items per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "menu.html", {"page_obj": page_obj})

#urls.py
from django.urls import path
from . import views 

urlpatterns = [
    path("menu/", views.menu, name="menu"),
]

#Template/menu.html
"""
<!DOCTYPE html>
<html>
<head>
    <title>Menu</title>
    <style>
        .pagination {
            margin: 40px;
            display: flex;
            gap: 10px;
        }
        .paginationn a, .paginationation span  {
            padding: 25px;
            border: 1px solid #ddd;
            text-decortion: none;
        }
        .pagination .current {
            background: #007BFF;
            color: white;
        }
    </style>
</head>
<body>
    <h1>Menu</h1>
    {% for item in page_obj %}
        <div>
            <h3>{{ item.name }} - ${{ item.price }}</h3>
            <p>{{ item.decrition }}</p>
        </div>
        <hr>
    {% empty %}
        <p>No menu item available.</p>
    {% endfor %}

    <!-- Pagination Controls -->
    <div class="pagination">
        {% if page_obj.has_previous %}
            <a href="?page=1">Frist</a>
            <a herf="?page={{ page-obj.previous_page_number }}">Previous</a>
        {% endif %}

        <span class="current">Page {{ page_obj.number }}of {{ page_obj.paginator.num-pages }}</span
            
        {% if page_obj.has_next %}
            <a herf="?page={{ page_obj.next_page_number }}">Next</a>
            <a herf="?page={{ page_obj.paginator.num_pages }}">Last</a>
        {% endif %}
    </div>
</body>
</html>
"""