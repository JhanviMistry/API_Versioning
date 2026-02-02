from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str

class UserV1(UserBase):
    id: int

class UserV2(UserV1):
    email: EmailStr