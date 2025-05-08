from sqlalchemy import Column, String
from database import Base


class Surveys(Base):
    __tablename__ = "surveys"

    id_survey = Column(int, primary_key=True, index=True)
    id_patient = Column(int, nullable=False)
    date = Column(String(10), nullable=False)
    time = Column(String(5), nullable=False)
    description = Column(String(100), nullable=False)
    sugestions = Column(String(50), nullable=False)
