from sqlalchemy.orm import declarative_base, sessionmaker
from models.sql import SQL

sql_engine = SQL().engine
Base = declarative_base()

Session = sessionmaker(sql_engine)
session = Session()
