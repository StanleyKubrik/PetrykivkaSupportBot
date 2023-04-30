from models.migrate import Base
from sqlalchemy import *


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(50))
    surname = Column(VARCHAR(50))
    telegramchatid = Column(BIGINT)
    isactive = Column(BOOLEAN, default=1)
