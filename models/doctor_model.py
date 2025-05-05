from sqlalchemy import Column, String
from database import Base

class Doctor(Base):
    __tablename__ = "doctors"
    
    id = Column(String(36), primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    specialty = Column(String(100), nullable=False)
    experience = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    