import pathlib


class Settings:
    BASE_DIR = pathlib.Path(__file__).parent.parent

    @property
    def extras(self):
        return self.BASE_DIR / 'extras'


settings = Settings()
