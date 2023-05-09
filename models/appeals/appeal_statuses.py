from sqlalchemy import *
from models.base import Base, session


class AppealStatuses(Base):
    __tablename__ = 'AppealStatuses'
    __table_args__ = {'schema': 'Appeals'}

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(50), nullable=False)
