from dataclasses import dataclass
from sparkpost import SparkPost
from api.models.email import Email
from base_email_strategy import BaseEmailStrategy
from core.models.sparkpost_config import SparkPostConfig


@dataclass
class SparkPostStrategy(BaseEmailStrategy):

    _configuration: SparkPostConfig

    def send(self, email: Email):
        sparky = SparkPost(
            api_key=self._configuration._API_KEY
        )

        response = sparky.transmissions.send(
            use_sandbox=self._configuration._IS_SANDBOX,
            from_email=self._configuration._FROM_EMAIL,
            recipients=email.recipients,
            html=email.content,
            subject=email.subject)
