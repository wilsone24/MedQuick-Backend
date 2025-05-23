from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from controllers import auth_controller
from schemas.token_schema import Token
from controllers import auth_controller
from schemas.user_schema import UserInDB, UserBase
from sqlalchemy.orm import Session
from database import get_db
from schemas.user_patient_schema import UserPatientBase

router = APIRouter()


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = auth_controller.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Credenciales inv")

    token_data = {
        "sub": user.email,
        "id_user": user.id_user,
        "full_name": user.full_name,
        "email": user.email,
        "role": user.role,
    }

    token = auth_controller.create_access_token(data=token_data)
    return {"access_token": token, "token_type": "bearer"}


@router.post("/register", response_model=UserInDB)
def create_user(payload: UserPatientBase, db: Session = Depends(get_db)):
    user_data = payload.user
    patient_data = payload.patient
    user = auth_controller.register_user(db, user_data)
    patient_data_dict = patient_data.dict()
    patient_data_dict["id_patient"] = user.id_user
    auth_controller.register_patient(db, patient_data_dict)
    return user
