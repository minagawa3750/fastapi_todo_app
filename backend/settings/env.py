import os

from dotenv import load_dotenv

load_dotenv()

class Env:
    # データベース
    MYSQL_USER=os.getenv('MYSQL_USER'),
    MYSQL_PASSWORD=os.getenv('MYSQL_PASSWORD'),
    LOCALHOST=os.getenv('LOCALHOST'),
    MYSQL_DATABASE=os.getenv('MYSQL_DATABASE'),
    PORT=os.getenv('PORT')