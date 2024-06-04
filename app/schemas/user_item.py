from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class ItemCreate(UserItemBase):
    title: str


# Properties to receive on item update
class ItemUpdate(UserItemBase):
    pass


# Properties shared by models stored in DB
class UserItemInDBBase(UserItemBase):
    id: int
    title: str
    owner_id: int

    class Config:
        orm_mode = True


# Properties to return to client
class UserItem(UserItemInDBBase):
    pass


# Properties properties stored in DB
class UserItemInDB(UserItemInDBBase):
    pass
