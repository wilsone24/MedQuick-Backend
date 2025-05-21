from pydantic import BaseModel, EmailStr, constr


class DoctorRequest(BaseModel):
    id_specialty: int
    full_name: str
    email: str
    phone: str
    room: str
    skills_description: str


class DoctorResponse(DoctorRequest):
    id_doctor: int
    class Config:
        orm_mode = True
        

