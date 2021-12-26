import pytest


def test_get_secret(secrets):
    # assert not secrets.storage
    assert secrets('app01_dev', 'db_user') == 'user_app01_dev'
    assert 'app01_dev' in secrets.storage
    assert 'db_user' in secrets.storage['app01_dev']


def test_invalid_secret(secrets):
    secret_id = 'invalid_secret'
    field_id = 'invalid_field'
    with pytest.raises(Exception, match=f'{secret_id} not found in secrets'):
        secrets(secret_id, field_id)


def test_invalid_field(secrets):
    secret_id = 'app01_dev'
    field_id = 'invalid_field'
    with pytest.raises(Exception, match=f'{field_id} not found in {secret_id}'):
        secrets(secret_id, field_id)
