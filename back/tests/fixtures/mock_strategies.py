import pytest
from unittest.mock import Mock


@pytest.fixture
def gmail_strategy():
    mock = Mock()
    mock._client = Mock()
    return mock


@pytest.fixture
def mailjet_strategy():
    mock = Mock()
    mock._client = Mock()
    return mock


@pytest.fixture
def sparkpost_strategy():
    mock = Mock()
    mock._client = Mock()
    return mock
