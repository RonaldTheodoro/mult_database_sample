from controllers.app01_controller import App01Controller
from controllers.app02_controller import App02Controller
from settings.db.database_connection_factory import connections

class Controllers:
    controllers = {
        'app01': App01Controller,
        'app02': App02Controller,
    }

    def get_session(self, app, stage=None):
        database = app if stage is None else f'{app}_{stage}'
        session = connections(database)

        controller = self.get_controller(app)
        instance = controller(session, database, stage)
        return instance

    def get_controller(self, app):
        if not self.has_controller_for_app(app):
            raise Exception(f'Controller for {app} not found')
        return self.controllers[app]

    def has_controller_for_app(self, app):
        return app in self.controllers