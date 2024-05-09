import os

DB_HOST = os.environ.get("DB_HOST")
DB_NAME = os.environ.get("DB_NAME")
DB_PASS = os.environ.get("DB_PASS")
DB_USER = os.environ.get("DB_USER")

db_url = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}'
