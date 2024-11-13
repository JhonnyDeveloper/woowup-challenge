from fastapi import Depends
from core.config.clients import dep_sparkpost_client, dep_mailjet_client
from core.config.environment import dep_env
from core.strategies.base_email_strategy import BaseEmailStrategy
from core.strategies.sparkpost_strategy import SparkPostStrategy
from core.strategies.mailjet_strategy import MailJetStrategy


def dep_sparkpost_strategy(
    configuration: dict = Depends(dep_env),
    sparkpost: dict = Depends(dep_sparkpost_client)
) -> SparkPostStrategy:
    return SparkPostStrategy(
        _configuration=configuration["SPARKPOST"],
        _client=sparkpost
    )


def dep_mailjet_strategy(
    configuration: dict = Depends(dep_env),
    mailjet: dict = Depends(dep_mailjet_client)
) -> MailJetStrategy:
    return MailJetStrategy(
        _configuration=configuration["MAILJET"],
        _client=mailjet
    )


def dep_email_strategies(
    sparkpost: SparkPostStrategy = Depends(dep_sparkpost_strategy),
    mailjet: MailJetStrategy = Depends(dep_mailjet_strategy)
) -> list[BaseEmailStrategy]:
    return [
        sparkpost,
        mailjet
    ]
