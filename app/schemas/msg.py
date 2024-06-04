from pydantic import BaseModel

class Msg(BaseModel):
    code: str
    msg: str
