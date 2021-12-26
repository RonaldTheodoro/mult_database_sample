from controllers.app01_controller import App01Controller
from controllers.app02_controller import App02Controller


def test_get_controller_for_app01(controllers):
    controller_cls = controllers.get_controller('app01')
    assert issubclass(controller_cls, App01Controller)


def test_get_controller_for_app02(controllers):
    controller_cls = controllers.get_controller('app02')
    assert issubclass(controller_cls, App02Controller)


def test_get_session_for_app01_dev(controllers):
    database = 'app01_dev'
    session = controllers.get_session(database)
    assert session.bind.url.database == database


def test_get_session_for_app01_homolog(controllers):
    database = 'app01_homolog'
    session = controllers.get_session(database)
    assert session.bind.url.database == database


def test_get_session_for_app01_prod(controllers):
    database = 'app01_prod'
    session = controllers.get_session(database)
    assert session.bind.url.database == database


def test_get_controller_with_session_for_app01_dev(controllers):
    app = 'app01'
    stage = 'dev'
    database = f'{app}_{stage}'
    controller = controllers(app, stage=stage)
    assert isinstance(controller, App01Controller)
    assert controller.session.bind.url.database == database
    assert controller.database == database
    assert controller.stage == stage


def test_get_controller_with_session_for_app01_homolog(controllers):
    app = 'app01'
    stage = 'homolog'
    database = f'{app}_{stage}'
    controller = controllers(app, stage=stage)
    assert isinstance(controller, App01Controller)
    assert controller.session.bind.url.database == database
    assert controller.database == database
    assert controller.stage == stage


def test_get_controller_with_session_for_app01_prod(controllers):
    app = 'app01'
    stage = 'prod'
    database = f'{app}_{stage}'
    controller = controllers(app, stage=stage)
    assert isinstance(controller, App01Controller)
    assert controller.session.bind.url.database == database
    assert controller.database == database
    assert controller.stage == stage


def test_get_controller_with_session_for_app02(controllers):
    app = 'app02'
    controller = controllers(app)
    assert isinstance(controller, App02Controller)
    assert controller.session.bind.url.database == app
    assert controller.database == app
    assert controller.stage is None
