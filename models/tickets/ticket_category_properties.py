from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session
from models.tickets.ticket_categories import *
from models.tickets.ticket_category_property_values import *


class TicketCategoryProperties(Base):
    __tablename__ = 'TicketCategoryProperties'
    __table_args__ = (
        # ForeignKeyConstraint(['TicketCategory_ID'], ['Tickets.TicketCategories.ID']),
        {'schema': 'Tickets'}
    )

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    UpdateDateTime = Column(DateTime, nullable=False)
    TicketCategory_ID = Column(Integer, ForeignKey('Tickets.TicketCategories.ID'), nullable=False)

    ticket_category = relationship('TicketCategories', back_populates='ticket_category_properties')
    ticket_category_property_values = relationship('TicketCategoryPropertyValues',
                                                   back_populates='tickets_category_properties')
