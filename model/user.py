from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import String, BigInteger, Integer, SmallInteger, DateTime
from config.db import engine, metadata
from datetime import datetime

users = Table("acc_usuarios", metadata,
             Column("regid", Integer, primary_key=True),
             Column("fecha", DateTime, default=datetime.now, nullable=False),
             Column("fechamod", DateTime, default=datetime.now, onupdate=datetime.now, nullable=False),
             Column("streg", SmallInteger, nullable=False, default=1),
             Column("modulo", SmallInteger, nullable=False, default=1),
             Column("modtipo", SmallInteger, nullable=False, default=1),
             Column("modnivel", SmallInteger, nullable=False, default=1),
             Column("usrcode", Integer, nullable=False, default=0),
             Column("nombres", String(50), nullable=True, default="X"),
             Column("apeuno", String(20), nullable=True, default="X"),
             Column("apedos", String(20), nullable=True, default="X"),
             Column("apetres", String(20), nullable=True, default="X"),
             Column("paisuno", SmallInteger, nullable=True, default=1),
             Column("teluno", BigInteger, nullable=True, default=0),
             Column("paisdos", SmallInteger, nullable=True, default=1),
             Column("teldos", BigInteger, nullable=True, default=0),
             )

metadata.create_all(engine)
