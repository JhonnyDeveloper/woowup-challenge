from fastapi import Depends
from core.config.environment import dep_sparkpost_env, dep_twilio_env
from core.models.sparkpost_config import SparkPostConfig
from core.models.twilio_config import TwilioConfig
from strategies.base_email_strategy import BaseEmailStrategy
from strategies.sparkpost_strategy import SparkPostStrategy
from strategies.twilio_strategy import TwilioStrategy


def dep_sparkpost_strategy(config: SparkPostConfig = Depends(dep_sparkpost_env)) -> SparkPostStrategy:
    return SparkPostStrategy(configuration=config)


def dep_twilio_strategy(config: TwilioConfig = Depends(dep_twilio_env)) -> TwilioStrategy:
    return TwilioStrategy(configuration=config)


def dep_email_strategies(
    sparkpost: SparkPostStrategy = Depends(dep_sparkpost_strategy),
    twilio: TwilioStrategy = Depends(dep_twilio_strategy)
) -> list[BaseEmailStrategy]:
    return [
        sparkpost,
        twilio
    ]
