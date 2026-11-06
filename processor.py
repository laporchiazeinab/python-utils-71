import time
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_click_params(interval, iterations):
    """Ensures click settings are within safe operational bounds."""
    if not isinstance(interval, (int, float)) or interval < 0.01:
        raise ValueError("Interval must be a float/int >= 0.01 seconds")
    if not isinstance(iterations, int) or iterations < 0:
        raise ValueError("Iterations must be a non-negative integer")
    return True

def run_autoclicker(interval, iterations):
    """Main processing loop with input validation."""
    try:
        validate_click_params(interval, iterations)
        logger.info(f"Starting autoclicker: {iterations} clicks at {interval}s interval")
        
        count = 0
        while iterations == 0 or count < iterations:
            # Simulate mouse click action
            logger.debug(f"Click action triggered: {count + 1}")
            time.sleep(interval)
            count += 1
            
        logger.info("Process completed successfully")
    except ValueError as e:
        logger.error(f"Validation failed: {e}")
    except KeyboardInterrupt:
        logger.info("Process terminated by user")
    except Exception as e:
        logger.error(f"Unexpected loop error: {e}")

if __name__ == "__main__":
    run_autoclicker(0.5, 10)