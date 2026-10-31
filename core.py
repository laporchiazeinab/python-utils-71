import time
import typing as t


class AutoClickerError(Exception):
    """Custom exception raised during autoclicker operations."""
    pass


class ClickEngine:
    """Core engine executing click actions with input validation."""

    def __init__(self, max_rate_hz: float = 100.0) -> None:
        self.max_rate_hz = max_rate_hz
        self.min_interval = 1.0 / max_rate_hz
        self.is_running = False

    def _validate_inputs(self, interval: float, click_type: str, count: int) -> None:
        """Validate click parameters before loop execution."""
        if not isinstance(interval, (int, float)):
            raise TypeError(f"Interval must be numeric, got {type(interval).__name__}")
        if interval < self.min_interval:
            raise ValueError(f"Interval {interval}s exceeds maximum rate ({self.max_rate_hz} Hz)")

        valid_clicks = {"left", "right", "middle", "double"}
        if not isinstance(click_type, str) or click_type.lower() not in valid_clicks:
            raise ValueError(f"Invalid click_type '{click_type}'. Allowed: {valid_clicks}")

        if not isinstance(count, int) or count < 0:
            raise ValueError(f"Count must be a non-negative integer, got {count}")

    def run_loop(self, interval: float, click_type: str = "left", count: int = 0) -> int:
        """Executes the main click loop after validating parameters."""
        self._validate_inputs(interval, click_type, count)
        
        self.is_running = True
        clicks_completed = 0
        click_action = click_type.lower()

        try:
            while self.is_running:
                # Re-check interval integrity inside loop
                if interval <= 0:
                    raise AutoClickerError("Runtime interval corruption detected")

                # Simulate click processing
                time.sleep(min(interval, 0.001))
                clicks_completed += 1

                if count > 0 and clicks_completed >= count:
                    break
        finally:
            self.is_running = False

        return clicks_completed

    def stop(self) -> None:
        """Stop the running click loop."""
        self.is_running = False
