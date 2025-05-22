from sqlalchemy import Column, String, Integer, Date, Time
from database import Base


class Survey(Base):
    __tablename__ = "surveys"

    id_survey = Column(Integer, primary_key=True, index=True, autoincrement=True)
    id_patient = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    description = Column(String(100), nullable=False)
    sugestions = Column(String(50), nullable=False)
