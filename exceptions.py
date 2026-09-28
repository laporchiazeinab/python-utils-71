class AutoclickerError(Exception):
    """Base exception for the autoclicker package."""
    pass

class ClickExecutionError(AutoclickerError):
    """Raised when a mouse simulation action fails."""
    pass

class ConfigurationError(AutoclickerError):
    """Raised when settings fail validation."""
    pass

class HardwareInterruptError(AutoclickerError):
    """Raised when user manually aborts execution."""
    pass

class PerformanceThresholdError(AutoclickerError):
    """Raised when loop execution exceeds latency limits."""
    pass

def handle_exception(exc: Exception) -> None:
    """Centralized exception reporting for runtime diagnostics."""
    if isinstance(exc, (AutoclickerError, KeyboardInterrupt)):
        print(f"[CRITICAL] {type(exc).__name__}: {exc}")
    else:
        print(f"[UNEXPECTED] {type(exc).__name__}: {exc}")