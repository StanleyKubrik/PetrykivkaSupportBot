import telebot as tb
from sqlalchemy import *
from sqlalchemy.orm import relationship
from models.base import Base, session
from models.commands import *
from models.people.roles import *


class CommandPermissions(Base):
    __tablename__ = 'CommandPermissions'

    ID = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    Command_ID = Column(Integer, ForeignKey('Commands.ID'), nullable=False)
    Role_ID = Column(Integer, ForeignKey('People.Roles.ID'), nullable=False)

    commands = relationship('Commands', back_populates='command_permissions')
    roles = relationship('Roles', back_populates='command_permissions')


def generate_command_list(role_id):
    commands_tuples_list = session.query(Commands.Command, Commands.Name) \
        .join(CommandPermissions) \
        .filter(CommandPermissions.Role_ID == role_id) \
        .all()
    commands_list = []

    for ct in commands_tuples_list:
        command = tb.types.BotCommand(ct[0], ct[1])
        commands_list.append(command)

    return commands_list
