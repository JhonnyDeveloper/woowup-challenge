from dataclasses import dataclass
from sparkpost import SparkPost
from api.models.email import Email
from core.strategies.base_email_strategy import BaseEmailStrategy


@dataclass
class SparkPostStrategy(BaseEmailStrategy):

    _client: SparkPost

    def send(self, email: Email):
        return self._client.transmissions.send(**self.get_email(email))

    def get_email(self, email: Email):
        return {
            "use_sandbox": self._configuration["IS_SANDBOX"],
            "from_email": self._configuration["FROM_EMAIL"],
            "recipients": email.recipients,
            "html": email.content,
            "subject": email.subject
        }
