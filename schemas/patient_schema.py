from pydantic import BaseModel


class PatientBase(BaseModel):
    age: int
    phone: str
    address: str
    blood_type: str
    gender: str


class PatientInDB(PatientBase):
    id_patient: int

    class Config:
        orm_mode = True
