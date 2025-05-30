import httpx
from sqlalchemy.orm import Session
from models.historial_model import Historial
from dotenv import load_dotenv
import os

load_dotenv()


OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"


def obtener_recomendacion(usuario: str, sintomas: str, db: Session):
    try:
        historico = db.query(Historial).filter(Historial.usuario == usuario).all()
        contexto = "\n".join(
            [
                f"Fecha: {h.fecha} | Síntomas: {h.sintomas}\nRecomendación: {h.recomendacion}"
                for h in historico
            ]
        )

        prompt = f"""
Eres un asistente médico. Con base en estos antecedentes del usuario:
{contexto}

Y los nuevos síntomas: {sintomas}

Da una recomendación clara (sin diagnosticar directamente). Ten en cuenta los antecedentes para responder, si los hay. Puedes mencionar antecedentes relevantes en tu respuesta teniendo en cuenta las fechas.
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
        contexto = "\n".join(
            [
                f"Fecha: {h.fecha} | Síntomas: {h.sintomas}\nRecomendación: {h.recomendacion}"
                for h in historico
            ]
        )

        prompt = f"""
Eres un asistente médico. Este es el historial médico del usuario:

{contexto}

El usuario pregunta: {pregunta_usuario}

Responde con base en su historial, sin hacer diagnósticos médicos explícitos, ten en cuenta las fechas.
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
