from schemas.patient_schema import PatientBase
from pydantic import BaseModel

from schemas.user_schema import UserBase

class UserPatientBase(BaseModel):
    user: UserBase
    patient: PatientBase

    class Config:
        orm_mode = True