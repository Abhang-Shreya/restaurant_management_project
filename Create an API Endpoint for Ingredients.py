from django.db import models
from rest_framework import serializers, viewsets
from rest_framework.routers import DefaultRouter
from django.urls import path, include

# ------------------------------------------------
# 1️⃣ INGREDIENT MODEL
# ------------------------------------------------
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    unit_of_measure = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.unit_of_measure})"


# ------------------------------------------------
# 2️⃣ SERIALIZER
# ------------------------------------------------
class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'unit_of_measure']


# ------------------------------------------------
# 3️⃣ VIEWSET
# ------------------------------------------------
class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


# ------------------------------------------------
# 4️⃣ URL ROUTING
# ------------------------------------------------
router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet, basename='ingredient')

urlpatterns = [
    path('api/', include(router.urls)),
]


# ------------------------------------------------
# 5️⃣ HOW TO TEST (Example)
# ------------------------------------------------
"""
🧩 Setup Instructions

1️⃣ Add this line in your project's main urls.py:
    from home.ingredient_api import urlpatterns as ingredient_urls
    urlpatterns += ingredient_urls

2️⃣ Run database migrations:
    python manage.py makemigrations home
    python manage.py migrate

3️⃣ Start your Django development server:
    python manage.py runserver

4️⃣ Test API endpoints:

   ➤ GET  http://127.0.0.1:8000/api/ingredients/
   ➤ POST http://127.0.0.1:8000/api/ingredients/
   ➤ GET  http://127.0.0.1:8000/api/ingredients/1/
   ➤ PUT  http://127.0.0.1:8000/api/ingredients/1/
   ➤ DELETE  http://127.0.0.1:8000/api/ingredients/1/

Example POST body:
{
    "name": "Tomato",
    "unit_of_measure": "kg"
}

Expected Response:
{
    "id": 1,
    "name": "Tomato",
    "unit_of_measure": "kg"
}
"""
