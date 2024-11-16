from json import loads
from api.main import app
from unittest.mock import Mock
from fastapi.testclient import TestClient

from core.config.services import dep_email_service

client = TestClient(app)


def test_send_email_success(email_model):

    mock = Mock()
    mock.send.return_value = True
    app.dependency_overrides[dep_email_service] = lambda: mock

    response = client.post(
        "/email",
        json=email_model.model_dump()
    )

    app.dependency_overrides.clear()

    assert response.status_code == 200


def test_send_email_failure(email_model):
    mock = Mock()
    mock.send.return_value = False
    app.dependency_overrides[dep_email_service] = lambda: mock

    response = client.post(
        "/email",
        json=email_model.model_dump()
    )

    app.dependency_overrides.clear()

    assert response.status_code == 500


def test_send_email_validations(email_model):
    mock = Mock()
    mock.send.return_value = False
    app.dependency_overrides[dep_email_service] = lambda: mock

    email_model.recipients = []
    email_model.subject = "1"
    email_model.content = ""

    response = client.post(
        "/email",
        json=email_model.model_dump()
    )

    app.dependency_overrides.clear()
    detail = loads(response.text)["detail"]
    assert response.status_code == 422
    assert len(detail) == 3
