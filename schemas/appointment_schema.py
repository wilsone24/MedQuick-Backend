from pydantic import BaseModel


class AppointmentRequest(BaseModel):
    patient_name: str
    doctor_name: str
    status: str


class AppointmentResponse(AppointmentRequest):
    id: str

    class Config:
        orm_mode = True
