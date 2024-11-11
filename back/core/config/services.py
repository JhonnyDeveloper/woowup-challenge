from fastapi import Depends
from core.config.strategies import dep_email_strategies
from core.strategies.base_email_strategy import BaseEmailStrategy
from service.email_service import EmailService


def dep_email_service(
    email_strategies: list[BaseEmailStrategy] = Depends(dep_email_strategies),
) -> EmailService:
    return EmailService(_email_strategies=email_strategies)
