from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from helpers.service_helpers import get_settings


class Postgres:

    def __init__(self):
        self.db_creds = get_settings()
        self.DATABASE_URL = (f"postgresql+psycopg2://{self.db_creds['postgres']['USER']}:"
                             f"{self.db_creds['postgres']['PASS']}@{self.db_creds['postgres']['HOST']}:"
                             f"{self.db_creds['postgres']['PORT']}/{self.db_creds['postgres']['DBNAME']}")
        self.engine = create_engine(self.DATABASE_URL, pool_size=20, max_overflow=30)

        self.Session = sessionmaker(bind=self.engine)

    def get_connection(self):

        return self.Session()

    @staticmethod
    def execute_custom_query(query, db_session, **kwargs):
        result = db_session.execute(text(query), kwargs)
        db_session.commit()
        return result
