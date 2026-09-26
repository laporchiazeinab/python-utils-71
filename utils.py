import random
import time
from typing import Tuple, Union


def apply_jitter(x: int, y: int, max_offset: int = 5) -> Tuple[int, int]:
    """Applies human-like random jitter to target coordinates to prevent bot detection."""
    if max_offset <= 0:
        return x, y
    offset_x = random.randint(-max_offset, max_offset)
    offset_y = random.randint(-max_offset, max_offset)
    return x + offset_x, y + offset_y


def get_humanized_delay(base_delay: float, variance_ratio: float = 0.15) -> float:
    """Calculates a dynamic delay by adding a small randomized variance to a base time."""
    if base_delay <= 0:
        return 0.0
    variance = base_delay * max(0.0, min(variance_ratio, 1.0))
    return max(0.001, random.uniform(base_delay - variance, base_delay + variance))


def parse_coordinates(coords_str: str) -> Union[Tuple[int, int], None]:
    """Parses coordinate strings like '1920, 1080' or '1920 1080' safely into integers."""
    cleaned = coords_str.replace(",", " ").strip()
    parts = [part for part in cleaned.split(" ") if part]
    if len(parts) == 2:
        try:
            return int(parts[0]), int(parts[1])
        except ValueError:
            return None
    return None


def sleep_humanized(base_delay: float) -> None:
    """Blocks thread execution using a randomized, human-like delay duration."""
    actual_delay = get_humanized_delay(base_delay)
    time.sleep(actual_delay)
