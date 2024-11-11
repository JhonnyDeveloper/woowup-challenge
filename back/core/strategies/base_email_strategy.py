from abc import ABC, abstractmethod
from api.models.email import Email


class BaseEmailStrategy(ABC):

    @abstractmethod
    def send(email: Email):
        raise NotImplementedError()
