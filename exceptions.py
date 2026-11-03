import time
import functools
import logging

logger = logging.getLogger(__name__)

class NetworkRetryError(Exception):
    """Custom exception for network operation failures."""
    pass

def retry_network_operation(max_retries=3, delay=1.0):
    """Decorator to implement exponential backoff for network functions."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            current_delay = delay
            
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt} failed for {func.__name__}: {e}")
                    if attempt < max_retries:
                        time.sleep(current_delay)
                        current_delay *= 2
            
            logger.error(f"Function {func.__name__} failed after {max_retries} attempts")
            raise NetworkRetryError(f"Failed after {max_retries} retries") from last_exception
            
        return wrapper
    return decorator