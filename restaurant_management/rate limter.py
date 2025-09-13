import time

class RateLimiter:
    def __init__(self, max_requests: int, window_size: int):
        self.max_requests = max_requests
        self.window_size = window_size
        self.requests_log = {}  # user_id -> [timestamps]

    def is_allowed(self, user_id: str) -> bool:
        current_time = time.time()
        
        if user_id not in self.requests_log:
            self.requests_log[user_id] = []

        # Filter out requests that are outside the time window
        valid_requests = [
            timestamp for timestamp in self.requests_log[user_id]
            if current_time - timestamp < self.window_size
        ]
        self.requests_log[user_id] = valid_requests

        # Check if user is within the limit
        if len(valid_requests) < self.max_requests:
            self.requests_log[user_id].append(current_time)
            return True
        else:
            return False


# Simulation 
if __name__ == "__main__":
    limiter = RateLimiter(max_requests=5, window_size=10)  # 5 requests per 10 seconds
    user = "user_1"

    for i in range(10):
        allowed = limiter.is_allowed(user)
        print(f"Request {i+1} for {user}: {'✅ Allowed' if allowed else '❌ Blocked'}")
        time.sleep(1)  # wait 1 second between requests
