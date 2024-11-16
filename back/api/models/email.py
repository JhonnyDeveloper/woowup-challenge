from typing import List
from pydantic import BaseModel, EmailStr, Field


class Email(BaseModel):
    recipients: List[EmailStr] = Field(min_length=1)
    subject: str = Field(min_length=5)
    content: str = Field(min_length=1)
