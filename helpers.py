import logging
import pyautogui

# Configure logging for autoclicker runtime errors
logger = logging.getLogger('autoclicker')

def safe_click(x: int, y: int):
    """
    Executes a click at screen coordinates with bounds checking
    and failure handling to prevent automation crashes.
    """
    try:
        screen_width, screen_height = pyautogui.size()
        
        # Validate coordinates are within the primary monitor range
        if not (0 <= x < screen_width and 0 <= y < screen_height):
            logger.error(f"Coordinates ({x}, {y}) out of bounds")
            return False

        # Fail-safe: if pyautogui mouse moves to corner, it raises a FailSafeException
        pyautogui.click(x=x, y=y)
        return True
        
    except pyautogui.FailSafeException:
        logger.critical("Fail-safe triggered: mouse moved to corner")
        return False
    except Exception as e:
        logger.error(f"Unexpected error during click execution: {e}")
        return False

def get_valid_interval(interval: float, min_val: float = 0.01) -> float:
    """
    Ensures click interval is within safe performance limits
    to prevent system resource exhaustion.
    """
    try:
        return max(float(interval), min_val)
    except (ValueError, TypeError):
        logger.warning(f"Invalid interval {interval}, defaulting to {min_val}")
        return min_val