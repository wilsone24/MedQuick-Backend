from sqlalchemy import Column, String
from database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id_appoinment = Column(int, primary_key=True, index=True)
    id_doctor = Column(int, nullable=False)
    id_patient = Column(int, nullable=False)
    date = Column(String(10), nullable=False)
    time = Column(String(5), nullable=False)
    description = Column(String(100), nullable=False)
    status = Column(String(10), nullable=False)
