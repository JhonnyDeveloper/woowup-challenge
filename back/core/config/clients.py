from smtplib import SMTP
from fastapi import Depends
from sparkpost import SparkPost
from mailjet_rest import Client
from core.config.environment import dep_env


def dep_sparkpost_client(configuration: dict = Depends(dep_env)) -> SparkPost:
    return SparkPost(
        api_key=configuration["SPARKPOST"]["API_KEY"]
    )


def dep_mailjet_client(configuration: dict = Depends(dep_env)) -> Client:
    return Client(
        auth=(
            configuration["MAILJET"]["API_KEY"],
            configuration["MAILJET"]["SECRET_KEY"]
        )
    )


def dep_gmail_client(configuration: dict = Depends(dep_env)) -> SMTP:
    return SMTP(configuration["GMAIL"]["SMTP_SERVER"], configuration["GMAIL"]["SMTP_PORT"])
