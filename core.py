import pyautogui
import time
import random

def safe_click(x: int, y: int, interval: float = 0.1):
    """Performs a click with randomized jitter to simulate human input."""
    jitter_x = x + random.randint(-2, 2)
    jitter_y = y + random.randint(-2, 2)
    pyautogui.click(jitter_x, jitter_y)
    time.sleep(interval)

def perform_sequence(coords: list, delay: float = 0.5):
    """Executes a list of coordinates sequentially."""
    for x, y in coords:
        safe_click(x, y)
        time.sleep(delay)

def get_screen_center():
    """Calculates the center of the primary screen."""
    width, height = pyautogui.size()
    return width // 2, height // 2

def rapid_click(count: int, interval: float = 0.05):
    """Clicks at the current mouse position multiple times."""
    for _ in range(count):
        pyautogui.click()
        time.sleep(interval)

def wait_random(min_sec: float, max_sec: float):
    """Pauses execution for a random duration to prevent detection."""
    time.sleep(random.uniform(min_sec, max_sec))