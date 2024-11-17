# src/infrastructure/file_repository.py

from src.domain_service.interface_file_repository import FileRepositoryInterface
from src.domain_model.data_entity import DataEntity

class FileRepository(FileRepositoryInterface):
    """
    FileRepositoryInterfaceの具体的な実装クラス。
    """

    def __init__(self, file_path: str):
        self.file_path = file_path

    def save(self, data_entity: DataEntity) -> None:
        with open(self.file_path, 'a') as f:
            # ファイルに必要な列のみを保存（idとname）
            f.write(f"{data_entity.id},{data_entity.name}\n")
