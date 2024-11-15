from api.main import app
from unittest.mock import patch
from fastapi.testclient import TestClient

client = TestClient(app)


def test_send_email_success(mailjet_strategy, gmail_strategy, sparkpost_strategy, email_model):
    gmail_strategy.send.return_value = False
    sparkpost_strategy.send.return_value = False
    mailjet_strategy.send.return_value = True

    with patch("api.routes.email.EmailService", autospec=True) as mock_email_service:
        mock_service_instance = mock_email_service.return_value
        mock_service_instance._email_strategies = [
            mailjet_strategy, gmail_strategy, sparkpost_strategy]

        with patch("api.routes.email.EmailService.send", return_value=False):
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
