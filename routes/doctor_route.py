from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from controllers import doctor_controller
from schemas.doctor_schema import DoctorResponse
from database import get_db

router = APIRouter()


@router.get("/doctors", response_model=List[DoctorResponse])
def get_doctors(db: Session = Depends(get_db)):
    return doctor_controller.get_all_doctors(db)
