from core.service.email_service import EmailService


def test_send_email_is_true(mailjet_strategy, gmail_strategy, sparkpost_strategy, email_model):
    gmail_strategy.send.return_value = False
    sparkpost_strategy.send.return_value = False
    mailjet_strategy.send.return_value = True
    service = EmailService(
        [
            gmail_strategy,
            sparkpost_strategy,
            mailjet_strategy,
        ]
    )

    assert service.send(email_model) == True
    mailjet_strategy.send.assert_called_once_with(email_model)
    gmail_strategy.send.assert_called_once_with(email_model)
    sparkpost_strategy.send.assert_called_once_with(email_model)


def test_send_email_is_false(mailjet_strategy, gmail_strategy, sparkpost_strategy, email_model):

    gmail_strategy.send.return_value = False
    sparkpost_strategy.send.return_value = False
    mailjet_strategy.send.return_value = False

    service = EmailService(
        [
            gmail_strategy,
            sparkpost_strategy,
            mailjet_strategy,
        ]
    )

    assert service.send(email_model) == False
    mailjet_strategy.send.assert_called_once_with(email_model)
    gmail_strategy.send.assert_called_once_with(email_model)
    sparkpost_strategy.send.assert_called_once_with(email_model)
