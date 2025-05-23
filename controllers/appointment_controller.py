from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.appointment_model import Appointment
from schemas.appointment_schema import AppointmentRequest


def get_all_appointments(db: Session):
    return db.query(Appointment).all()


def create_appointment(db: Session, data: AppointmentRequest):
    new_appointment = Appointment(
        id_doctor=data.id_doctor,
        id_patient=data.id_patient,
        date=data.date,
        time=data.time,
        description=data.description,
        status="In process",
    )
    try:
        db.add(new_appointment)
        db.commit()
        db.refresh(new_appointment)
        return new_appointment
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def get_appointments_by_user(db: Session, user_id: int):
    return db.query(Appointment).filter(Appointment.id_patient == user_id).all()


def delete_appointment(db: Session, appointment_id: int):
    appointment = db.query(Appointment).filter(Appointment.id_appointment == appointment_id).first()
    if not appointment:
        return {"error": "Appointment not found"}
    db.delete(appointment)
    db.commit()
    return {"message": "Appointment deleted successfully"}
