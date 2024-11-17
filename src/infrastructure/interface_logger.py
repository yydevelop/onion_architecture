# src/infrastructure/interface_logger.py

from abc import ABC, abstractmethod

class LoggerInterface(ABC):
    """
    ロガーのインターフェース。
    """

    @abstractmethod
    def info(self, message: str) -> None:
        pass

    @abstractmethod
    def error(self, message: str) -> None:
        pass
