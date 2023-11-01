import pytest

from app import create_app
from app.modules import normalizer

""" References
https://www.patricksoftwareblog.com/testing-a-flask-application-using-pytest/

Collection of pytest fixtured https://github.com/pytest-dev/pytest-flask
"""


@pytest.fixture
def app():
    app = create_app()
    return app
