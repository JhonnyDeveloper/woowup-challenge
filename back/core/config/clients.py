from fastapi import Depends
from sparkpost import SparkPost
from sendgrid import SendGridAPIClient
from core.config.environment import dep_env


def dep_sparkpost_client(configuration: dict = Depends(dep_env)) -> SparkPost:
    return SparkPost(
        api_key=configuration["SPARKPOST"]["API_KEY"]
    )


def dep_twilio_client(configuration: dict = Depends(dep_env)) -> SparkPost:
    return SendGridAPIClient(
        api_key=configuration["TWILIO"]["API_KEY"]
    )
