from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

# from app.core.config import settings
from app.models.base import Base

# 为 SQLAlchemy 定义数据库 URL地址
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:175161Ugi!0617@localhost:5432/datacenter"

# 创建一个 SQLAlchemy的“引擎”
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# 判断写入的数据库是否存在
if not database_exists(engine.url):
    create_database(engine.url)

# 创建模型
Base.metadata.create_all(engine)
print("数据库连接成功!")
# 创建一个SessionLocal类，用于创建数据库会话的实例,但该类本身还不是数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
