from sqlalchemy.engine.base import Engine


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