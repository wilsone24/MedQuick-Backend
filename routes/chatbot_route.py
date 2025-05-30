from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers import chatbot_controller
from schemas.chatbot_schema import Consulta, Pregunta
from models.historial_model import Historial

router = APIRouter()


@router.post("/chatbot/guardar-y-recomendar")
def guardar_y_recomendar(consulta: Consulta, db: Session = Depends(get_db)):
    try:
        recomendacion = chatbot_controller.obtener_recomendacion(
            consulta.usuario, consulta.sintomas, db
        )

        nuevo = Historial(
            usuario=consulta.usuario,
            sintomas=consulta.sintomas,
            recomendacion=recomendacion,
            fecha=consulta.fecha,
        )
        db.add(nuevo)
        db.commit()

        return {
            "usuario": consulta.usuario,
            "sintomas": consulta.sintomas,
            "fecha": consulta.fecha,
            "recomendacion": recomendacion,
        }
    except Exception as e:
        return {"error": str(e)}


@router.post("/chatbot/preguntar")
def preguntar(pregunta: Pregunta, db: Session = Depends(get_db)):
    try:
        respuesta = chatbot_controller.obtener_consulta(
            pregunta.usuario, pregunta.pregunta, db
        )
        return {
            "usuario": pregunta.usuario,
            "respuesta": respuesta,
        }
    except Exception as e:
        return {"error": str(e)}
