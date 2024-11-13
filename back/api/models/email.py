from pydantic import BaseModel


class Email(BaseModel):
    recipients: list
    subject: str
    content: str
