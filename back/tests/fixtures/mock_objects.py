import pytest

from api.models.email import Email


@pytest.fixture
def email_model():
    return Email(
        content="emailt test",
        recipients=["test@test.com", "test2@test.com"],
        subject="TESTING"
    )


@pytest.fixture
def environment():
    return {
        "SPARKPOST": {
            "API_KEY": "API_KEY_TEST",
            "IS_SANDBOX": True,
            "FROM_EMAIL": "from@from.com",
        },
        "MAILJET": {
            "API_KEY": "API_KEY_TEST",
            "SECRET_KEY": "SECRET_KEY_TEST",
            "FROM_EMAIL": "from@from.com",
            "FROM_NAME": "from_name",
        },
        "GMAIL": {
            "SMTP_SERVER": "SMTP_SERVER_TEST",
            "SMTP_PORT": "SMTP_PORT_TEST",
            "SENDER_EMAIL": "from@from.com",
            "PASSWORD": "PASSWORD_TEST",
        }
    }
