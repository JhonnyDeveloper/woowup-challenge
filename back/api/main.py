from fastapi import FastAPI
from api.routes.email import email_router
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(email_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir solo los orígenes en la lista
    allow_credentials=True,
    allow_methods=["*"],  # Métodos permitidos
    allow_headers=["*", ""],  # Encabezados permitidos
)
