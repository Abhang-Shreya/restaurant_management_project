from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Order


@api_view(["GET"])
def get_order_status(request, order_id):
    """
    Retrieve the current status of an order by its ID.
    """
    order = get_object_or_404(Order, id=order_id)
    return Response(
        {
            "order_id": order.id,
            "status": order.status
        },
        status=status.HTTP_200_OK
    )

from django.urls import path
from . import views

urlpatterns = [
    path("status/<int:order_id>/", views.get_order_status, name="get_order_status"),
]