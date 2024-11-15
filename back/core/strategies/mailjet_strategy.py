from dataclasses import dataclass
from mailjet_rest import Client
from api.models.email import Email
from core.strategies.base_email_strategy import BaseEmailStrategy


@dataclass
class MailJetStrategy(BaseEmailStrategy):

    _client: Client

    def send(self, email: Email):
        try:
            result = self._client.send.create(data=self.get_email(email))

            return result.ok

        except Exception as e:
            print(e)
            return False

    def get_email(self, email: Email):
        return {
            'FromEmail': self._configuration["FROM_EMAIL"],
            'FromName': self._configuration["FROM_NAME"],
            'Subject': email.subject,
            'Html-part': email.content,
            'Recipients': [{"Email": recipient} for recipient in email.recipients]
        }
