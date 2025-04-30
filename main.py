from fastapi import FastAPI
from routes import appointment_route

app = FastAPI()

app.include_router(appointment_route.router)
