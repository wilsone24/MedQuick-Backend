from sqlalchemy import Column, String, Integer
from database import Base


class User(Base):
    __tablename__ = "users"

    id_user = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(30), nullable=False)
    email = Column(String(40), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(String(30), nullable=False)
