from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers import survey_controller
from schemas.survey_schema import SurveyRequest, SurveyResponse
from database import get_db
from schemas.user_schema import UserInDB
from controllers.auth_controller import get_current_user

router = APIRouter()


@router.post("/surveys", response_model=SurveyResponse)
def create_survey(
    data: SurveyRequest,
    db: Session = Depends(get_db),
    current_user: UserInDB = Depends(get_current_user),
):
    return survey_controller.create_survey(db, data)
