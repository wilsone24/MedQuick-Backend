from sqlalchemy import Column, String, Integer
from database import Base


class Survey(Base):
    __tablename__ = "surveys"

    id_survey = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_patient = Column(Integer, nullable=False)
    date = Column(String(10), nullable=False)
    time = Column(String(5), nullable=False)
    description = Column(String(100), nullable=False)
    sugestions = Column(String(50), nullable=False)
