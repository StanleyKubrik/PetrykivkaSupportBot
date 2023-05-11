from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session


class TicketCategories(Base):
    __tablename__ = 'TicketCategories'
    __table_args__ = {'schema': 'Tickets'}

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(100), nullable=False)
    UpdateDateTime = Column(DateTime, nullable=False)

    tickets = relationship('Tickets.Tickets', back_populates='ticket_category')
    ticket_category_properties = relationship('Tickets.TicketCategoryProperties', back_populates='ticket_category')
