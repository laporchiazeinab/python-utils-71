import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger(name='autoclicker', log_file='app.log', level=logging.INFO):
    """
    Configures a rotating file logger for the autoclicker process.
    Keeps 5 files of 1MB each.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if re-initialized
    if not logger.handlers:
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        # Rotate logs after 1MB, keeping max 5 backups
        file_handler = RotatingFileHandler(
            log_file, maxBytes=1*1024*1024, backupCount=5
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Stream logs to console as well
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Instance for global application usage
app_logger = setup_logger()