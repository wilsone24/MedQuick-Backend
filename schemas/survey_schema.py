from pydantic import BaseModel
from datetime import date
from datetime import time


class SurveyRequest(BaseModel):
    id_patient: int
    date: date
    time: time
    description: str
    sugestions: str


class SurveyResponse(SurveyRequest):
    id_survey: int

    class Config:
        orm_mode = True
