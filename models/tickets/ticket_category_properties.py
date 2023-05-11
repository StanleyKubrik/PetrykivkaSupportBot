from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session


class TicketCategoryProperties(Base):
    __tablename__ = 'TicketCategoryProperties'
    __table_args__ = (
        ForeignKeyConstraint(['TicketCategory_ID'], ['Tickets.TicketCategories.ID']),
        {'schema': 'Tickets'}
    )

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    UpdateDateTime = Column(DateTime, nullable=False)
    TicketCategory_ID = Column(Integer, nullable=False)

    ticket_category = relationship('Tickets.TicketCategories', back_populates='ticket_category_properties')
    ticket_category_property_values = relationship('Tickets.TicketCategoryPropertyValues',
                                                   back_populates='tickets_category_properties')
