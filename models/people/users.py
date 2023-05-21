from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session
from models.appeals.processed_messages import *
from models.appeals.appeals import *
from models.tickets.tickets import *
from models.people.roles import *


class Users(Base):
    """Model for work with bot users."""
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


def get_user_id_by_tg_id(tg_chat_id: int) -> int:
    """
    Return user ID.

    :param tg_chat_id: user Telegram chat ID
    :return: user ID
    """
    return session.query(Users.ID)\
        .filter(and_(Users.TelegramChatID == tg_chat_id, Users.IsActive == 1))\
        .scalar()


def get_user_role_by_tg_id(user_tg_id: int) -> int:
    """
    Return ID of user role.

    :param user_tg_id: user Telegram chat ID
    :return: user role ID
    """
    return session.query(Users.Role_ID)\
        .filter(and_(Users.TelegramChatID == user_tg_id, Users.IsActive == 1))\
        .scalar()


def get_admins_chat_id() -> list:
    """
    Return list of current admins IDs.

    :return: list of admins IDs.
    """
    return session.query(Users.TelegramChatID) \
        .filter(and_(Users.Role_ID == 1, Users.IsActive == 1)) \
        .all()
