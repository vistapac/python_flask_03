import os
import importlib
from flask import Blueprint, request
import logging
from flask_jwt_extended import jwt_required, get_jwt

def register_blueprints(app):
    logger = logging.getLogger('API_Logger')

    # 設定日誌
    logging.basicConfig(level=logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    file_handler = logging.FileHandler('apiRequests.log', encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # 掃描 routes 目錄下的所有 py 文件
    routesDir = os.path.dirname(__file__)
    for filename in os.listdir(routesDir):
        if filename.endswith('.py') and filename != '__init__.py':  #取得 __init__.py 以外的 .py 檔
            module_name = f'routes.{filename[:-3]}' #去掉 user.py 的 .py 後，併接 routes. + user 成 routes.user。用來導入。
            module = importlib.import_module(module_name)   #導入
            register_blueprint_with_logging(app, module, logger)

def register_blueprint_with_logging(app, module, logger):
    for attr in dir(module):    #dir(module) 獲取 module 中所有的屬性名稱。
        obj = getattr(module, attr) #根據 attr 的值，從 module 中獲取對應的屬性對象。
        if isinstance(obj, Blueprint):  #尋找屬於 Blueprint 對象的屬性。
            if not hasattr(obj, '_logged'): #檢查 obj 是否有名為 _logged 的屬性
                obj.before_request(lambda: log_request_info(logger))
                obj.after_request(lambda response: log_response_info(logger, response))
                obj._logged = True  # 添加一個標記，表示已經設置過日誌功能
            app.register_blueprint(obj, url_prefix='/api')


def log_request_info(logger):
    logger.info(f"Path: {request.path}")
    logger.info(f"Method: {request.method}")
    logger.info(f"Request Data: {request.get_data(as_text=True).encode('utf-8')}")
    logger.info(f"Request Args: {request.args}")
    
    @jwt_required()
    def log_jwt_info():
        jwt_data = get_jwt()
        logger.info(f"JWT Info: {jwt_data}")
    
    try:
        log_jwt_info()
    except Exception as e:
        logger.info(f"No JWT found in request: {e}")

def log_response_info(logger, response):
    logger.info(f"Response Status: {response.status}")
    logger.info(f"Response Data: {response.get_data(as_text=True).encode('utf-8')}")
    return response
