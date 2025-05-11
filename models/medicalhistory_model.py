from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from database import Base


class MedicalHistory(Base):
    __tablename__ = "medical_histories"

    id_medical_history = Column(Integer, primary_key=True, index=True)
    id_patient = Column(Integer, ForeignKey("patients.id_patient"), nullable=False)
    id_doctor = Column(Integer, ForeignKey("doctors.id_doctor"), nullable=False)
    date = Column(Date, nullable=False)
    prescription = Column(String(100), nullable=False)
    diagnosis = Column(String(200), nullable=False)
    treatment = Column(String(200), nullable=False)