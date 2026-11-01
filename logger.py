import logging
from logging.handlers import RotatingFileHandler
import os

# Logger configuration for autoclicker tracking
LOG_FILE = "autoclicker.log"
MAX_BYTES = 1 * 1024 * 1024  # 1MB per file
BACKUP_COUNT = 3

def setup_logger(name: str = "python-utils-71") -> logging.Logger:
    """Configures a rotating file logger for session tracking."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # File handler with rotation logic
        file_handler = RotatingFileHandler(
            LOG_FILE, 
            maxBytes=MAX_BYTES, 
            backupCount=BACKUP_COUNT
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Optional console output for debugging
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger