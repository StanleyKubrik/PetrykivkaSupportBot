from sqlalchemy import *
from models.base import Base, session


class Worker(Base):
    __tablename__ = 'Workers'
    __table_args__ = {'schema': 'Peoples'}

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(50), nullable=False)
    Surname = Column(VARCHAR(50), nullable=False)
    TelegramChatID = Column(BIGINT, nullable=False)
    IsActive = Column(Boolean, nullable=False, default=1)

    def add_new_worker(self, name: str, surname: str, telegramchatid: int, isactive: bool = 1):
        self.Name = name
        self.Surname = surname
        self.TelegramChatID = telegramchatid
        self.IsActive = isactive

        session.add(self)
        session.commit()

    def get_worker_by_id(self, worker_id: int):
        return session.query(self).filter_by(ID=f'{worker_id}')
