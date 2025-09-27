# home/faq_api_example.py

from django.db import models
from django.urls import path
from rest_framework import serializers, generics, pagination
from rest_framework.response import Response
from rest_framework.decorators import api_view

# -------------------
# Models
# -------------------
class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    def __str__(self):
        return self.question

# -------------------
# Serializers
# -------------------
class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']

# -------------------
# Pagination (optional)
# -------------------
class FAQPagination(pagination.PageNumberPagination):
    page_size = 10  # Number of FAQs per page
    page_size_query_param = 'page_size'
    max_page_size = 50

# -------------------
# Views
# -------------------
class FAQListView(generics.ListAPIView):
    """
    API view to return a list of FAQs.
    Supports pagination.
    """
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    pagination_class = FAQPagination

# Optional: function-based view
@api_view(['GET'])
def faq_list(request):
    try:
        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True)
        return Response(serializer.data)
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# -------------------
# URL Routing
# -------------------
urlpatterns = [
    # Class-based view
    path('api/faqs/', FAQListView.as_view(), name='faq-list'),

    # Function-based view alternative
    # path('api/faqs/', faq_list, name='faq-list'),
]
