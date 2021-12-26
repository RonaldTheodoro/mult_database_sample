from sqlalchemy import text

from controllers.base_controller import BaseController


class App02Controller(BaseController):

    def get_info(self):
        query = self.session.query(text('SELECT 1'))
        return query.all()
