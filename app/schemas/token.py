from pydantic import BaseModel
from typing import Optional

# 定义令牌端点响应的 Pydantic 模型
class Token(BaseModel):
    access_token: str
    token_type: str

# 定义用户发送的token对象
class TokenPayload(BaseModel):
    sub: Optional[str] = None