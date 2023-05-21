"""File for work with SQLAlchemy ORM mapper and session."""
from sqlalchemy.orm import declarative_base, sessionmaker
from utils.sql import SQL

sql_engine = SQL('PetrykivkaSupportBot').engine
Base = declarative_base()

Session = sessionmaker(sql_engine)
session = Session()
