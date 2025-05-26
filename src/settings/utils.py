import logging
from pathlib import Path

def create_logger():
    logger = logging.getLogger(__name__)

    logger.setLevel(logging.INFO)

    file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(Path(__file__).parent / "utils.log", mode="a", encoding="utf-8")
    file_handler.setFormatter(file_format)

    console_format = logging.Formatter('%(levelname)s: %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_format)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger