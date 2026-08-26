import time
import random

def get_current_timestamp() -> float:
    """Return current high-precision timestamp."""
    return time.perf_counter()

def calculate_sleep_interval(base_delay: float, variance: float = 0.05) -> float:
    """Calculate randomized delay to mimic human clicking behavior."""
    jitter = random.uniform(-variance, variance)
    interval = base_delay + (base_delay * jitter)
    return max(0.001, interval)

def human_delay(base_delay: float, variance: float = 0.05) -> None:
    """Sleep for a randomized duration to avoid detection."""
    sleep_time = calculate_sleep_interval(base_delay, variance)
    time.sleep(sleep_time)
