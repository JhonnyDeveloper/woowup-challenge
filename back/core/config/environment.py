from os import getenv
from core.models.sparkpost_config import SparkPostConfig
from core.models.twilio_config import TwilioConfig


def dep_sparkpost_env():
    return SparkPostConfig(
        _API_KEY=getenv("SPARKPOST_API_KEY", ""),
        _IS_SANDBOX=getenv("SPARKPOST_IS_SANDBOX", True),
        _FROM_EMAIL=getenv("SPARKPOST_FROM_EMAIL", "")
    )


def dep_twilio_env():
    return TwilioConfig(
        _API_KEY=getenv("TWILIO_API_KEY", ""),
        _FROM_EMAIL=getenv("TWILIO_FROM_EMAIL", "")
    )
