class BaseController:

    def __init__(self, session, database, stage=None):
        self.session = session
        self.database = database
        self.stage = stage

