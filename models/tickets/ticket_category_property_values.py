from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session


class TicketCategoryPropertyValues(Base):
    __tablename__ = 'TicketCategoryPropertyValues'
    __table_args__ = (
        ForeignKeyConstraint(['Ticket_ID'], ['Tickets.Tickets.ID']),
        ForeignKeyConstraint(['TicketCategoryProperty_ID'], ['Tickets.TicketCategoryProperties.ID']),
        {'schema': 'Tickets'}
    )

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    UpdateDateTime = Column(DateTime, nullable=False)
    Ticket_ID = Column(Integer, nullable=False)
    TicketCategoryProperty_ID = Column(Integer, nullable=False)
    Value = Column(VARCHAR(), nullable=False)

    tickets = relationship('Tickets.Tickets', back_populates='ticket_category_property_values')
    tickets_category_properties = relationship('Tickets.TicketCategoryProperties', back_populates='ticket_category')
