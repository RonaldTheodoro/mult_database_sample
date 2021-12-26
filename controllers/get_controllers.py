from controllers.app01_controller import App01Controller
from controllers.app02_controller import App02Controller


class Controllers:
    controllers = {
        'app01': App01Controller,
        'app02': App02Controller,
    }

    def get_controller(self, app):
        if not self.has_controller_for_app(app):
            raise Exception(f'Controller for {app} not found')
        return self.controllers[app]

    def has_controller_for_app(self, app):
        return app in self.controllers