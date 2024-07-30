import pytest


@pytest.fixture()
def set_up():
    print('Test started')
    yield
    print('Test finished')


@pytest.fixture(scope='module')
def set_group():
    print('Enter system')
    yield
    print('Exit system')