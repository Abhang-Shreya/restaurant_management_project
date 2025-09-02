import time
import uuid

class SessionManager:
    def __init__(self, expiry_seconds=60):
        # expiry time for each session
        self.expiry_seconds = expiry_seconds
        # in-memory storage for sessions: {session_id: expiry_timestamp}
        self.sessions = {}

    def create_session(self, user_id):
        """Create a new session for a user."""
        session_id = str(uuid.uuid4())  # unique session ID
        expiry_time = time.time() + self.expiry_seconds
        self.sessions[session_id] = {"user_id": user_id, "expiry": expiry_time}
        return session_id

    def is_session_valid(self, session_id):
        """Check if a session is still valid."""
        self.cleanup_sessions()  # remove expired sessions first
        session = self.sessions.get(session_id)
        if session:
            return True
        return False

    def cleanup_sessions(self):
        """Delete all expired sessions automatically."""
        current_time = time.time()
        expired_sessions = [sid for sid, data in self.sessions.items()
                            if data["expiry"] < current_time]
        for sid in expired_sessions:
            del self.sessions[sid]

    def get_active_sessions(self):
        """Return all active sessions."""
        self.cleanup_sessions()
        return self.sessions


# ---------------- DEMO -----------------
if __name__ == "__main__":
    manager = SessionManager(expiry_seconds=10)  # sessions expire in 10 sec
    
    # create a session
    session_id = manager.create_session(user_id=101)
    print("New session created:", session_id)

    # check immediately
    print("Valid now?", manager.is_session_valid(session_id))

    # wait 12 seconds (session will expire)
    time.sleep(12)

    print("Valid after 12 sec?", manager.is_session_valid(session_id))
    print("All active sessions:", manager.get_active_sessions())
