from fastapi import APIRouter

from app.api.v1.data import data_domain
from app.api.v1.user import user_manage

api_router = APIRouter()
api_router.include_router(data_domain.router, prefix="/data", tags=["数据管理"])
api_router.include_router(user_manage.router, prefix="/user", tags=["用户管理"])
