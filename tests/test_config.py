import pytest


class NotInRAnge(Exception):
    def __init__(self, message='Value not in range'):
        self.message = message
        super().__init__(self.message)


def test_generic():
    a = 5

    with pytest.raises(NotInRAnge):
        if a not in range(10, 20):
            raise NotInRAnge


def test_something():
    a = 2
    b = 2
    assert True
