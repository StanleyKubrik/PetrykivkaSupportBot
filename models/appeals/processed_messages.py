from sqlalchemy import *
from models.base import Base, session


class ProcessedMessages(Base):
    __tablename__ = 'ProcessedMessages'
    __table_args__ = {'schema': 'Appeals'}

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    DateTime = Column(DateTime, nullable=False)
    TelegramMessageID = Column(Integer, nullable=False)
    MessageData = Column(VARCHAR(), nullable=True)
    Appeal_ID = Column(Integer, nullable=True)
