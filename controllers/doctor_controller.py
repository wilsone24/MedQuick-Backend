from sqlalchemy.orm import Session
from uuid import uuid4
from models.doctor_model import Doctor
from schemas.appointment_schema import DoctorRequest


def get_all_doctors(db: Session):
    return db.query(Doctor).all()


def create_appointment(db: Session, data: DoctorRequest):
    new_app = Doctor(
        id=str(uuid4()),
        name=data.name,
        specialty=data.specialty,
        status=data.status,
        email=data.email,
        
    )
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app