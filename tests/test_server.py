# External Libraries
import pytest

# Internal Libraries
from rab.server import app
from rab.server import handlers


@pytest.fixture
def client():
    """Test code that makes a request to the application"""
    with app.app.test_client() as client:
        yield client


@pytest.fixture
def app_context():
    """Test code that uses an application context: current_app, g, url_for"""
    with app.app.test_request_context() as context:
        yield context


def test_get_request_json(app_context):
    assert handlers._get_request_json() is None
