from dataclasses import dataclass
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from api.models.email import Email
from base_email_strategy import BaseEmailStrategy
from core.models.twilio_config import TwilioConfig


@dataclass
class TwilioStrategy(BaseEmailStrategy):

    _configuration: TwilioConfig

    def send(self, email: Email):
        sg = SendGridAPIClient(api_key=self._configuration._API_KEY)

        message = Mail(
            from_email=self._configuration._FROM_EMAIL,
            to_emails=email.recipients,
            subject=email.subject,
            html_content=email.content
        )

        response = sg.send(message)
