import pytest
from api import create_app


@pytest.fixture(scope="session")
def app():
    return create_app(True)
