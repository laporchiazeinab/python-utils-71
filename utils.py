import time
import threading

class ClickerController:
    """Handles autoclicker state and timing logic."""
    def __init__(self, interval=0.1):
        self.interval = interval
        self.running = False
        self._lock = threading.Lock()

    def start(self):
        with self._lock:
            self.running = True

    def stop(self):
        with self._lock:
            self.running = False

    def execute_click(self, action_func):
        """Runs the provided action while controller is active."""
        while True:
            with self._lock:
                if not self.running:
                    break
            action_func()
            time.sleep(self.interval)

class InputValidator:
    """Validates autoclicker configuration parameters."""
    @staticmethod
    def validate_interval(value):
        if not isinstance(value, (int, float)) or value < 0.01:
            raise ValueError("Interval must be a float greater than 0.01")
        return True

def format_duration(seconds):
    """Converts seconds into human-readable minute/second format."""
    mins, secs = divmod(int(seconds), 60)
    return f"{mins:02d}m {secs:02d}s"