from sqlalchemy import Column, Integer, String
from database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id_appointment = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_doctor = Column(Integer, nullable=False)
    id_patient = Column(Integer, nullable=False)
    date = Column(String(10), nullable=False)
    time = Column(String(5), nullable=False)
    description = Column(String(50), nullable=False)
    status = Column(String(10), nullable=False)
