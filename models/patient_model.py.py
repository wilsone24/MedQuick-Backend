from sqlalchemy import Column, String, Integer, Enum
from database import Base
from models.enums import BloodTypeEnum

class Patient(Base):
    __tablename__ = "patients"

    id_patient = Column(Integer, primary_key=True, index=True)
    age = Column(Integer, nullable=False)
    phone = Column(String(15), nullable=False, unique=True)
    address = Column(String(50), nullable=False)
    blood_type = Column(Enum(BloodTypeEnum, name="blood_type_enum"), nullable=False)


