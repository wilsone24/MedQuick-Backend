from sqlalchemy import Column, String, Integer
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    id_patient = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    phone = Column(String(10), nullable=False, unique=True)
    address = Column(String(100), nullable=False)
    blood_type = Column(String(3), nullable=False)
    gender = Column(String(1), nullable=False)

