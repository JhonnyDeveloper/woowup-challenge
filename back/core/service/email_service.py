from dataclasses import dataclass
from api.models.email import Email
from core.strategies.base_email_strategy import BaseEmailStrategy


@dataclass
class EmailService():

    _email_strategies: list[BaseEmailStrategy]

    def send(self, email: Email):
        is_sent = False
        for strategy in self._email_strategies:
            is_sent = strategy.send(email)
            if is_sent:
                break

        return is_sent
