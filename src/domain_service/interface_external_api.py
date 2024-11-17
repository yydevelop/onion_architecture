# src/domain_service/interface_external_api.py

from abc import ABC, abstractmethod
from typing import Dict

class ExternalAPIInterface(ABC):
    """
    外部APIからデータを取得するためのインターフェース。
    """

    @abstractmethod
    def get_data(self) -> Dict:
        pass
