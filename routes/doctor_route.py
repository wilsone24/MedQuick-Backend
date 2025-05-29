from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import date
from fastapi import HTTPException
from controllers import doctor_controller
from schemas.doctor_schema import DoctorResponse, DoctorRequest
from database import get_db
from schemas.user_schema import UserInDB
from controllers.auth_controller import get_current_user
from schemas.schedule_schema import ScheduleRequest

router = APIRouter()


@router.get("/doctors", response_model=List[DoctorResponse])
def get_doctors(db: Session = Depends(get_db)):
    return doctor_controller.get_all_doctors(db)


@router.post("/doctors", response_model=DoctorResponse)
def create_doctor(data: DoctorRequest, db: Session = Depends(get_db)):
    return doctor_controller.create_doctor(db, data)


@router.post("/doctors/schedule", response_model=List[str])
def doctor_schedule(
    request: ScheduleRequest,  # ← Aquí recibes el body
    db: Session = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user),
):
    try:
        available_slots = doctor_controller.get_doctor_schedule(
            db, request.id_doctor, request.date
        )
        return available_slots
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/doctors/{id_doctor}")
def delete_doctor(id_doctor: int, db: Session = Depends(get_db)):
    return doctor_controller.delete_doctor(db, id_doctor)
