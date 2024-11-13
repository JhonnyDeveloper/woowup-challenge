from abc import ABC, abstractmethod
from dataclasses import dataclass
from api.models.email import Email


@dataclass
class BaseEmailStrategy(ABC):

    _configuration: dict

    @abstractmethod
    def send(email: Email):
        raise NotImplementedError()
