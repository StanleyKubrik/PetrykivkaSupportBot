from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base  # , session


class Departments(Base):
    __tablename__ = 'Departments'
    __table_args__ = {'schema': 'People'}

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(50), nullable=False)

    appeals = relationship('Appeals.Appeals', back_populates='departments')
