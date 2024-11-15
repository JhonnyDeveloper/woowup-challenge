import pytest
from unittest.mock import Mock


@pytest.fixture
def gmail_strategy():
    return Mock()


@pytest.fixture
def mailjet_strategy():
    return Mock()


@pytest.fixture
def sparkpost_strategy():
    return Mock()
