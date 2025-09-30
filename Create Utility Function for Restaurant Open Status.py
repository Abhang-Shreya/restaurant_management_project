from datetime import datetime, time

# ----------------------------------------
# Utility Function: Check if restaurant is open
# ----------------------------------------
def is_restaurant_open():
    """
    Returns True if the restaurant is currently open, False otherwise.
    Opening hours are hardcoded for now.
    """

    # Get the current time and day
    now = datetime.now()
    current_day = now.strftime("%A")  # e.g., 'Monday', 'Tuesday'
    current_time = now.time()

    # Define opening hours (example schedule)
    # Monday to Friday: 9 AM - 10 PM
    # Saturday and Sunday: 10 AM - 11 PM
    opening_hours = {
        "Monday": (time(9, 0), time(22, 0)),
        "Tuesday": (time(9, 0), time(22, 0)),
        "Wednesday": (time(9, 0), time(22, 0)),
        "Thursday": (time(9, 0), time(22, 0)),
        "Friday": (time(9, 0), time(22, 0)),
        "Saturday": (time(10, 0), time(23, 0)),
        "Sunday": (time(10, 0), time(23, 0)),
    }

    # Get today's opening and closing times
    opening_time, closing_time = opening_hours.get(current_day, (None, None))

    # Safety check (in case the day isn't found)
    if not opening_time or not closing_time:
        return False

    # Check if the current time is within operating hours
    if opening_time <= current_time <= closing_time:
        return True
    else:
        return False


# ----------------------------------------
# (Optional) Test the function manually
# ----------------------------------------
if __name__ == "__main__":
    status = is_restaurant_open()
    print("Restaurant is open!" if status else "Restaurant is closed.")
