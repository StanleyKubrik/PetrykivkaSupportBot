from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session


class Commands(Base):
    """Model for work with bot commands."""
    __tablename__ = 'Commands'

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(50), nullable=False)
    Command = Column(VARCHAR(50), nullable=False)

    command_permissions = relationship('CommandPermissions', back_populates='commands')
