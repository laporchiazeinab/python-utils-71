import time
from functools import wraps

def retry(max_retries=3, delay=1, backoff=2, exceptions=(Exception,)):
    """Apply retry logic to network operations."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == max_retries - 1:
                        raise
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator

# Simulated network function for demonstration
@retry(max_retries=4, delay=0.5, exceptions=(ConnectionError,))
def perform_network_operation(endpoint):
    """Performs a network call with retry on failure."""
    import random
    if random.random() > 0.3:
        raise ConnectionError("Simulated network failure")
    return f"Data retrieved from {endpoint}"

if __name__ == "__main__":
    try:
        result = perform_network_operation("https://api.example.com/data")
        print(result)
    except ConnectionError:
        print("Operation failed after all retries")
