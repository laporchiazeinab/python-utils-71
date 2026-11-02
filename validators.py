import logging

def validate_click_params(interval: float, duration: float) -> bool:
    """Ensures click parameters are within realistic hardware limits."""
    logger = logging.getLogger('python-utils-71')
    
    if not isinstance(interval, (int, float)) or not isinstance(duration, (int, float)):
        logger.error("Invalid type: interval and duration must be numeric")
        return False
        
    if interval < 0.01:
        logger.warning("Interval too low, clamping to 0.01s to prevent system freeze")
        return False
        
    if duration < 0:
        logger.error("Duration cannot be negative")
        return False
        
    return True

def validate_coordinates(x: int, y: int, screen_width: int, screen_height: int) -> bool:
    """Checks if coordinates fall within active screen bounds."""
    logger = logging.getLogger('python-utils-71')
    
    if not (0 <= x <= screen_width and 0 <= y <= screen_height):
        logger.error(f"Coordinates ({x}, {y}) out of screen bounds")
        return False
        
    return True

def validate_input_config(config: dict) -> bool:
    """General validation for configuration dictionaries."""
    required = ['interval', 'duration', 'x', 'y']
    return all(key in config for key in required)