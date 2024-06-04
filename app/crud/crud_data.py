from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.data_domain import Data_Domain
from app.schemas.data_domain import DataDomainCreate, DataDomainUpdate, DataDomainDetails


class CRUDData(CRUDBase[Data_Domain, DataDomainCreate, DataDomainUpdate]):
    def getByDataDomainName(
        self, db: Session, domainName: str
    ) -> DataDomainDetails:
        rest = db.query(self.model).filter(
            Data_Domain.Data_Domain_Name == domainName).first()
        return DataDomainDetails(**jsonable_encoder(rest))


data = CRUDData(Data_Domain)
