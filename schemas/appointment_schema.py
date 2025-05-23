from pydantic import BaseModel
from datetime import time
from datetime import date


class AppointmentRequest(BaseModel):
    id_doctor: int
    id_patient: int
    date: date
    time: time
    description: str


class AppointmentResponse(BaseModel):
    id_appointment: int
    id_doctor: int
    id_patient: int
    date: date
    time: time
    description: str
    status: str

    class Config:
        orm_mode = True
