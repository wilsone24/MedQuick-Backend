from sqlalchemy.orm import Session
from models.specialty_model import Specialty


def get_all_specialties(db: Session):
    return db.query(Specialty).all()
