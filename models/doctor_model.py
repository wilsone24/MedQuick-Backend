from sqlalchemy import Column, String
from database import Base


class Doctor(Base):
    __tablename__ = "doctors"

    id_doctor = Column(int, primary_key=True, index=True)
    id_specialty = Column(int, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(10), nullable=False, unique=True)
    room = Column(String(10), nullable=False)
