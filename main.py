from fastapi import FastAPI
from routes import appointment_route
from routes import doctor_route

app = FastAPI()

app.include_router(appointment_route.router)
app.include_router(doctor_route.router)
