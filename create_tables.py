from database import Base, engine
from models.appointment_model import Appointment

Base.metadata.create_all(bind=engine)
