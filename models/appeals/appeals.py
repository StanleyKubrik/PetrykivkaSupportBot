from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base  # , session
from models.people.users import *
from models.tickets.tickets import *
from models.appeals.appeal_statuses import *
from models.people.departments import *


class Appeals(Base):
    __tablename__ = 'Appeals'
    __table_args__ = (
        # ForeignKeyConstraint(['User_ID'], ['People.Users.ID']),
        # ForeignKeyConstraint(['AppealStatus_ID'], ['Appeals.AppealStatuses.ID']),
        # ForeignKeyConstraint(['Departament_ID'], ['People.Departments.ID']),
        {'schema': 'Appeals'}
    )

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    DateTime = Column(DateTime, nullable=False)
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

    # def get_appeal_by_id(self, appeal_id: int):
    #     return session.query(self).filter_by(ID=f'{appeal_id}')
