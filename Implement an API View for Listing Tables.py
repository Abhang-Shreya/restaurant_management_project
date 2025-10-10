from django.db import models
from rest_framework import serializers, generics
from django.urls import path
from rest_framework.response import Response

# ------------------------------------------------
# 1️⃣ TABLE MODEL
# ------------------------------------------------
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Table {self.table_number} (Capacity: {self.capacity})"


# ------------------------------------------------
# 2️⃣ SERIALIZER
# ------------------------------------------------
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


# ------------------------------------------------
# 3️⃣ VIEW
# ------------------------------------------------
class TableListView(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


# ------------------------------------------------
# 4️⃣ URLS
# ------------------------------------------------
urlpatterns = [
    path('api/tables/', TableListView.as_view(), name='table-list'),
]


# ------------------------------------------------
# 5️⃣ HOW TO TEST (Example)
# ------------------------------------------------
"""
🧩 Setup Instructions

1️⃣ Add this line in your project's main urls.py:
    from orders.table_api import urlpatterns as table_urls
    urlpatterns += table_urls

2️⃣ Run the following commands to apply the model:
    python manage.py makemigrations orders
    python manage.py migrate

3️⃣ Start the server:
    python manage.py runserver

4️⃣ Test API endpoint:
    GET http://127.0.0.1:8000/api/tables/

Example Response:
[
    {
        "id": 1,
        "table_number": 1,
        "capacity": 4,
        "is_available": true
    },
    {
        "id": 2,
        "table_number": 2,
        "capacity": 2,
        "is_available": false
    }
]
"""
