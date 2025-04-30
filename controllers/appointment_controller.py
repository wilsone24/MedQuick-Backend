from sqlalchemy.orm import Session
from uuid import uuid4
from models.appointment_model import Appointment
from schemas.appointment_schema import AppointmentRequest


def get_all_appointments(db: Session):
    return db.query(Appointment).all()


def create_appointment(db: Session, data: AppointmentRequest):
    new_app = Appointment(
        id=str(uuid4()),
        patient_name=data.patient_name,
        doctor_name=data.doctor_name,
        status=data.status,
    )
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app
