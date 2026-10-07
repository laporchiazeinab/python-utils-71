import time
import pyautogui
import logging
from typing import Optional

class AutoClicker:
    """Core logic for automated mouse interaction."""

    def __init__(self, interval: float = 0.1, button: str = 'left'):
        self.interval = interval
        self.button = button
        self.is_running = False
        logging.basicConfig(level=logging.INFO)

    def start(self, duration: Optional[int] = None):
        """Executes click loop for set duration or indefinitely."""
        self.is_running = True
        start_time = time.time()
        logging.info(f"Starting clicker: {self.button} every {self.interval}s")
        
        try:
            while self.is_running:
                pyautogui.click(button=self.button)
                time.sleep(self.interval)
                
                if duration and (time.time() - start_time) > duration:
                    break
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        """Halts current click execution."""
        self.is_running = False
        logging.info("Stopping clicker")

if __name__ == "__main__":
    bot = AutoClicker(interval=0.5)
    bot.start(duration=10)