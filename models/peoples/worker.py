from sqlalchemy import *
from models.base import *


class Worker(Base):
    __table__ = 'Workers'

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(50))
    Surname = Column(VARCHAR(50))
    TelegramChatID = Column(BIGINT)
    IsActive = Column(Boolean, default=1)

    def add_new_worker(self, name, surname, telegramchatid, isactive=1):
        self.Name = name
        self.Surname = surname
        self.TelegramChatID = telegramchatid
        self.IsActive = isactive

    #     session.add(self)
    #     session.commit()
    #
    # def get_worker_by_id(self, id):
    #     return session.query(self).filter_by(ID=f'{id}')
