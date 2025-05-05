from pydantic import BaseModel

class DoctorRequest(BaseModel):
    name: str
    specialty: str
    status: str
    email: str
    
    
class DoctorResponse(DoctorRequest):
    id: str

    class Config:
        orm_mode = True
        