import logging

# Configure logger for module
logger = logging.getLogger(__name__)

def validate_click_params(interval: float, iterations: int) -> bool:
    """Validates autoclicker configuration parameters."""
    try:
        if not isinstance(interval, (int, float)) or interval < 0.01:
            logger.error(f"Invalid interval: {interval}. Must be >= 0.01s")
            return False
        
        if not isinstance(iterations, int) or (iterations < -1):
            logger.error(f"Invalid iterations: {iterations}. Must be >= -1")
            return False
            
        return True
    except Exception as e:
        logger.exception(f"Unexpected validation error: {e}")
        return False

def sanitize_input(value: str) -> str:
    """Ensures input strings are stripped and safe for parsing."""
    return str(value).strip()

# Main loop integration example usage snippet:
# if not validate_click_params(interval, count):
#     raise ValueError("Configuration failed validation checks")