from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session


class Tickets(Base):
    __tablename__ = 'Tickets'
    __table_args__ = {'schema': 'Tickets'}

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    DateTime = Column(DateTime, nullable=False)
    Appeal_ID = Column(Integer, ForeignKey('Appeals.Appeals.ID', onupdate='CASCADE', ondelete='CASCADE'),
                       nullable=False)
    TicketCategory_ID = Column(Integer, ForeignKey('Tickets.TicketCategories.ID',
                                                   onupdate='CASCADE',
                                                   ondelete='CASCADE'),
                               nullable=False)

    appeals = relationship('Appeals.Appeals', back_populates='tickets')
    ticket_category = relationship('Tickets.TicketCategories', back_populates='tickets')

    def get_ticket_by_id(self, ticket_id: int):
        return session.query(self).filter_by(ID=f'{ticket_id}')
