from dataclasses import dataclass
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from api.models.email import Email
from base_email_strategy import BaseEmailStrategy


@dataclass
class TwilioStrategy(BaseEmailStrategy):

    _client: SendGridAPIClient

    def send(self, email: Email):
        message = Mail(
            from_email=self._configuration["FROM_EMAIL"],
            to_emails=email.recipients,
            subject=email.subject,
            html_content=email.content
        )

        response = self._client.send(message)
