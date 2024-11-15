from fastapi import FastAPI
from api.routes.email import email_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(email_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*", ""],
)
