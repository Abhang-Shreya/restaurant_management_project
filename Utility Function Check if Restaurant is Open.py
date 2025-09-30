# File: home/utils.py

from datetime import datetime, time

def is_restaurant_open():
    """
    Checks if the restaurant is currently open based on hardcoded opening hours.
    
    Returns:
        bool: True if open, False if closed.
    """
    # Define restaurant hours (Monday-Friday 9:00 AM - 10:00 PM, closed on weekends)
    opening_hours = {
        0: (time(9, 0), time(22, 0)),  # Monday
        1: (time(9, 0), time(22, 0)),  # Tuesday
        2: (time(9, 0), time(22, 0)),  # Wednesday
        3: (time(9, 0), time(22, 0)),  # Thursday
        4: (time(9, 0), time(22, 0)),  # Friday
        5: None,                        # Saturday closed
        6: None                         # Sunday closed
    }

    now = datetime.now()
    current_day = now.weekday()  # Monday=0, Sunday=6
    current_time = now.time()

    hours = opening_hours.get(current_day)
    
    if hours is None:
        return False  # Closed on this day
    
    open_time, close_time = hours
    return open_time <= current_time <= close_time


# -------------------------
# Simple test when running directly
# -------------------------
if __name__ == "__main__":
    if is_restaurant_open():
        print("Restaurant is OPEN")
    else:
        print("Restaurant is CLOSED")
