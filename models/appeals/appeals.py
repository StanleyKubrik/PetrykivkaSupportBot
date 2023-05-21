from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session
from models.people.users import *
from models.tickets.tickets import *
from models.appeals.appeal_statuses import *
from models.people.departments import *
from datetime import datetime


class Appeals(Base):
    """
    Model for work with appeals from users.

    Attributes:
    ----------
    **User_ID**: user ID in DB\n
    **AppealStatus_ID**: appeals status ID in DB\n
    **Text**: appeals text based on messages\n
    **MediaID**: ID of media (if exist, optional); by default None\n
    **Departament_ID**: department ID in DB\n

    Methods:
    ----------
    **write_in_db()**: write appeal to DB.

    """
    __tablename__ = 'Appeals'
    __table_args__ = (
        {'schema': 'Appeals'}
    )

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    DateTime = Column(DateTime, nullable=False, default=datetime.now())
    User_ID = Column(Integer, ForeignKey('People.Users.ID'), nullable=False)
    AppealStatus_ID = Column(Integer, ForeignKey('Appeals.AppealStatuses.ID'), nullable=False)
    Text = Column(VARCHAR(), nullable=True)
    MediaID = Column(Integer, nullable=True)
    Departament_ID = Column(Integer, ForeignKey('People.Departments.ID'), nullable=False)

    users = relationship('Users', back_populates='appeals')
    tickets = relationship('Tickets', back_populates='appeals')
    appeal_statuses = relationship('AppealStatuses', back_populates='appeals')
    departments = relationship('Departments', back_populates='appeals')
    processed_messages = relationship('ProcessedMessages', back_populates='appeals')

    def write_in_db(self):
        """Write appeal to DB."""
        session.add(self)
        session.commit()
