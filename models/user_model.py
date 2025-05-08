from sqlalchemy import Column, String
from database import Base


class Users(Base):
    __tablename__ = "users"

    id_user = Column(int, primary_key=True, index=True)
    full_name = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    role = Column(String(20), nullable=False)
