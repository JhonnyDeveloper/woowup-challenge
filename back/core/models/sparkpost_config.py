from dataclasses import dataclass


@dataclass
class SparkPostConfig():
    _API_KEY: str
    _IS_SANDBOX: bool
    _FROM_EMAIL: str
