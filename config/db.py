from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://kohana:Kinteki#69@127.0.0.1:3306/ksmdb")

conn = engine.connect()

metadata = MetaData()
