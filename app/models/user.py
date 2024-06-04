from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, TIMESTAMP
from sqlalchemy.orm import relationship

# 导入Base, 创建从它继承的类，这些类就是 SQLAlchemy 模型。
from .base import Base

class User(Base):
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_time = Column(TIMESTAMP)
    updated_time = Column(TIMESTAMP)

    # items = relationship("user_item", back_populates="owner")