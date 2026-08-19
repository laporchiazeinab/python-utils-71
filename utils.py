import time
import random

class AutoClicker:
    def __init__(self, click_interval, click_times):
        self.click_interval = click_interval
        self.click_times = click_times

    def validate_inputs(self):
        if not isinstance(self.click_interval, (int, float)) or self.click_interval <= 0:
            raise ValueError('Click interval must be a positive number.')
        if not isinstance(self.click_times, int) or self.click_times < 1:
            raise ValueError('Click times must be a positive integer.')

    def start_clicking(self):
        self.validate_inputs()
        for _ in range(self.click_times):
            self.perform_click()
            time.sleep(self.click_interval)

    def perform_click(self):
        # Simulate a mouse click
        print('Mouse clicked.')

# Example usage
if __name__ == '__main__':
    clicker = AutoClicker(0.5, 10)
    clicker.start_clicking()