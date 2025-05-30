from database import Base

from sqlalchemy import Column, Integer, String, Date

class Historial(Base):
    __tablename__ = "historial"

    id = Column(Integer, primary_key=True, index=True)
    usuario = Column(String, index=True)
    sintomas = Column(String)
    recomendacion = Column(String)
    fecha = Column(Date)