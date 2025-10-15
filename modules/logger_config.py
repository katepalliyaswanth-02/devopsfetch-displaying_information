import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logging(log_path="logs/devopsfetch.log"):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    handler = RotatingFileHandler(log_path, maxBytes=5_000_000, backupCount=5)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger = logging.getLogger("devopsfetch")
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        logger.addHandler(handler)
