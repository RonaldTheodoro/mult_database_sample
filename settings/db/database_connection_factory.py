from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings.db.database_url_parse import get_database_url_from_secret


class DatabaseConnectionFactory:
    __engines = {}

    def __call__(self, database):
        engine = self.create_engine(database)
        session = self.create_session(engine)
        return session

    def create_session(self, engine):
        Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        return Session()

    def create_engine(self, database):
        if not self.is_database_in_engines(database):
            url = get_database_url_from_secret(database)
            engine = create_engine(url)
            self.save_engine(database, engine)

        return self.get_engine(database)

    def get_engine(self, database):
        return self.__engines[database]

    def save_engine(self, database, engine):
        self.__engines[database] = engine

    def is_database_in_engines(self, database):
        return database in self.__engines