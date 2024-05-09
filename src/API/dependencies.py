from API.db import DB
from config import db_url

db = DB(db_url, echo=True)