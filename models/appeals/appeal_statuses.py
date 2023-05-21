from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base  # , session
from models.appeals.appeals import *


class AppealStatuses(Base):
    """Model for work with appeal statuses."""
    __tablename__ = 'AppealStatuses'
    __table_args__ = {'schema': 'Appeals'}

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(50), nullable=False)

    appeals = relationship('Appeals', back_populates='appeal_statuses')
