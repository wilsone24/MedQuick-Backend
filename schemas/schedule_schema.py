from pydantic import BaseModel
from datetime import date


class ScheduleRequest(BaseModel):
    id_doctor: int
    date: date
