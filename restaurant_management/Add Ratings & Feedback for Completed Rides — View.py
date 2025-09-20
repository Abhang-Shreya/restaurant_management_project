# rides/feedback_api.py
from django.db import models, transaction
from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

# If you're using SimpleJWT, import it; otherwise replace with your JWT auth class
from rest_framework_simplejwt.authentication import JWTAuthentication

# --------------------------
# Models (replace with your own models if needed)
# --------------------------
User = get_user_model()

class Ride(models.Model):
    STATUS_REQUESTED = "REQUESTED"
    STATUS_ACCEPTED = "ACCEPTED"
    STATUS_IN_PROGRESS = "IN_PROGRESS"
    STATUS_COMPLETED = "COMPLETED"
    STATUS_CANCELLED = "CANCELLED"

    STATUS_CHOICES = [
        (STATUS_REQUESTED, "Requested"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_IN_PROGRESS, "In progress"),
        (STATUS_COMPLETED, "Completed"),
        (STATUS_CANCELLED, "Cancelled"),
    ]

    rider = models.ForeignKey(User, related_name="rides_as_rider", on_delete=models.CASCADE)
    driver = models.ForeignKey(User, related_name="rides_as_driver", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default=STATUS_REQUESTED)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def mark_completed(self):
        self.status = self.STATUS_COMPLETED
        self.completed_at = timezone.now()
        self.save(update_fields=["status", "completed_at"])


class Feedback(models.Model):
    ride = models.ForeignKey(Ride, related_name="feedbacks", on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # 1..5
    comment = models.TextField(blank=True, null=True)
    submitted_by = models.ForeignKey(User, related_name="submitted_feedbacks", on_delete=models.CASCADE)
    is_driver = models.BooleanField(default=False)  # True if the feedback was submitted by the driver about the rider
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # optional DB-level safeguard: one feedback per user per ride
        unique_together = ("ride", "submitted_by")

# --------------------------
# Serializer
# --------------------------
class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("id", "ride", "rating", "comment", "submitted_by", "is_driver", "created_at")
        read_only_fields = ("id", "ride", "submitted_by", "is_driver", "created_at")

    rating = serializers.IntegerField(min_value=1, max_value=5)

    def validate(self, attrs):
        # Nothing else to validate here because view enforces ride/user relationship.
        # Keep this hook for extensibility (e.g., disallow certain words in comments).
        return attrs

# --------------------------
# View
# --------------------------
class RideFeedbackView(APIView):
    """
    POST /api/ride/feedback/<ride_id>/
    Body:
    {
      "rating": 4,
      "comment": "Great ride!"
    }
    """
    authentication_classes = [JWTAuthentication]  # use your project's auth if different
    permission_classes = [IsAuthenticated]

    def post(self, request, ride_id, *args, **kwargs):
        user = request.user

        # 1. Validate that the ride exists
        try:
            ride = Ride.objects.select_related("rider", "driver").get(pk=ride_id)
        except Ride.DoesNotExist:
            return Response({"error": "Ride not found."}, status=status.HTTP_404_NOT_FOUND)

        # 2. Ensure ride is COMPLETED
        if ride.status != Ride.STATUS_COMPLETED:
            return Response({"error": "Feedback can only be submitted for completed rides."},
                            status=status.HTTP_400_BAD_REQUEST)

        # 3. Ensure request.user is either the rider or driver for that ride
        is_rider = (ride.rider_id == user.id)
        is_driver = (ride.driver_id == user.id)
        if not (is_rider or is_driver):
            return Response({"error": "You are not authorized to submit feedback for this ride."},
                            status=status.HTTP_403_FORBIDDEN)

        # 4. Determine if feedback from that user already exists
        already_exists = Feedback.objects.filter(ride=ride, submitted_by=user).exists()
        if already_exists:
            return Response({"error": "You have already submitted feedback for this ride."},
                            status=status.HTTP_400_BAD_REQUEST)

        # 5. Build serializer data and save
        serializer = FeedbackSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Attach ride, submitted_by, is_driver then save within transaction
        try:
            with transaction.atomic():
                feedback_obj = Feedback(
                    ride=ride,
                    rating=serializer.validated_data["rating"],
                    comment=serializer.validated_data.get("comment", "").strip() or None,
                    submitted_by=user,
                    is_driver=is_driver,
                )
                feedback_obj.save()
        except Exception as exc:
            # catch DB integrity error (e.g., unique_together race) or other failures
            return Response({"error": "Failed to submit feedback.", "details": str(exc)},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({"message": "Feedback submitted successfully."}, status=status.HTTP_201_CREATED)

# --------------------------
# URL pattern (example)
# --------------------------
# In your app's urls.py you can wire it like:
#
# from django.urls import path
# from .feedback_api import RideFeedbackView
#
# urlpatterns = [
#     path('api/ride/feedback/<int:ride_id>/', RideFeedbackView.as_view(), name='ride-feedback'),
# ]
#
# And ensure your project's REST_FRAMEWORK and SimpleJWT are configured (example settings snippet below).
#
# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework_simplejwt.authentication.JWTAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     ),
# }
#
# Simple JWT setup (in settings.py)
# from datetime import timedelta
# SIMPLE_JWT = {
#     'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
#     # other config...
# }
#
# If you already have Ride and Feedback models elsewhere, import them instead and remove the model definitions above.
