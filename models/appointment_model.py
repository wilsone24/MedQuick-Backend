from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from database import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id_appointment = Column(Integer, primary_key=True, index=True)
    id_doctor = Column(Integer, ForeignKey("doctors.id_doctor"), nullable=False)
    id_patient = Column(Integer, ForeignKey("patients.id_patient"), nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    description = Column(String(100), nullable=False)
    status = Column(String(10), nullable=False)
