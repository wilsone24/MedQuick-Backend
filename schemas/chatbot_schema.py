from pydantic import BaseModel
from datetime import date

class Consulta(BaseModel):
    usuario: str
    sintomas: str
    fecha: date

class Pregunta(BaseModel):
    usuario: str
    pregunta: str
