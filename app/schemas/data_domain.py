from typing import Optional

from pydantic import BaseModel


# Shared properties
class DataDomainCreate(BaseModel):
    ID: str
    Data_Domain_Name: str
    Data_Domain_EN: str


class DataDomainUpdate(BaseModel):
    Data_Domain_EN: str

class DataDomainDetails(BaseModel):
    ID: str
    Data_Domain_Name: str
    Data_Domain_EN: str