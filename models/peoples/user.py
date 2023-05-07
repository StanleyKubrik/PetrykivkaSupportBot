from sqlalchemy import *
from models.base import Base


class User(Base):
    __tablename__ = 'Users'
    # __table_args__ = {'schema': 'Peoples'}

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    Name = Column(VARCHAR(50), nullable=False)
    Surname = Column(VARCHAR(50), nullable=False)
    TelegramChatID = Column(BIGINT, nullable=False)
    IsActive = Column(Boolean, nullable=False, default=1)

    def add_new_user(self, name, surname, telegramchatid, isactive=1):
        self.Name = name
        self.Surname = surname
        self.TelegramChatID = telegramchatid
        self.IsActive = isactive

    #     session.add(self)
    #     session.commit()
    #
    # def get_user_by_id(self, id):
    #     return session.query(self).filter_by(ID=f'{id}')
