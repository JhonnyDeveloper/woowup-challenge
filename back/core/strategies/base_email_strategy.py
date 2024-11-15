from abc import ABC, abstractmethod
from dataclasses import dataclass
from api.models.email import Email


@dataclass
class BaseEmailStrategy(ABC):

    _configuration: dict

    @abstractmethod
    def send(self, email: Email) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def get_email(self, email: Email):
        raise NotImplementedError()
