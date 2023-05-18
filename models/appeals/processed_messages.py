from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session
from models.people.users import *
from models.appeals.appeals import *


class ProcessedMessages(Base):
    __tablename__ = 'ProcessedMessages'
    __table_args__ = (
        #     ForeignKeyConstraint(['User_ID'], ['People.Users.ID']),
        #     ForeignKeyConstraint(['Appeal_ID'], ['Appeals.Appeals.ID']),
        {'schema': 'Appeals'}
    )

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    DateTime = Column(DateTime, nullable=False)
    User_ID = Column(Integer, ForeignKey('People.Users.ID'), nullable=False)
    TelegramMessageID = Column(Integer, nullable=False)
    MessageData = Column(VARCHAR())
    Appeal_ID = Column(Integer, ForeignKey('Appeals.Appeals.ID'))

    users = relationship('Users', back_populates='processed_messages')
    appeals = relationship('Appeals', back_populates='processed_messages')
