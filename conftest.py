import logging
import pytest

from fixtures.app import App
from config import settings

logger = logging.getLogger("api")


def pytest_configure(config):
    config.addinivalue_line("markers", "p0: marks smoke tests")
    config.addinivalue_line("markers", "p1: marks p1 tests")
    config.addinivalue_line("markers", "p2: marks p2 tests")
    config.addinivalue_line("markers", "backend: marks backend tests")
    config.addinivalue_line("markers", "frontend: marks frontend tests")


def pytest_addoption(parser):
    parser.addoption(
        "--frontend",
        action="store",
        help="Enter Frontend url",
        default='https://front.heroku.com',
    ),
    parser.addoption(
        "--backend",
        action="store",
        help="Enter Backend url",
        default="https://public.heroku.com"
    )


@pytest.fixture(scope='session')
def app(request):
    url = request.config.getoption("--frontend")
    url_pub = request.config.getoption("--backend")
    logger.info(f"Start api tests, front url is {url}, public is {url_pub}")
    return App(url, url_pub)


@pytest.fixture(scope='session')
def user(app):
    user = User
    return user


@pytest.fixture(scope='session')
def token(app):
    user = User.get_access_token(settings.user_1)
    return user.token
