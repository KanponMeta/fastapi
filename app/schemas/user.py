from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    is_active: Optional[bool] = True
    is_superuser: bool = False
    username: Optional[str] = None
    email: Optional[EmailStr] = None


# Properties to receive via API on creation
class UserCreate(BaseModel):
    username: str
    password: str
    email: Optional[EmailStr] = None


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
