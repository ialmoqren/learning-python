import os
from dotenv import load_dotenv

load_dotenv()

# Getting the DB parameters from the .env file
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PWD = os.getenv('MYSQL_PWD')
MYSQL_DB = os.getenv('MYSQL_DB')
print(f"db parameters: {MYSQL_HOST} {MYSQL_USER} {MYSQL_PWD} {MYSQL_DB}")

SQLALCHEMY_DATABASE_URI = f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PWD}@{MYSQL_HOST}:3306/{MYSQL_DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = False
