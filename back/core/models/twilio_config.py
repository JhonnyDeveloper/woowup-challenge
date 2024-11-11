from dataclasses import dataclass


@dataclass
class TwilioConfig():
    _API_KEY: str
    _FROM_EMAIL: str
