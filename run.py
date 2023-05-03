from bot.telegram_bot import bot
from sqlalchemy import *
from sql import SQL
from sqlalchemy.orm import declarative_base, sessionmaker
from models.peoples.worker import *


if __name__ == '__main__':
    # bot.polling()

    migrate()
    vlad = Worker('Vlad', 'Petryk', 327444916)
    vlad.create_worker()
