from pydantic import BaseModel


class UserBase(BaseModel):
    full_name: str
    email: str
    role: str
    password:str




class UserInDB(UserBase):
    id_user: int    

    class Config:
        orm_mode = True
