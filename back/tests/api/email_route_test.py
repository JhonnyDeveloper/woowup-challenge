from api.main import app
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch

client = TestClient(app)


def test_send_email_success(email_model):
    with patch("api.routes.email.EmailService.send", return_value=True) as mock_service:

        response = client.post(
            "/email",
            json=email_model.model_dump()
        )

        assert response.status_code == 200
        assert response.json() == {}


# def test_send_email_failure(email_model):
#     with patch("api.routes.email.EmailService.send", return_value=False) as mock_service:
#         response = client.post(
#             "/email",
#             json=email_model.model_dump()
#         )

#         assert response.status_code == 500
