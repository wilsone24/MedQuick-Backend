from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from controllers import specialty_controller
from schemas.specialty_schema import SpecialtyResponse
from database import get_db

router = APIRouter()


@router.get("/specialties", response_model=List[SpecialtyResponse])
def get_specialties(db: Session = Depends(get_db)):
    return specialty_controller.get_all_specialties(db)
