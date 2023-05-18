from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session
from models.appeals.processed_messages import *
from models.appeals.appeals import *
from models.tickets.tickets import *
from models.people.roles import *


class Users(Base):
    __tablename__ = 'Users'
    __table_args__ = {'schema': 'People'}

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(50), nullable=False)
    Surname = Column(VARCHAR(50), nullable=False)
    PhoneNumber = Column(Integer, nullable=False)
    TelegramChatID = Column(BIGINT, nullable=False)
    Role_ID = Column(Integer, ForeignKey('People.Roles.ID'), nullable=False)
    IsActive = Column(Boolean, nullable=False, default=1)

    processed_messages = relationship('ProcessedMessages', back_populates='users')
    appeals = relationship('Appeals', back_populates='users')
    tickets = relationship('Tickets', back_populates='users')
    roles = relationship('Roles', back_populates='users')

    def get_user_by_id(self, user_id: int):
        return session.query(self).filter_by(ID=f'{user_id}')


def get_user_by_telegram_id(user_telegram_id: int):
    if session.query(Users).filter_by(TelegramChatID=f'{user_telegram_id}') is not None:
        return 1
    else:
        return 0
