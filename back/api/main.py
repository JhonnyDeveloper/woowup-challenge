from fastapi import FastAPI
from api.routes.email import email_router

app = FastAPI()
app.include_router(email_router)
