# src/infrastructure/sqlite_data_repository.py

from src.domain_service.interface_data_repository import DataRepositoryInterface
from src.domain_model.data_entity import DataEntity
import sqlite3

class SQLiteDataRepository(DataRepositoryInterface):
    """
    SQLiteを使用したDataRepositoryInterfaceの具体的な実装クラス。
    """

    def __init__(self, db_connection_string: str):
        self.db_connection_string = db_connection_string
        self.conn = sqlite3.connect(self.db_connection_string)
        self.cursor = self.conn.cursor()
        # テーブルが存在しない場合は作成
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS data_table (
                id INTEGER PRIMARY KEY,
                name TEXT,
                value REAL,
                timestamp TEXT,
                db_server_name TEXT
            )
        ''')

    def save(self, data_entity: DataEntity, db_server_name: str) -> None:
        self.cursor.execute('''
            INSERT INTO data_table (id, name, value, timestamp, db_server_name) VALUES (?, ?, ?, ?, ?)
        ''', (data_entity.id, data_entity.name, data_entity.value, data_entity.timestamp, db_server_name))
        self.conn.commit()
