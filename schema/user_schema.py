from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    regid: Optional[int]
    fecha: Optional[datetime]
    fechamod: Optional[datetime]
    streg: int
    modulo: int
    modtipo: int
    modnivel: int
    usrcode: int
    nombres: str
    apeuno: str
    apedos: str
    apetres: Optional[str]
    paisuno: int
    teluno: int
    paisdos: int
    teldos: int
    