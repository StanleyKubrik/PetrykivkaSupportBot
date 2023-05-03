from models.migrate import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker


class Worker(Base):
    __tablename__ = 'BotWorkers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50))
    surname = Column(VARCHAR(50))
    telegramchatid = Column(BIGINT)
    isactive = Column(Boolean, default=1)

    def __init__(self, name, surname, telegramchatid, isactive=1):
        self.name = name
        self.surname = surname
        self.telegramchatid = telegramchatid
        self.isactive = isactive

    def create_worker(self):
        session.add(self)
        session.commit()

        print('User successfully created!')
