import pytest

from controllers.get_controllers import Controllers
from settings.secrets import Secrets
from settings.db.database_connection_factory import DatabaseConnectionFactory


@pytest.fixture
def secrets():
    return Secrets()


@pytest.fixture
def database_connections():
    return DatabaseConnectionFactory()


@pytest.fixture
def controllers():
    return Controllers()
