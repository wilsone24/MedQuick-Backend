from fastapi import FastAPI
from routes import appointment_route
from database import Base, engine

app = FastAPI()

app.include_router(appointment_route.router)
