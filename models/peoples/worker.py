# from models.migrate import Base
from sqlalchemy import *
from sql import SQL
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()


class Worker(Base):
    __tablename__ = 'BotWorkers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50))
    surname = Column(VARCHAR(50))
    telegramchatid = Column(BIGINT)
    isactive = Column(BOOLEAN, default=1)


# Session = sessionmaker(engine)
# session = Session()
# new_worker = Worker(name='Vlad', surname='Petryk', telegramchatid='513153658')
# session.add(new_worker)
# session.commit()
