import pytest

from settings.secrets.get_secrets import Secrets


@pytest.fixture
def secrets():
    return Secrets()
