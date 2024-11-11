from fastapi import Depends
from fastapi.routing import APIRouter
from core.service.email_service import EmailService
from core.config.strategies import dep_email_service
from models.email import Email

email_router = APIRouter()


@email_router.post("/")
def send(
    email_model: Email,
    email_service: EmailService = Depends(dep_email_service)
):
    return email_service.send(email_model)
