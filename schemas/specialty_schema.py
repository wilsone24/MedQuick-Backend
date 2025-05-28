from pydantic import BaseModel
from datetime import time
from datetime import date


class SpecialtyResponse(BaseModel):
    id_specialty: int
    name: str
    description: str

    class Config:
        orm_mode = True
