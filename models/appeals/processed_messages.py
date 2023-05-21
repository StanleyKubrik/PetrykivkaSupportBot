from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session
from models.people.users import *
from models.appeals.appeals import *
from datetime import datetime


class ProcessedMessages(Base):
    """
    Model for work with new messages from users to bot.

    Attributes:
    ----------
    **User_ID**: user ID in DB\n
    **TelegramMessageID**: Telegram ID of a processed message\n
    **MessageData**: data (text, media etc.) of a processed message; for media need to write Telegram ID's\n
    **Appeal_ID**: appeal ID that based on the current processed message\n

    Methods:
    ----------
    **write_in_db()**: write processed message to DB.

    """

    __tablename__ = 'ProcessedMessages'
    __table_args__ = (
        {'schema': 'Appeals'}
    )

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    DateTime = Column(DateTime, nullable=False, default=datetime.now())
    User_ID = Column(Integer, ForeignKey('People.Users.ID'), nullable=False)
    TelegramMessageID = Column(Integer, nullable=False)
    MessageData = Column(VARCHAR())
    Appeal_ID = Column(Integer, ForeignKey('Appeals.Appeals.ID'))

    users = relationship('Users', back_populates='processed_messages')
    appeals = relationship('Appeals', back_populates='processed_messages')

    def write_in_db(self):
        """Write processed message to DB."""
        session.add(self)
        session.commit()


def get_new_msg_by_user(user_id) -> dict:
    session.query(ProcessedMessages)\
        .filter(and_(ProcessedMessages.User_ID == user_id, ProcessedMessages.Appeal_ID is None))\
        .all()
