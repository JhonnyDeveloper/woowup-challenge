import pytest
from types import SimpleNamespace
from unittest.mock import Mock


@pytest.fixture
def sparkpost_client():
    mock = Mock()
    mock.transmissions.send.return_value = True
    return mock


@pytest.fixture
def sparkpost_client_exception():
    mock = Mock()
    mock.transmissions.send.side_effect = Exception("Error")
    return mock


@pytest.fixture
def mailjet_client():
    mock = Mock()
    mock.send.create.return_value.ok = True
    return mock


@pytest.fixture
def mailjet_client_exception():
    mock = Mock()
    mock.send.create.side_effect = Exception("Error")
    return mock


@pytest.fixture
def gmail_client():
    mock = Mock()
    mock.starttls.return_value = True
    mock.login.return_value = True
    mock.sendmail.return_value = True
    return mock


@pytest.fixture
def gmail_client_exception():
    mock = Mock()
    mock.starttls.side_effect = Exception("Error")
    return mock
