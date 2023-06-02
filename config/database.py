from sqlalchemy import create_engine, MetaData

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://kohana:Kinteki#69@127.0.0.1:3306/ksmdb"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

conn = engine.connect()

metadata = MetaData()
