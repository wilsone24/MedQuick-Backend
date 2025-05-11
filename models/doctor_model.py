from sqlalchemy import Column, String, Integer
from database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id_doctor = Column(Integer, primary_key=True, index=True)
    id_specialty = Column(Integer, nullable=False)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(15), nullable=False, unique=True)
    room = Column(String(10), nullable=False)
