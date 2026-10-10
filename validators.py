import logging

# Configure logger for input validation
logger = logging.getLogger(__name__)

def validate_click_params(interval, repeat):
    """Ensures click parameters are within safe ranges."""
    try:
        # Verify interval is a positive number
        interval_float = float(interval)
        if interval_float < 0.01:
            logger.warning("Interval too low, defaulting to 0.01s")
            interval_float = 0.01
        
        # Verify repeat count is valid
        repeat_int = int(repeat)
        if repeat_int < -1:
            raise ValueError("Repeat count must be -1 for infinite or >= 0")
            
        return interval_float, repeat_int
    except (ValueError, TypeError) as e:
        logger.error(f"Invalid configuration detected: {e}")
        return 0.1, 1

def validate_coordinates(x, y):
    """Checks if provided screen coordinates are logical."""
    try:
        x_val, y_val = int(x), int(y)
        if x_val < 0 or y_val < 0:
            logger.warning("Negative coordinates clamped to zero")
            return max(0, x_val), max(0, y_val)
        return x_val, y_val
    except (ValueError, TypeError):
        logger.error("Non-numeric coordinates provided, defaulting to 0,0")
        return 0, 0