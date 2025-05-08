from pydantic import BaseModel


class AppointmentRequest(BaseModel):
    id_doctor: int
    id_patient: int
    date: str
    time: str
    description: str


class AppointmentResponse(BaseModel):
    id_appointment: int
    id_doctor: int
    id_patient: int
    date: str
    time: str
    description: str
    status: str

    class Config:
        orm_mode = True
