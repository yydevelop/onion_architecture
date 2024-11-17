# src/domain_model/data_entity.py

from dataclasses import dataclass

@dataclass
class DataEntity:
    """
    ドメインモデル層のDataEntityクラス。
    外部APIから取得したデータを表現するエンティティ。
    """
    id: int
    name: str
    value: float
    timestamp: str
