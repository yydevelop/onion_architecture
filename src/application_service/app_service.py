# src/application_service/app_service.py

import time
from src.domain_service.data_processor import DataProcessor
from src.infrastructure.interface_logger import LoggerInterface

class AppService:
    """
    アプリケーションのフロー制御とエラーハンドリングを行うクラス。
    モードによる処理の切り分けもここで行います。
    """

    def __init__(self, data_processor: DataProcessor, logger: LoggerInterface):
        self.data_processor = data_processor
        self.logger = logger

    def execute(self, mode: str) -> None:
        try:
            if mode == 'persistent':
                while True:
                    self.data_processor.process()
                    self.logger.info('Data processed successfully.')
                    time.sleep(300)  # 5分待機
            elif mode == 'once':
                self.data_processor.process()
                self.logger.info('Data processed successfully.')
            else:
                self.logger.error(f'Invalid mode: {mode}')
        except Exception as e:
            self.logger.error(f'Error processing data: {e}')
            raise e
