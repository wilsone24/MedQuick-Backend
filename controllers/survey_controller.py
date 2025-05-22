from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from models.survey_model import Survey
from schemas.survey_schema import SurveyRequest


def create_survey(db: Session, data: SurveyRequest):
    new_survey = Survey(
        id_patient=data.id_patient,
        date=data.date,
        time=data.time,
        description=data.description,
        sugestions=data.sugestions,
    )
    try:
        db.add(new_survey)
        db.commit()
        db.refresh(new_survey)
        return new_survey
    except SQLAlchemyError as e:
        db.rollback()
        raise e
