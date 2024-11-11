from fastapi import FastAPI
from routes.email import email_router

app = FastAPI()
app.include_router(email_router)
