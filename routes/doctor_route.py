from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from controllers import doctor_controller
from schemas.appointment_schema import DoctorRequest, DoctorResponse
from database import get_db

router = APIRouter()

@router.get("/doctors", response_model=List[DoctorResponse])
def get_doctors(db: Session = Depends(get_db)):
    return doctor_controller.get_all_doctors(db)

@router.post("/doctors", response_model=DoctorResponse)
def create_doctor(data: DoctorRequest, db: Session = Depends(get_db)):
    return doctor_controller.create_doctor(db, data)