from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
    regid: Optional[int]
    fecha: Optional[datetime]
    streg: int
    usrcode: int
    knombre: str
    kpasswd: str
    