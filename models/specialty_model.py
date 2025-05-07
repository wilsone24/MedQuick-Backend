from sqlalchemy import Column, String
from database import Base


class Specialty(Base):
    __tablename__ = "specialties"

    id_specialty = Column(int, primary_key=True, index=True)
    name = Column(String(50), nullable=False, unique=True)
    description = Column(String(100), nullable=False)