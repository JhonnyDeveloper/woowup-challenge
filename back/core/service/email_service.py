from dataclasses import dataclass
from api.models.email import Email
from core.strategies.base_email_strategy import BaseEmailStrategy
from core.config.logger import logger


@dataclass
class EmailService():

    _email_strategies: list[BaseEmailStrategy]

    def send(self, email: Email):
        is_sent = False
        for strategy in self._email_strategies:
            logger.info(f"Strategy: {strategy.__class__.__name__}")
            is_sent = strategy.send(email)
            logger.info(f"Is sent: {is_sent}")
            if is_sent:
                break

        return is_sent
