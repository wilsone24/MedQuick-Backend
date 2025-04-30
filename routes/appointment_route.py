from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from controllers import appointment_controller
from schemas.appointment_schema import AppointmentRequest, AppointmentResponse
from database import get_db

router = APIRouter()


@router.get("/appointments", response_model=List[AppointmentResponse])
def get_appointments(db: Session = Depends(get_db)):
    return appointment_controller.get_all_appointments(db)


@router.post("/appointments", response_model=AppointmentResponse)
def create_appointment(data: AppointmentRequest, db: Session = Depends(get_db)):
    return appointment_controller.create_appointment(db, data)
