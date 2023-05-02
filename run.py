from bot.telegram_bot import bot
from sqlalchemy import *
from sql import SQL
from sqlalchemy.orm import declarative_base, sessionmaker
from models.migrate import Base


if __name__ == '__main__':
    # bot.polling()

    engine = SQL().engine
    Base.metadata.create_all(engine)
