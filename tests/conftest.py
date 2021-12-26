import pytest

from settings.secrets import Secrets
from settings.db.session import DatabaseConnections


@pytest.fixture
def secrets():
    return Secrets()


@pytest.fixture
def database_connections():
    return DatabaseConnections()
