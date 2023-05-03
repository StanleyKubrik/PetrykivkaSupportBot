from models.migrate import *
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker


class Worker(Base):
    __tablename__ = 'BotWorkers'

    ID = Column(Integer, primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(50))
    Surname = Column(VARCHAR(50))
    TelegramChatID = Column(BIGINT)
    IsActive = Column(Boolean, default=1)
    DickLength = Column(SMALLINT)
    DickRadius = Column(SMALLINT)
    DickTaste = Column(VARCHAR(50))

    def __init__(self, name, surname, telegramchatid, isactive=1):
        self.Name = name
        self.Surname = surname
        self.TelegramChatID = telegramchatid
        self.IsActive = isactive

    def createWorker(self):
        session.add(self)
        session.commit()

        print('User successfully created!')

    def getWorker(self):
        pass
