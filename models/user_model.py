from sqlalchemy import Column, String
from database import Base


class Users(Base):
    __tablename__ = "users"

    id_user = Column(int, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    role = Column(String(20), nullable=False)
