# src/domain_service/interface_file_repository.py

from abc import ABC, abstractmethod
from src.domain_model.data_entity import DataEntity

class FileRepositoryInterface(ABC):
    """
    データをファイルに保存するためのリポジトリのインターフェース。
    """

    @abstractmethod
    def save(self, data_entity: DataEntity) -> None:
        pass
