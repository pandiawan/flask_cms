import pytest
from app import create_app
from flask_jwt_extended import create_access_token


@pytest.fixture
def app():
    app = create_app('testing')

    context = app.app_context()
    context.push()

    return app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def access_token(client):
    user_data = {"username": "test_user"}
    token = create_access_token(identity=user_data)
    return token


@pytest.fixture
def headers(access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    return headers
