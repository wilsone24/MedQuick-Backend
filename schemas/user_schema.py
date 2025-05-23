from pydantic import BaseModel


class UserBase(BaseModel):
    full_name: str
    email: str
    password: str


class UserInDB(UserBase):
    id_user: int
    role: str

    class Config:
        orm_mode = True
