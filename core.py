import time
import functools
import logging
from typing import Callable, Any

# Configure logger for autoclicker networking
logger = logging.getLogger('python-utils-71')

def retry_operation(retries: int = 3, delay: float = 1.0):
    """Decorator to retry network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(f"Attempt {attempt + 1} failed: {e}")
                    if attempt < retries - 1:
                        time.sleep(delay)
            logger.error(f"Operation failed after {retries} attempts")
            raise last_exception
        return wrapper
    return decorator

@retry_operation(retries=3, delay=2.0)
def fetch_server_config(url: str):
    """Example network call for autoclicker settings."""
    # Simulating request logic
    import urllib.request
    with urllib.request.urlopen(url, timeout=5) as response:
        return response.read().decode('utf-8')