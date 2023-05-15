from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base  # , session


class Roles(Base):
    __tablename__ = 'Roles'
    __table_args__ = {'schema': 'People'}

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(50), nullable=False)

    users = relationship('People.Users', back_populates='roles')
