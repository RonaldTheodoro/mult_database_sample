import inspect

from controllers.app01_controller import App01Controller
from controllers.app02_controller import App02Controller


def test_get_controller_for_app01(controllers):
    controller_cls = controllers.get_controller('app01')
    assert issubclass(controller_cls, App01Controller)


def test_get_controller_for_app02(controllers):
    controller_cls = controllers.get_controller('app02')
    assert issubclass(controller_cls, App02Controller)
