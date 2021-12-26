from sqlalchemy import text

from controllers.base_controller import BaseController


class App01Controller(BaseController):

    def get_data(self):
        query = self.session.query(text('SELECT 1'))
        return query.all()
