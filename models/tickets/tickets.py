from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session


class Tickets(Base):
    __tablename__ = 'Tickets'
    __table_args__ = (
        ForeignKeyConstraint(['Appeal_ID'], ['Appeals.Appeals.ID']),
        ForeignKeyConstraint(['TicketCategory_ID'], ['Tickets.TicketCategories.ID']),
        ForeignKeyConstraint(['Worker_ID'], ['People.Workers.ID']),
        ForeignKeyConstraint(['Responsible_ID'], ['People.Workers.ID']),
        {'schema': 'Tickets'}
    )

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    DateTime = Column(DateTime, nullable=False)
    Worker_ID = Column(Integer, nullable=False)
    Appeal_ID = Column(Integer, nullable=False)
    TicketCategory_ID = Column(Integer, nullable=False)
    Responsible_ID = Column(Integer)

    workers = relationship('People.Workers', back_populates='tickets')
    appeals = relationship('Appeals.Appeals', back_populates='tickets')
    ticket_category = relationship('Tickets.TicketCategories', back_populates='tickets')
    ticket_category_property_values = relationship('Tickets.TicketCategoryPropertyValues', back_populates='tickets')

    def get_ticket_by_id(self, ticket_id: int):
        return session.query(self).filter_by(ID=f'{ticket_id}')
