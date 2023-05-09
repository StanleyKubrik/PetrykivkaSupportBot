from sqlalchemy import *
from models.base import Base, session


class TicketCategoryProperties(Base):
    __tablename__ = 'TicketCategoryProperties'
    __table_args__ = {'schema': 'Tickets'}

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    UpdateDateTime = Column(DateTime, nullable=False)
    Ticket_ID = Column(Integer, ForeignKey('Tickets.Tickets.ID', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    TicketCategoryProperty_ID = Column(Integer, ForeignKey('Tickets.Tickets.ID', onupdate='CASCADE', ondelete='CASCADE'), nullable=False)
    Value = Column(VARCHAR(), nullable=False)

    def get_ticket_by_id(self, ticket_id: int):
        return session.query(self).filter_by(ID=f'{ticket_id}')
