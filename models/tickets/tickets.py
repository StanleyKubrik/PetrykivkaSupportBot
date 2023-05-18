from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session
from models.people.users import *
from models.appeals.appeals import *
from models.tickets.ticket_categories import *
from models.tickets.ticket_category_property_values import *


class Tickets(Base):
    __tablename__ = 'Tickets'
    __table_args__ = (
        # ForeignKeyConstraint(['Appeal_ID'], ['Appeals.Appeals.ID']),
        # ForeignKeyConstraint(['TicketCategory_ID'], ['Tickets.TicketCategories.ID']),
        # ForeignKeyConstraint(['User_ID'], ['People.Users.ID']),
        # ForeignKeyConstraint(['Responsible_ID'], ['People.Users.ID']),
        {'schema': 'Tickets'}
    )

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    DateTime = Column(DateTime, nullable=False)
    User_ID = Column(Integer, ForeignKey('People.Users.ID'), nullable=False)
    Appeal_ID = Column(Integer, ForeignKey('Appeals.Appeals.ID'), nullable=False)
    TicketCategory_ID = Column(Integer, ForeignKey('Tickets.TicketCategories.ID'), nullable=False)
    Responsible_ID = Column(Integer)  # , ForeignKey('People.Users.ID'))

    users = relationship('Users', back_populates='tickets')
    appeals = relationship('Appeals', back_populates='tickets')
    ticket_category = relationship('TicketCategories', back_populates='tickets')
    ticket_category_property_values = relationship('TicketCategoryPropertyValues', back_populates='tickets')

    # def get_ticket_by_id(self, ticket_id: int):
    #     return session.query(self).filter_by(ID=f'{ticket_id}')
