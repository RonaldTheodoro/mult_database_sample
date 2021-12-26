import pytest

from settings.secrets import Secrets
from settings.db.session import DatabaseConnectionFactory


@pytest.fixture
def secrets():
    return Secrets()


@pytest.fixture
def database_connections():
    return DatabaseConnectionFactory()
