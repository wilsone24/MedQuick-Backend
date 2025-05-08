from sqlalchemy import Column, String
from database import Base


class Patient(Base):
    __tablename__ = "patients"

    id_patient = Column(int, primary_key=True, index=True)
    age = Column(int, nullable=False)
    phone = Column(String(10), nullable=False, unique=True)
    addres = Column(String(30), nullable=False)
    blood_type = Column(String(3), nullable=False)
    gender = Column(String(1), nullable=False)
    identification = Column(String(20), nullable=False, unique=True)
