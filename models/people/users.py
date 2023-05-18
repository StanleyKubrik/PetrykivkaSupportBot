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
    PhoneNumber = Column(BIGINT, nullable=False)
    TelegramChatID = Column(BIGINT, nullable=False)
    Role_ID = Column(Integer, ForeignKey('People.Roles.ID'), nullable=False)
    IsActive = Column(Boolean, nullable=False, default=1)

    processed_messages = relationship('ProcessedMessages', back_populates='users')
    appeals = relationship('Appeals', back_populates='users')
    tickets = relationship('Tickets', back_populates='users')
    roles = relationship('Roles', back_populates='users')

    def get_user_by_id(self, user_id: int):
        return session.query(self).filter_by(ID=f'{user_id}')


def get_user_role_by_telegram_id(user_telegram_id: int):
    return session.query(Users.Role_ID)\
        .filter(and_(Users.TelegramChatID == user_telegram_id, Users.IsActive == 1))\
        .scalar()


def get_admins_chat_id():
    return session.query(Users.TelegramChatID) \
        .filter(and_(Users.Role_ID == 1, Users.IsActive == 1)) \
        .all()
