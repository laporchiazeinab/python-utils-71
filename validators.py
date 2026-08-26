import time

class ValidationError(Exception):
    """Raised when input parameters fail validation."""
    pass

def validate_click_interval(interval: float) -> float:
    """Ensure the click interval is within safe and practical bounds."""
    try:
        parsed_interval = float(interval)
    except (TypeError, ValueError):
        raise ValidationError(f"Invalid interval type: {interval}. Must be a number.")

    if parsed_interval < 0.01:
        raise ValidationError(f"Interval {parsed_interval}s is too fast. Minimum is 0.01s.")
    
    if parsed_interval > 3600.0:
        raise ValidationError(f"Interval {parsed_interval}s is too slow. Maximum is 3600.0s.")

    return parsed_interval

def validate_coordinates(x: int, y: int) -> tuple[int, int]:
    """Validate screen coordinates for the autoclicker."""
    try:
        parsed_x = int(x)
        parsed_y = int(y)
    except (TypeError, ValueError):
        raise ValidationError(f"Invalid coordinates: ({x}, {y}). Must be integers.")

    if parsed_x < 0 or parsed_y < 0:
        raise ValidationError(f"Coordinates cannot be negative: ({parsed_x}, {parsed_y}).")

    return parsed_x, parsed_y

def validate_loop_arguments(interval: float, x: int, y: int) -> tuple[float, int, int]:
    """Validate all parameters required for the main processing loop."""
    validated_interval = validate_click_interval(interval)
    validated_x, validated_y = validate_coordinates(x, y)
    return validated_interval, validated_x, validated_y
