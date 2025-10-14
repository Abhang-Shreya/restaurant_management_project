# home/utils.py

from datetime import datetime
from django.utils import timezone
from home.models import DailyOperatingHours

def is_restaurant_open(restaurant):
    """
    Check if the restaurant is currently open based on DailyOperatingHours.
    Returns True if open, False if closed.
    """
    # Get current time and weekday (e.g., 'Monday')
    current_time = timezone.localtime().time()
    current_day = datetime.now().strftime('%A')

    try:
        # Get today's operating hours for the given restaurant
        hours = DailyOperatingHours.objects.get(restaurant=restaurant, day_of_week=current_day)
        if hours.opening_time <= current_time <= hours.closing_time:
            return True
        else:
            return False
    except DailyOperatingHours.DoesNotExist:
        # If no record exists for today, assume closed
        return False
