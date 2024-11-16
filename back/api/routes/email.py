from fastapi import Body, HTTPException, Depends
from fastapi.routing import APIRouter
from core.service.email_service import EmailService
from core.config.services import dep_email_service
from api.models.email import Email
from core.config.logger import logger

email_router = APIRouter()

email_docs = {
    "post": {
        "tags": ["Email"],
        "summary": "Enviar correo",
        "description": "Intentar el envio de correo con diferentes proovedores",
        "status_code": 200,
        "responses": {
            "500": {
                "description": "Internal Server Error"
            }
        }
    },
    "examples": Body(
        examples=[
            {
                "recipients": [
                    "test@test.com",
                    "test2@test.com"
                ],
                "subject": "TEST",
                "content": "emailt test"
            }
        ]
    )

}


@email_router.post(path="/email", **email_docs["post"])
def send(
    email_model: Email = email_docs["examples"],
    email_service: EmailService = Depends(dep_email_service)
):
    logger.info(f"Payload: {email_model.model_dump_json()}")
    result = email_service.send(email_model)
    logger.info(f"Email sent: {result}")
    if not result:
        raise HTTPException(status_code=500)
    return {}
