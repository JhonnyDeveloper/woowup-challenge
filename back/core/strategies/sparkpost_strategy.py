from dataclasses import dataclass
from sparkpost import SparkPost
from api.models.email import Email
from core.strategies.base_email_strategy import BaseEmailStrategy
from core.config.logger import logger


@dataclass
class SparkPostStrategy(BaseEmailStrategy):

    _client: SparkPost

    def send(self, email: Email):
        try:
            self._client.transmissions.send(**self.get_email(email))
            return True
        except Exception as e:
            logger.error(e)
            return False

    def get_email(self, email: Email):
        result = {
            "use_sandbox": self._configuration["IS_SANDBOX"],
            "from_email": self._configuration["FROM_EMAIL"],
            "recipients": email.recipients,
            "html": email.content,
            "subject": email.subject
        }
        logger.info(f"{self.__class__.__name__} Email Message: {result}")
        return result
