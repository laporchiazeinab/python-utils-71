class AutoclickerError(Exception):
    """Base exception class for all autoclicker modules."""
    pass

class ClickError(AutoclickerError):
    """Raised when a mouse event cannot be processed."""
    def __init__(self, message: str, button: str) -> None:
        super().__init__(f"{message} (button: {button})")
        self.button = button

class ConfigurationError(AutoclickerError):
    """Raised when settings are invalid or missing."""
    def __init__(self, key: str, reason: str) -> None:
        super().__init__(f"Invalid configuration for '{key}': {reason}")
        self.key = key

class DeviceNotFoundError(AutoclickerError):
    """Raised when the input device is disconnected."""
    def __init__(self, device_id: str) -> None:
        super().__init__(f"Device {device_id} not found or unreachable")
        self.device_id = device_id

class ExecutionTimeoutError(AutoclickerError):
    """Raised when a clicking operation exceeds expected duration."""
    def __init__(self, timeout: float) -> None:
        super().__init__(f"Operation timed out after {timeout} seconds")
        self.timeout = timeout