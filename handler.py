import time
import pyautogui
import random

def perform_click(x: int, y: int, interval: float = 0.0) -> None:
    """Executes a mouse click at specified coordinates."""
    pyautogui.click(x, y)
    if interval > 0:
        time.sleep(interval)

def perform_random_move(x_range: tuple, y_range: tuple) -> None:
    """Moves mouse to random coordinates within provided ranges."""
    target_x = random.randint(x_range[0], x_range[1])
    target_y = random.randint(y_range[0], y_range[1])
    pyautogui.moveTo(target_x, target_y, duration=0.2)

def safe_exit_check(key: str = 'q') -> bool:
    """Checks for user exit signal during loop execution."""
    try:
        import keyboard
        return keyboard.is_pressed(key)
    except ImportError:
        return False

def delay_execution(base: float, jitter: float = 0.1) -> None:
    """Pauses execution with randomized jitter for human-like behavior."""
    sleep_time = base + random.uniform(-jitter, jitter)
    time.sleep(max(0, sleep_time))