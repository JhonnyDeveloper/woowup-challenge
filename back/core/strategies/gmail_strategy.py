from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from dataclasses import dataclass
from api.models.email import Email
from core.strategies.base_email_strategy import BaseEmailStrategy
from core.config.logger import logger


@dataclass
class GmailStrategy(BaseEmailStrategy):

    _client: SMTP

    def send(self, email: Email):
        try:
            self._client.starttls()
            self._client.login(
                user=self._configuration["SENDER_EMAIL"], password=self._configuration["PASSWORD"])
            self._client.sendmail(**self.get_email(email))
            return True
        except Exception as e:
            logger.error(e)
            return False

    def get_email(self, email: Email):
        message = MIMEMultipart()
        message["From"] = self._configuration["SENDER_EMAIL"]
        message["To"] = ", ".join(email.recipients)
        message["Subject"] = email.subject
        message.attach(self.get_message(email.content))

        result = {
            "from_addr": self._configuration["SENDER_EMAIL"],
            "to_addrs": email.recipients,
            "msg": message.as_string()
        }
        logger.info(f"{self.__class__.__name__} Email Message: {result}")

        return result

    def get_message(self, content):
        return MIMEText(f"""
            <!DOCTYPE html>
                <body>
                    {content}
                </body>
            </html>
            """, "html")
