import re

# ------------------------
# Utility Function
# ------------------------
def is_valid_email(email: str) -> bool:
    """
    Validate email address using regex.
    Returns True if valid, False otherwise.
    """
    if not isinstance(email, str):
        return False

    # Basic email regex (covers most valid formats)
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


# ------------------------
# Quick Test (can be removed in production)
# ------------------------
if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "user.name+tag@example.co.uk",
        "invalid-email@",
        "another@domain",
        "good.email@domain.com"
    ]

    for email in test_emails:
        print(f"{email} -> {is_valid_email(email)}")
