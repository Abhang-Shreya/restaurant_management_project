#view.py 
from django.http import HttpRespnse
from django.urls import path

#View
def menu_list(request):
    menu_items = [
        {"id":1, "name": "Margherita Pizza", "price": 299},
        {"id":2, "name": "Veggie Burger", "price":199},
        {"id":3, "name": "Pasta Alfredo", "price": 249},
    ]
    return JsonResponse(menu_items, safe=False)

#URL Config

urlpatterns =[
    path('api/menu/', menu_list, name='menu-list'),
]