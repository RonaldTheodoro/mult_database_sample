from sqlalchemy.engine.base import Engine
from sqlalchemy.orm.session import Session


def test_create_engine_mysql(database_connections):
    engine = database_connections.create_engine('app01_dev')
    assert isinstance(engine, Engine)
    assert engine.driver == 'pymysql'
    assert engine.name == 'mysql'


def test_create_engine_postgres(database_connections):
    engine = database_connections.create_engine('app02')
    assert isinstance(engine, Engine)
    assert engine.driver == 'psycopg2'
    assert engine.name == 'postgresql'


def test_create_session_mysql(database_connections):
    session = database_connections.create_session('app01_dev')
    assert isinstance(session, Session)
    assert session.bind.driver == 'pymysql'
    assert session.bind.name == 'mysql'


def test_create_session_postgres(database_connections):
    session = database_connections.create_session('app02')
    assert isinstance(session, Session)
    assert session.bind.driver == 'psycopg2'
    assert session.bind.name == 'postgresql'
