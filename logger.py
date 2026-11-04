import sys
import os
import logging
from datetime import datetime
from typing import Optional


class AutoclickerLogger:
    """Configures and manages logging for autoclicker operations with edge-case handling."""

    def __init__(self, log_dir: str = "logs", default_level: int = logging.INFO):
        self.log_dir = log_dir
        self.default_level = default_level
        self.logger = logging.getLogger("AutoclickerLogger")
        self.logger.setLevel(self.default_level)
        self._setup_handlers()

    def _setup_handlers(self) -> None:
        """Sets up file and stream handlers, handling permission and path edge cases."""
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Standard console output handler as basic fallback
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # Handle file system creation errors gracefully
        try:
            os.makedirs(self.log_dir, exist_ok=True)
            log_file = os.path.join(self.log_dir, f"autoclicker_{datetime.now():%Y%m%d}.log")
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        except (PermissionError, OSError) as err:
            self.logger.warning(f"Failed to create log file: {err}. Falling back to console logging.")

    def log_action(self, action_name: str, x: Optional[int] = None, y: Optional[int] = None) -> None:
        """Logs clicker actions while handling invalid coordinate values."""
        try:
            if x is not None and y is not None:
                msg = f"Action: {action_name} at ({x}, {y})"
            else:
                msg = f"Action: {action_name}"
            self.logger.info(msg)
        except Exception as err:
            self.logger.error(f"Failed to format log entry for '{action_name}': {err}")

    def log_error(self, message: str, exc: Optional[Exception] = None) -> None:
        """Safely logs operational errors and exceptions."""
        if exc:
            self.logger.error(f"{message} | Exception: {type(exc).__name__}: {exc}")
        else:
            self.logger.error(message)
