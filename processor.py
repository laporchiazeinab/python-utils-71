import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('processor')

def validate_inputs(clicks: int, interval: float) -> bool:
    """Ensures click count and interval are positive values."""
    if not isinstance(clicks, int) or clicks <= 0:
        logger.error(f'Invalid click count: {clicks}')
        return False
    if not isinstance(interval, (int, float)) or interval < 0.01:
        logger.error(f'Invalid interval: {interval}')
        return False
    return True

def run_autoclicker(clicks: int, interval: float):
    """Main processing loop with input validation."""
    if not validate_inputs(clicks, interval):
        return

    logger.info(f'Starting {clicks} clicks with {interval}s delay')
    
    try:
        for i in range(clicks):
            # Simulating click event
            logger.info(f'Performing click {i + 1}/{clicks}')
            time.sleep(interval)
    except KeyboardInterrupt:
        logger.info('Processing interrupted by user')

if __name__ == '__main__':
    run_autoclicker(5, 0.5)