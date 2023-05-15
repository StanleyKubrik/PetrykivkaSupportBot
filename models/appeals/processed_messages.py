from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base  # , session


class ProcessedMessages(Base):
    __tablename__ = 'ProcessedMessages'
    __table_args__ = (
        ForeignKeyConstraint(['User_ID'], ['People.Users.ID']),
        ForeignKeyConstraint(['Appeal_ID'], ['Appeals.Appeals.ID']),
        {'schema': 'Appeals'}
    )

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    DateTime = Column(DateTime, nullable=False)
    User_ID = Column(Integer, nullable=False)
    TelegramMessageID = Column(Integer, nullable=False)
    MessageData = Column(VARCHAR())
    Appeal_ID = Column(Integer)

    users = relationship('People.Users', back_populates='processed_messages')
    appeals = relationship('Appeals.Appeals', back_populates='processed_messages')
