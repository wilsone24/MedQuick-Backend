from sqlalchemy import Column, String
from database import Base

from sqlalchemy import Column, Integer, String

class Doctor(Base):
    __tablename__ = "doctors"

    id_doctor = Column(Integer, primary_key=True, index=True)
    id_specialty = Column(Integer, nullable=False)
    full_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    phone = Column(String(10), nullable=False, unique=True)
    room = Column(String(10), nullable=False)
    skills_description = Column(String(20), nullable=False)

