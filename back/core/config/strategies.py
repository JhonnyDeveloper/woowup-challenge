from fastapi import Depends
from core.config.clients import dep_sparkpost_client, dep_twilio_client
from core.config.environment import dep_env
from strategies.base_email_strategy import BaseEmailStrategy
from strategies.sparkpost_strategy import SparkPostStrategy
from strategies.twilio_strategy import TwilioStrategy


def dep_sparkpost_strategy(
    configuration: dict = Depends(dep_env),
    sparkpost: dict = Depends(dep_sparkpost_client)
) -> SparkPostStrategy:
    return SparkPostStrategy(
        _configuration=configuration["SPARKPOST"],
        _client=sparkpost
    )


def dep_twilio_strategy(
    configuration: dict = Depends(dep_env),
    twilio: dict = Depends(dep_twilio_client)
) -> TwilioStrategy:
    return TwilioStrategy(
        _configuration=configuration["TWILIO"],
        _client=twilio
    )


def dep_email_strategies(
    sparkpost: SparkPostStrategy = Depends(dep_sparkpost_strategy),
    twilio: TwilioStrategy = Depends(dep_twilio_strategy)
) -> list[BaseEmailStrategy]:
    return [
        sparkpost,
        twilio
    ]
