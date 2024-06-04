from typing import TYPE_CHECKING
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# 从database导入Base, 创建从它继承的类，这些类就是 SQLAlchemy 模型。
from app.db.session import Base

class User_Item(Base):
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    # owner_id = Column(Integer, ForeignKey("user.id"))

    # owner = relationship("user", back_populates="items")
