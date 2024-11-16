from fastapi import FastAPI
from api.routes.email import email_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Woowup challenge API",
    description="Esta API tiene como objetivo el envio de correos usando diferentes servidores de correo",
    version="1.0.0"
)
app.include_router(email_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*", ""],
)
