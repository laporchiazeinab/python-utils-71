import random
import re

def parse_interval(interval_str: str) -> float:
    """
    Parses a human-readable interval string and returns duration in seconds.

    Supported formats: "100ms", "1.5s", "500". If no unit is specified,
    it defaults to seconds.

    Args:
        interval_str: The interval string to parse (e.g., '250ms', '2s').

    Returns:
        The duration in seconds as a float.

    Raises:
        ValueError: If the interval string cannot be parsed.
    """
    match = re.match(r"^([\d.]+)\s*(ms|s)?$", interval_str.strip().lower())
    if not match:
        raise ValueError(f"Invalid interval format: {interval_str}")

    value_str, unit = match.groups()
    value = float(value_str)

    if unit == "ms":
        return value / 1000.0
    return value


def calculate_jitter(base_delay: float, jitter_range: float) -> float:
    """
    Applies a random delay variation (jitter) to make clicking behavior more human-like.

    Args:
        base_delay: The baseline delay between clicks in seconds.
        jitter_range: The maximum deviation percentage as a float (e.g., 0.1 for 10%).

    Returns:
        The final delay in seconds including random jitter.
    """
    if jitter_range <= 0:
        return max(0.0, base_delay)

    max_deviation = base_delay * jitter_range
    actual_deviation = random.uniform(-max_deviation, max_deviation)
    return max(0.0, base_delay + actual_deviation)


def validate_coordinate(x: int, y: int, max_x: int, max_y: int) -> bool:
    """
    Validates if target click coordinates fall within safe screen boundaries.

    Args:
        x: The horizontal pixel coordinate.
        y: The vertical pixel coordinate.
        max_x: The maximum allowable screen width resolution.
        max_y: The maximum allowable screen height resolution.

    Returns:
        True if coordinates are within [0, max_dimension], False otherwise.
    """
    return 0 <= x <= max_x and 0 <= y <= max_y
