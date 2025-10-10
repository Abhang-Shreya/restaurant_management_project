from django.db import models
from rest_framework import serializers, views, status
from rest_framework.response import Response
from django.urls import path

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
# 3️⃣ API VIEW
# ------------------------------------------------
class TableListCreateView(views.APIView):
    """
    GET  -> List all tables
    POST -> Create a new table
    """

    def get(self, request):
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------------------------------------
# 4️⃣ URLS
# ------------------------------------------------
urlpatterns = [
    path('api/tables/', TableListCreateView.as_view(), name='table-list-create'),
]


# ------------------------------------------------
# 5️⃣ HOW TO TEST (Example)
# ------------------------------------------------
"""
🧩 Setup Instructions

1️⃣ Add this line in your project's main urls.py file:
    from orders.table_api import urlpatterns as table_urls
    urlpatterns += table_urls

2️⃣ Make migrations & migrate:
    python manage.py makemigrations orders
    python manage.py migrate

3️⃣ Run your server:
    python manage.py runserver

4️⃣ Test with Postman or curl:

   ➤ GET  http://127.0.0.1:8000/api/tables/
   ➤ POST http://127.0.0.1:8000/api/tables/

   Example POST body:
   {
       "table_number": 1,
       "capacity": 4,
       "is_available": true
   }

Expected Response:
{
    "id": 1,
    "table_number": 1,
    "capacity": 4,
    "is_available": true
}
"""
