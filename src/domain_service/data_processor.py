# src/domain_service/data_processor.py

from src.domain_service.interface_data_repository import DataRepositoryInterface
from src.domain_service.interface_file_repository import FileRepositoryInterface
from src.domain_service.interface_external_api import ExternalAPIInterface
from src.domain_model.data_entity import DataEntity

class DataProcessor:
    """
    ビジネスロジックを実行するクラス。
    """

    def __init__(
        self,
        data_repository: DataRepositoryInterface,
        file_repository: FileRepositoryInterface,
        external_api: ExternalAPIInterface,
        db_server_name: str
    ):
        self.data_repository = data_repository
        self.file_repository = file_repository
        self.external_api = external_api
        self.db_server_name = db_server_name

    def process(self) -> None:
        # 外部APIからデータを取得
        data = self.external_api.get_data()
        # DataEntityを作成
        data_entity = DataEntity(**data)
        # DBに保存（DBサーバ名を追加）
        self.data_repository.save(data_entity, self.db_server_name)
        # ファイルに保存
        self.file_repository.save(data_entity)
