# src/infrastructure/logger.py

import logging
from src.infrastructure.interface_logger import LoggerInterface

class Logger(LoggerInterface):
    """
    ロガーの具体的な実装クラス。
    """

    def __init__(self, log_file_path: str):
        self.logger = logging.getLogger('app_logger')
        self.logger.setLevel(logging.INFO)
        fh = logging.FileHandler(log_file_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(fh)

    def info(self, message: str) -> None:
        self.logger.info(message)

    def error(self, message: str) -> None:
        self.logger.error(message)
