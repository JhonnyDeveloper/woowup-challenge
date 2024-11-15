from core.strategies.sparkpost_strategy import SparkPostStrategy


def test_send_return_true(sparkpost_client, environment, email_model):

    sparkpost_strategy = SparkPostStrategy(
        _client=sparkpost_client, _configuration=environment["SPARKPOST"])

    assert sparkpost_strategy.send(email_model) == True


def test_send_return_false(sparkpost_client_exception, environment, email_model):

    sparkpost_strategy = SparkPostStrategy(
        _client=sparkpost_client_exception, _configuration=environment["SPARKPOST"])

    assert sparkpost_strategy.send(email_model) == False


def test_get_email_return_dict(sparkpost_client, environment, email_model):
    sparkpost_strategy = SparkPostStrategy(
        _client=sparkpost_client, _configuration=environment["SPARKPOST"])

    result = sparkpost_strategy.get_email(email_model)

    assert "use_sandbox" in result
    assert "from_email" in result
    assert "recipients" in result
    assert "html" in result
    assert "subject" in result
    assert isinstance(result["use_sandbox"], bool)
    assert isinstance(result["from_email"], str)
    assert isinstance(result["recipients"], list)
    assert isinstance(result["html"], str)
    assert isinstance(result["subject"], str)
