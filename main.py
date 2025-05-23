from fastapi import FastAPI
from routes import appointment_route, doctor_route, survey_route, auth_route


app = FastAPI()

app.include_router(appointment_route.router)
app.include_router(doctor_route.router)
app.include_router(survey_route.router)
app.include_router(auth_route.router)
