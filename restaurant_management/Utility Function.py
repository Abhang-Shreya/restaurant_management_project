# utils.py

from typing import List, Optional

# ----------------------
# Simulated Review model
# ----------------------
class Review:
    def __init__(self, review_text: str, rating: int):
        self.review_text = review_text
        self.rating = rating


# ----------------------
# Utility function
# ----------------------
def calculate_average_rating(reviews: List[Review]) -> Optional[float]:
    """
    Calculate the average rating from a list of Review objects.

    Args:
        reviews (List[Review]): A list or queryset of Review objects.

    Returns:
        float: The average rating rounded to 2 decimal places, or None if no reviews.
    """
    if not reviews:
        return None  # no reviews available

    try:
        total = sum(review.rating for review in reviews)
        average = total / len(reviews)
        return round(average, 2)
    except Exception as e:
        print(f"Error calculating average rating: {e}")
        return None


# ----------------------
# Test the function
# ----------------------
if __name__ == "__main__":
    # Sample reviews
    reviews_sample = [
        Review("Great food!", 5),
        Review("Good service.", 4),
        Review("Average experience.", 3),
        Review("Not good.", 2),
    ]

    average_rating = calculate_average_rating(reviews_sample)
    if average_rating is not None:
        print(f"Average rating: {average_rating}")
    else:
        print("No reviews to calculate average rating.")
