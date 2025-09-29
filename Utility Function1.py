from django.db import models

# ----------------------------
# MODEL
# ----------------------------
class Review(models.Model):
    restaurant_name = models.CharField(max_length=255)
    rating = models.FloatField()  # Rating between 1.0 and 5.0
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.restaurant_name} - {self.rating}"

# ----------------------------
# UTILITY FUNCTION
# ----------------------------
def calculate_average_rating(reviews_queryset):
    """
    Calculates the average rating of all restaurant reviews.
    Args:
        reviews_queryset: Django QuerySet of Review objects.
    Returns:
        float: Average rating value.
    """

    try:
        total_reviews = reviews_queryset.count()

        # Handle case where no reviews exist
        if total_reviews == 0:
            return 0.0

        # Sum up all ratings
        total_rating = sum(review.rating for review in reviews_queryset)

        # Calculate and return the average rating
        average_rating = total_rating / total_reviews
        return round(average_rating, 2)

    except Exception as e:
        # Gracefully handle unexpected errors
        print(f"Error calculating average rating: {e}")
        return 0.0
