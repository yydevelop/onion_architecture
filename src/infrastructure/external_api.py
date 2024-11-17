# src/infrastructure/external_api.py

import requests
from typing import Dict
from src.domain_service.interface_external_api import ExternalAPIInterface

class ExternalAPI(ExternalAPIInterface):
    """
    ExternalAPIInterfaceの具体的な実装クラス。
    """

    def __init__(self, api_url: str):
        self.api_url = api_url

    def get_data(self) -> Dict:
        response = requests.get(self.api_url)
        response.raise_for_status()
        return response.json()
