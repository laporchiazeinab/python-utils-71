import time
import pyautogui
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('handler')

def click_at_position(x: int, y: int, interval: float = 0.1):
    """Perform a click at specific screen coordinates."""
    try:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(interval)
    except Exception as e:
        logger.error(f'Click operation failed at ({x}, {y}): {e}')

def perform_sequence(points: list[tuple[int, int]], delay: float = 0.5):
    """Execute a series of clicks from a list of coordinates."""
    for x, y in points:
        click_at_position(x, y)
        time.sleep(delay)

def get_mouse_position() -> tuple[int, int]:
    """Retrieve current mouse cursor coordinates."""
    return pyautogui.position()

def safe_exit():
    """Gracefully terminate process execution."""
    logger.info('Shutting down handler operations')
    exit(0)