from config.settings import settings

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbConfig:

    @staticmethod
    def get_db(self):
        db_config = f"mysql+pymsql://{settings.DB_USER_NAME}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
        db_engine = create_engine(db_config)
        db_session = sessionmaker( bind=db_engine   )
        return db_session()

    