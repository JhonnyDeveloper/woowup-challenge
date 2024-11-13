from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP
from dataclasses import dataclass
from api.models.email import Email
from core.strategies.base_email_strategy import BaseEmailStrategy


@dataclass
class GmailStrategy(BaseEmailStrategy):

    _client: SMTP

    def get_message(self, content):
        return MIMEText(f"""
            <!DOCTYPE html>
                <body>
                    {content}
                </body>
            </html>
            """, "html")

    def send(self, email: Email):
        message = MIMEMultipart()
        message["From"] = self._configuration["SENDER_EMAIL"]
        message["To"] = ", ".join(email.recipients)
        message["Subject"] = email.subject
        message.attach(self.get_message(email.content))

        self._client.starttls()
        self._client.login(
            user=self._configuration["SENDER_EMAIL"], password=self._configuration["PASSWORD"])
        return self._client.sendmail(
            self._configuration["SENDER_EMAIL"], email.recipients, message.as_string())
