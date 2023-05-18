from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session
from models.tickets.tickets import *
from models.tickets.ticket_category_properties import *


class TicketCategoryPropertyValues(Base):
    __tablename__ = 'TicketCategoryPropertyValues'
    __table_args__ = (
        # ForeignKeyConstraint(['Ticket_ID'], ['Tickets.Tickets.ID']),
        # ForeignKeyConstraint(['TicketCategoryProperty_ID'], ['Tickets.TicketCategoryProperties.ID']),
        {'schema': 'Tickets'}
    )

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    UpdateDateTime = Column(DateTime, nullable=False)
    Ticket_ID = Column(Integer, ForeignKey('Tickets.Tickets.ID'), nullable=False)
    TicketCategoryProperty_ID = Column(Integer, ForeignKey('Tickets.TicketCategoryProperties.ID'), nullable=False)
    Value = Column(VARCHAR(), nullable=False)

    tickets = relationship('Tickets', back_populates='ticket_category_property_values')
    tickets_category_properties = relationship('TicketCategoryProperties',
                                               back_populates='ticket_category_property_values')
