from sqlalchemy import Column, String
from database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(String(36), primary_key=True, index=True)
    patient_name = Column(String(100), nullable=False)
    doctor_name = Column(String(100), nullable=False)
    status = Column(String(50), nullable=False)
