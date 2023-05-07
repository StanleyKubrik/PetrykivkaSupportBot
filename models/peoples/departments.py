from sqlalchemy import *
from models.base import *


class Department(Base):
    __tablename__ = 'Departments'
    # __table_args__ = {'schema': 'Peoples'}

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(50), nullable=False)
