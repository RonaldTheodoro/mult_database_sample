import pytest

from settings.secrets import Secrets


@pytest.fixture
def secrets():
    return Secrets()
