from core.strategies.mailjet_strategy import MailJetStrategy


def test_send_return_true(mailjet_client, environment, email_model):

    mailjet_strategy = MailJetStrategy(
        _client=mailjet_client, _configuration=environment["MAILJET"])

    assert mailjet_strategy.send(email_model) == True


def test_send_return_false(mailjet_client_exception, environment, email_model):
    mailjet_strategy = MailJetStrategy(
        _client=mailjet_client_exception, _configuration=environment["MAILJET"])

    assert mailjet_strategy.send(email_model) == False


def test_get_email_return_dict(gmail_client, environment, email_model):
    gmail_strategy = MailJetStrategy(
        _client=gmail_client, _configuration=environment["MAILJET"])

    result = gmail_strategy.get_email(email_model)

    assert "FromEmail" in result
    assert "FromName" in result
    assert "Subject" in result
    assert "Html-part" in result
    assert "Recipients" in result
    assert isinstance(result["FromEmail"], str)
    assert isinstance(result["FromName"], str)
    assert isinstance(result["Subject"], str)
    assert isinstance(result["Html-part"], str)
    assert isinstance(result["Recipients"], list)
