from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# 导入Base, 创建从它继承的类，这些类就是 SQLAlchemy 模型。
from .base import Base

class Data_Domain(Base):
    
    ID = Column(String, primary_key=True, index=True)
    Data_Domain_Name = Column(String)
    Data_Domain_EN = Column(String)
    Create_Time = Column(String)
    Update_Time = Column(String)