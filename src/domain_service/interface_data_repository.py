# src/domain_service/interface_data_repository.py

from abc import ABC, abstractmethod
from src.domain_model.data_entity import DataEntity

class DataRepositoryInterface(ABC):
    """
    データをDBに保存するためのリポジトリのインターフェース。
    """

    @abstractmethod
    def save(self, data_entity: DataEntity, db_server_name: str) -> None:
        pass
