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
