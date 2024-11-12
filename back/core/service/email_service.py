from dataclasses import dataclass
from api.models.email import Email
from core.strategies.base_email_strategy import BaseEmailStrategy


@dataclass
class EmailService():

    _email_strategies: list[BaseEmailStrategy]

    def send(self, email: Email):
        for strategy in self._email_strategies:
            try:
                strategy.send(email)
                break
            except Exception as e:
                print(e)
