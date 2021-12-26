from settings import secrets


class DatabaseUrlParser:
    __user = None
    __password = None
    __port = None
    __host = None
    __name = None
    __engine = None

    def __init__(self, user, password, port, host, name, engine):
        self.__user = user
        self.__password = password
        self.__port = port
        self.__host = host
        self.__name = name
        self.__engine = engine

    @property    
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    @property
    def port(self):
        return self.__port

    @property
    def host(self):
        return self.__host

    @property
    def name(self):
        return self.__name

    @property
    def engine(self):
        engine = self.__engine
        if engine == 'mysql':
            engine = f'{engine}+pymysql'
        elif engine == 'postgres':
            engine = 'postgresql'
        return engine

    @property
    def url(self):
        engine = self.engine
        user = self.user
        password = self.password
        host = self.host
        port = self.port
        name = self.name
        return f'{engine}://{user}:{password}@{host}:{port}/{name}'


def get_database_url_from_secret(secret_id):
    user = secrets(secret_id, 'db_user')
    password = secrets(secret_id, 'db_password')
    port = secrets(secret_id, 'db_port')
    host = secrets(secret_id, 'db_host')
    name = secrets(secret_id, 'db_name')
    engine = secrets(secret_id, 'db_engine')
    db_parser = DatabaseUrlParser(user, password, port, host, name, engine)
    return db_parser.url