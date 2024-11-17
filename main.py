# main.py

import json
import sys
from src.ui.user_interface import get_execution_mode
from src.application_service.app_service import AppService
from src.infrastructure.logger import Logger
from src.domain_service.data_processor import DataProcessor
from src.infrastructure.sqlite_data_repository import SQLiteDataRepository
from src.infrastructure.file_repository import FileRepository
from src.infrastructure.external_api import ExternalAPI

def main():
    # 設定情報を読み込み
    with open('config/settings.json', 'r') as f:
        config = json.load(f)

    log_file_path = config['LOG_FILE_PATH']
    api_url = config['API_URL']
    db_connection_string = config['DB_CONNECTION_STRING']
    file_path = config['FILE_PATH']
    db_server_name = config['DB_SERVER_NAME']

    if len(sys.argv) > 1:
        mode = sys.argv[1]
        if mode not in ['persistent', 'once']:
            print("Invalid mode provided. Please enter 'persistent' or 'once'.")
            mode = get_execution_mode()
    else:
        mode = get_execution_mode()

    # インスタンスの生成
    logger = Logger(log_file_path)
    data_repository = SQLiteDataRepository(db_connection_string)
    file_repository = FileRepository(file_path)
    external_api = ExternalAPI(api_url)

    data_processor = DataProcessor(
        data_repository=data_repository,
        file_repository=file_repository,
        external_api=external_api,
        db_server_name=db_server_name
    )

    app_service = AppService(data_processor=data_processor, logger=logger)

    # アプリケーションサービス層でモードによる処理の切り分けを実行
    app_service.execute(mode)

    logger.info("Processing completed.")

if __name__ == '__main__':
    main()
