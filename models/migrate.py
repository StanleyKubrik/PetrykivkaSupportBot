from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import *
from sql import SQL

# mig_engine = SQL().eng
engine = create_engine("sqlite:///models/hui.sqlite3", echo=True)
Base = declarative_base()

Session = sessionmaker(engine)
session = Session()


def migrate():
    # Base.metadata.create_all(engine)
    Base.metadata.clear()
