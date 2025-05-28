from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from controllers import appointment_controller
from schemas.appointment_schema import AppointmentRequest, AppointmentResponse
from database import get_db
from schemas.user_schema import UserInDB
from controllers.auth_controller import get_current_user

router = APIRouter()


@router.get("/appointments", response_model=List[AppointmentResponse])
def get_appointments(
    db: Session = Depends(get_db)
):
    return appointment_controller.get_all_appointments(db)


@router.post("/appointments", response_model=AppointmentResponse)
def create_appointment(
    data: AppointmentRequest,
    db: Session = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user),
):
    return appointment_controller.create_appointment(db, data)


@router.get("/appointments/{user_id}", response_model=List[AppointmentResponse])
def get_appointments_by_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user),
):
    return appointment_controller.get_appointments_by_user(db, user_id)


@router.delete("/appointments/{appointment_id}")
def delete_appointment(
    appointment_id: int,
    db: Session = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user),
):
    return appointment_controller.delete_appointment(db, appointment_id)
