import time

class SessionManager:
    def __init__(self, expiry_seconds):
        """
        Initialize the session manager with a session expiry time.
        :param expiry_seconds: Time (in seconds) after which a session expires.
        """
        self.expiry_seconds = expiry_seconds
        self.sessions = {}  # { session_id: creation_time }

    def create_session(self, session_id):
        """
        Create a new session with the given session_id.
        """
        self.sessions[session_id] = time.time()
        print(f"Session '{session_id}' created at {self.sessions[session_id]}")

    def is_session_active(self, session_id):
        """
        Check if the session is still active.
        If expired, remove it and return False.
        """
        if session_id not in self.sessions:
            return False

        creation_time = self.sessions[session_id]
        current_time = time.time()
        if current_time - creation_time < self.expiry_seconds:
            return True
        else:
            # Session expired — delete it
            del self.sessions[session_id]
            print(f"Session '{session_id}' expired and removed.")
            return False

    def delete_session(self, session_id):
        """
        Delete a session manually.
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
            print(f"Session '{session_id}' deleted manually.")
            return "Deleted"
        else:
            return "Not Found"


# =========================
# Example Usage / Test Code
# =========================
if __name__ == "__main__":
    sm = SessionManager(expiry_seconds=5)

    # Create a session
    sm.create_session("user123")

    # Check immediately
    print("Active?", sm.is_session_active("user123"))  # Expected: True

    # Wait 3 seconds (still active)
    time.sleep(3)
    print("Active after 3s?", sm.is_session_active("user123"))  # Expected: True

    # Wait 3 more seconds (total 6s — should expire)
    time.sleep(3)
    print("Active after 6s?", sm.is_session_active("user123"))  # Expected: False

    # Try deleting an already expired session
    print("Delete result:", sm.delete_session("user123"))  # Expected: Not Found

    # Create another session and delete it manually before expiry
    sm.create_session("user456")
    print("Delete result:", sm.delete_session("user456"))  # Expected: Deleted
    print("Active?", sm.is_session_active("user456"))  # Expected: False