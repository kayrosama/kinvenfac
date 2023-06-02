from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String, Integer, SmallInteger
from config.database import engine, metadata 
from sqlalchemy import DateTime

users = Table("acc_usuarios", metadata,
             Column("regid", Integer, primary_key=True),
             Column("fecha", DateTime, default=DateTime, nullable=False),
             Column("streg", SmallInteger, nullable=False, default=1),
             Column("usrcode", Integer, nullable=False, default=0),
             Column("knombre", String(50), nullable=True, default="X"),
             Column("kpasswd", String(255), nullable=True, default="X"),
             )

metadata.create_all(engine)
