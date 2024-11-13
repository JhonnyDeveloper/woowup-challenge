from fastapi import HTTPException, Depends
from fastapi.routing import APIRouter
from core.service.email_service import EmailService
from core.config.services import dep_email_service
from api.models.email import Email

email_router = APIRouter()


@email_router.post("/email")
def send(
    email_model: Email,
    email_service: EmailService = Depends(dep_email_service)
):
    if not email_service.send(email_model):
        raise HTTPException(status_code=500)
    return {}
