from sqlalchemy import text
from src.database import db, DATABASE
from src.news.models import News
from src.tags.models import Tags


with db.engine.connect() as connection:
    connection.execute(text(f'CREATE DATABASE IF NOT EXISTS {DATABASE}'))


try:
    News().__table__.create(db.engine)
except:
    print('уже создано')

try:
    Tags().__table__.create(db.engine)
except:
    print('уже создано')
