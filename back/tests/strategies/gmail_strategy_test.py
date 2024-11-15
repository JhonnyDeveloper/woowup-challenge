from email.mime.text import MIMEText
from core.strategies.gmail_strategy import GmailStrategy


def test_send_return_true(gmail_client, environment, email_model):

    gmail_strategy = GmailStrategy(
        _client=gmail_client, _configuration=environment["GMAIL"])

    assert gmail_strategy.send(email_model) == True
    gmail_client.starttls.assert_called_once()
    gmail_client.login.assert_called_once()
    gmail_client.sendmail.assert_called_once()


def test_send_return_false(gmail_client_exception, environment, email_model):
    gmail_strategy = GmailStrategy(
        _client=gmail_client_exception, _configuration=environment["GMAIL"])

    assert gmail_strategy.send(email_model) == False
    gmail_client_exception.starttls.assert_called_once()


def test_get_email_return_dict(gmail_client, environment, email_model):
    gmail_strategy = GmailStrategy(
        _client=gmail_client, _configuration=environment["GMAIL"])

    result = gmail_strategy.get_email(email_model)

    assert "from_addr" in result
    assert "to_addrs" in result
    assert "msg" in result
    assert isinstance(result["from_addr"], str)
    assert isinstance(result["to_addrs"], list)
    assert isinstance(result["msg"], str)


def test_get_message_return_dict(gmail_client, environment, email_model):
    gmail_strategy = GmailStrategy(
        _client=gmail_client, _configuration=environment["GMAIL"])

    result = gmail_strategy.get_message("content")

    assert isinstance(result, MIMEText)
