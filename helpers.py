import logging

# Configure logging for the autoclicker module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('python-utils-71')

def validate_click_params(interval: float, duration: int) -> bool:
    """
    Validates input parameters for the main clicking loop.
    Ensures timing values are non-negative and within reasonable bounds.
    """
    try:
        if not isinstance(interval, (int, float)) or not isinstance(duration, int):
            raise ValueError("Parameters must be numeric")
        
        if interval < 0.01:
            logger.warning("Interval too small, defaulting to 0.01s to prevent system freeze")
            return False
            
        if duration < 0:
            logger.error("Duration cannot be negative")
            return False
            
        return True
    except Exception as e:
        logger.error(f"Validation failure: {e}")
        return False

def sanitize_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> tuple:
    """
    Clamps coordinates to ensure clicks occur within screen bounds.
    """
    x = max(0, min(x, screen_width))
    y = max(0, min(y, screen_height))
    return x, y

def log_status(message: str):
    """
    Standardized output formatter for the processing loop.
    """
    logger.info(f"[AUTOCLICKER-71] {message}")