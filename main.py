from fastapi import FastAPI
from routes import (
    appointment_route,
    doctor_route,
    auth_route,
    specialty_route,
    chatbot_route,
)
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(appointment_route.router)
app.include_router(doctor_route.router)
app.include_router(auth_route.router)
app.include_router(specialty_route.router)
app.include_router(chatbot_route.router)
