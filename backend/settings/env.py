import os

from dotenv import load_dotenv

load_dotenv()

class Env:
    # データベース
    MYSQL_USER = os.getenv('MYSQL_USER')
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
    MYSQL_HOST = os.getenv('MYSQL_HOST')
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')
    MYSQL_PORT = os.getenv('MYSQL_PORT')
    MYSQL_TZ = os.getenv('MYSQL_TZ')

    # フロントURL
    APP_URL = os.getenv('APP_URL')