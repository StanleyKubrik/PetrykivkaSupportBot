from sqlalchemy.orm import declarative_base, sessionmaker
from sql import SQL

mig_engine = SQL().engine
Base = declarative_base()

Session = sessionmaker(mig_engine)
session = Session()


def migrate():
    Base.metadata.create_all(mig_engine)
