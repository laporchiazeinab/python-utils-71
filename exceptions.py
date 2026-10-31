"""Custom exceptions for autoclicker configuration and execution handling."""

import time
from typing import Optional, Any


class AutoClickerError(Exception):
    """Base exception class for all autoclicker errors."""

    def __init__(self, message: str, details: Optional[Any] = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details
        self.timestamp = time.time()

    def to_dict(self) -> dict:
        """Convert exception metadata to a dictionary for logging."""
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "details": self.details,
            "timestamp": self.timestamp,
        }


class InvalidConfigurationError(AutoClickerError):
    """Raised when click intervals, targets, or settings are invalid."""
    pass


class TargetNotFoundError(AutoClickerError):
    """Raised when standard screen target or pixel condition is not met."""
    pass


class HotkeyConflictError(AutoClickerError):
    """Raised when hotkey binding fails or collides with system bindings."""
    pass


class ExecutionPermissionError(AutoClickerError):
    """Raised when OS blocks automated mouse or keyboard event injection."""
    pass
