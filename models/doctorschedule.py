from sqlalchemy import Column, Integer, String,Time, ForeignKey, Enum
from database import Base
from models.enums import DayOfWeekEnum  
class DoctorSchedule(Base):
    __tablename__ = "doctor_schedules"

    id_schedule = Column(Integer, primary_key=True, index=True)
    id_doctor = Column(Integer, ForeignKey("doctors.id_doctor"), nullable=False)
    day_of_week =  Column(Enum(DayOfWeekEnum, name = "day_of_week_enum"), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    status = Column(String(10), nullable=False)