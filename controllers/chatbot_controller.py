import httpx
from sqlalchemy.orm import Session
from models.historial_model import Historial
from dotenv import load_dotenv
import os
from models.doctor_model import Doctor
from models.specialty_model import Specialty
from models.appointment_model import Appointment

load_dotenv()


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def obtener_recomendacion(usuario: str, sintomas: str, db: Session):
    try:
        historico = db.query(Historial).filter(Historial.usuario == usuario).all()
        medicos_disponibles = db.query(Doctor).all()
        especialidades_disponibles = db.query(Specialty).all()
        contexto = "\n".join(
            [
                f"Fecha: {h.fecha} | Síntomas: {h.sintomas}\nRecomendación: {h.recomendacion}"
                for h in historico
            ]
        )

        medicos = "\n".join(
            [
                f"{doc.id_doctor} - {doc.full_name} | Email: {doc.email} | Tel: {doc.phone} | Sala: {doc.room} | Especialidad ID: {doc.id_specialty}"
                for doc in medicos_disponibles
            ]
        )

        especialidades_disponibles = "\n".join(
            [
                f"{esp.id_specialty} - {esp.name} | Descripción: {esp.description}"
                for esp in especialidades_disponibles
            ]
        )

        prompt = f"""
Eres un asistente médico. Un usuario te proporcionará sus síntomas y la duración de los mismos. 
Debes dar una recomendación médica clara y concisa (lo necesario, no extenderse) sobre lo que puede hacer sin automedicarse. 
Además, sugiérele consultar con uno de los siguientes profesionales de la clínica, si corresponde:

{medicos}

Especialidades disponibles de los doctores por ID:
{especialidades_disponibles}

Ten en cuenta el historial médico del usuario para responder. Puedes mencionar antecedentes relevantes incluyendo fechas si lo consideras necesario y relacionarlos con los sintomas actuales. 
Si los antecedentes no son relevantes para esta recomendación, omítelos. 

Historial del usuario con sintomas y fechas:
{contexto}

Nuevos síntomas del usuario, con sintomas y fechas: {sintomas}
"""

        headers = {
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "HTTP-Referer": "https://www.sitename.com",
            "X-Title": "MedApp",
            "Content-Type": "application/json",
        }

        body = {
            "model": "deepseek/deepseek-chat-v3-0324:free",
            "messages": [
                {
                    "role": "system",
                    "content": "Eres un asistente médico que da recomendaciones según síntomas teniendo en cuenta las fechas.",
                },
                {"role": "user", "content": prompt},
            ],
        }

        response = httpx.post(OPENROUTER_URL, headers=headers, json=body)
        if response.status_code != 200:
            raise Exception(f"Error al llamar a OpenRouter: {response.text}")

        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        raise e


def obtener_consulta(usuario: str, pregunta_usuario: str, db: Session) -> str:
    try:
        historico = db.query(Historial).filter(Historial.usuario == usuario).all()
        citas_medicas = (
            db.query(Appointment).filter(Appointment.id_patient == usuario).all()
        )
        medicos_disponibles = db.query(Doctor).all()

        medicos = "\n".join(
            [
                f"{doc.id_doctor} - {doc.full_name} | Email: {doc.email} | Tel: {doc.phone} | Sala: {doc.room} | Especialidad ID: {doc.id_specialty}"
                for doc in medicos_disponibles
            ]
        )
        contexto = "\n".join(
            [
                f"Fecha: {h.fecha} | Síntomas: {h.sintomas}\nRecomendación: {h.recomendacion}"
                for h in historico
            ]
        )
        citas_medicas = "\n".join(
            [
                f"Fecha: {cita.date} | Hora: {cita.time} | Descripción: {cita.description} | Doctor ID: {cita.id_doctor}"
                for cita in citas_medicas
            ]
        )

        prompt = f"""
Eres un asistente médico. Un usuario te hará preguntas relacionadas con su historial médico. 
Debes responder de forma clara y concisa, solo con la información necesaria. 
Puedes hacer recomendaciones generales si aplica, pero siempre indica que para una orientación más detallada debe usar el chat de nueva consulta.
No hagas diagnósticos médicos.

Historial médico del usuario:
{contexto}

Citas medicas del usuario:
{citas_medicas}

Nombres de doctores por ID Doctores: 
{medicos}

Pregunta del usuario:
{pregunta_usuario}

Responde con base en su historial, sin hacer diagnósticos médicos explícitos, ten en cuenta muy bien las fechas.
"""

        headers = {
            "Authorization": f"Bearer {os.getenv('OPENROUTER_API_KEY')}",
            "HTTP-Referer": "https://www.sitename.com",
            "X-Title": "MedApp",
            "Content-Type": "application/json",
        }

        body = {
            "model": "deepseek/deepseek-chat-v3-0324:free",
            "messages": [
                {
                    "role": "system",
                    "content": "Eres un asistente médico que analiza el historial del paciente teniendo en cuenta antecedentes médicos y fechas.",
                },
                {"role": "user", "content": prompt},
            ],
        }

        response = httpx.post(OPENROUTER_URL, headers=headers, json=body)
        if response.status_code != 200:
            raise Exception(f"Error al llamar a OpenRouter: {response.text}")

        data = response.json()
        return data["choices"][0]["message"]["content"]
    except Exception as e:
        raise e
