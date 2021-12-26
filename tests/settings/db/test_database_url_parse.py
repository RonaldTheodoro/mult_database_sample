from settings.db.database_url_parse import DatabaseUrlParser
from settings.db.database_url_parse import get_database_url_from_secret


def test_database_url_parse_mysql():
    user = 'shimira'
    password = 'xelo'
    port = '9999'
    host = 'localhost'
    name = 'db'
    engine = 'mysql'
    url = f'{engine}+pymysql://{user}:{password}@{host}:{port}/{name}'
    db_parser = DatabaseUrlParser(user, password, port, host, name, engine)

    assert db_parser.user == user
    assert db_parser.password == password
    assert db_parser.port == port
    assert db_parser.host == host
    assert db_parser.name == name
    assert db_parser.engine == f'{engine}+pymysql'
    assert db_parser.url == url


def test_database_url_parse_postgres():
    user = 'shimira'
    password = 'xelo'
    port = '9999'
    host = 'localhost'
    name = 'db'
    engine = 'postgres'
    url = f'postgresql://{user}:{password}@{host}:{port}/{name}'
    db_parser = DatabaseUrlParser(user, password, port, host, name, engine)

    assert db_parser.user == user
    assert db_parser.password == password
    assert db_parser.port == port
    assert db_parser.host == host
    assert db_parser.name == name
    assert db_parser.engine == 'postgresql'
    assert db_parser.url == url


def test_get_database_url_from_secret_mysql():
    url = get_database_url_from_secret('app01_dev')
    url_expected = (
        'mysql+pymysql://user_app01_dev:b2weeL*4#H@localhost:3306/app01_dev'
    )
    assert url == url_expected


def test_get_database_url_from_secret_postgres():
    url = get_database_url_from_secret('app02')
    assert url == 'postgresql://user_app02:vdM?g)Di_J@localhost:5432/app02'
