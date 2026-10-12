class AutoclickerError(Exception):
    """Base exception for the autoclicker module."""
    pass

class ClickExecutionError(AutoclickerError):
    """Raised when the OS level click operation fails."""
    pass

class HardwareInputError(AutoclickerError):
    """Raised when hardware input simulation is restricted."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised when autoclicker parameters are invalid."""
    pass

class PerformanceThresholdError(AutoclickerError):
    """Raised when internal timing cycles exceed latency limits."""
    pass

def raise_if_slow(latency: float, threshold: float = 0.016):
    """Performance check to ensure frame timing stays under 16ms."""
    if latency > threshold:
        raise PerformanceThresholdError(f"Cycle latency {latency:.4f}s exceeded {threshold}s limit")

class ErrorHandler:
    """Centralized error handling for performance-critical execution loops."""
    @staticmethod
    def handle(e: Exception):
        if isinstance(e, PerformanceThresholdError):
            print(f"[PERF WARNING] {e}")
        else:
            print(f"[CRITICAL ERROR] {type(e).__name__}: {e}")