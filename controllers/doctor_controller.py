from sqlalchemy.orm import Session
from models.doctor_model import Doctor
from datetime import date
from models.appointment_model import Appointment
from schemas.doctor_schema import DoctorRequest
from sqlalchemy.exc import SQLAlchemyError


def get_all_doctors(db: Session):
    return db.query(Doctor).all()


def get_doctor_schedule(
    db: Session,
    doctor_id: int,
    date: date,
):
    appoinments = (
        db.query(Appointment)
        .filter(
            Appointment.id_doctor == doctor_id,
            Appointment.date == date,
        )
        .all()
    )
    schedule = [
        "08:00:00",
        "09:00:00",
        "10:00:00",
        "11:00:00",
        "14:00:00",
        "15:00:00",
        "16:00:00",
        "17:00:00",
    ]
    for appointment in appoinments:
        schedule.remove(appointment.time.strftime("%H:%M:%S"))
    print(schedule)
    return schedule


def create_doctor(db: Session, data: DoctorRequest):
    new_doctor = Doctor(
        id_specialty=data.id_specialty,
        full_name=data.full_name,
        email=data.email,
        phone=data.phone,
        room=data.room,
        skills_description=data.skills_description,
    )
    try:
        db.add(new_doctor)
        db.commit()
        db.refresh(new_doctor)
        return new_doctor
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def delete_doctor(db: Session, id_doctor: int):
    doctor = db.query(Doctor).filter(Doctor.id_doctor == id_doctor).first()
    if not doctor:
        return {"error": "Doctor not found"}
    db.delete(doctor)
    db.commit()
    return {"message": "Doctor deleted successfully"}
