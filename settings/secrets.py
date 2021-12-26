import json

from settings import settings


class Secrets:

    __storage = {}

    def __call__(self, secret_id, field_id):
        if not self.is_secret_in_storage(secret_id):
            with (settings.extras / 'secrets.json').open(mode='r') as fp:
                secrets = json.load(fp)

            if secret_id not in secrets:
                raise Exception(f'{secret_id} not found in secrets')

            self.save_in_storage(secret_id, secrets)

        if not self.is_field_in_secret(secret_id, field_id):
            raise Exception(f'{field_id} not found in {secret_id}')

        return self.get_field(secret_id, field_id)

    def get_field(self, secret_id, field_id):
        return self.__storage[secret_id][field_id]

    def is_secret_in_storage(self, secret_id):
        return secret_id in self.__storage

    def is_field_in_secret(self, secret_id, field_id):
        return field_id in self.__storage[secret_id]

    def save_in_storage(self, secret_id, secrets):
        self.__storage[secret_id] = secrets[secret_id]

    @property
    def storage(self):
        return self.__storage
