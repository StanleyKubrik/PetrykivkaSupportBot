from bot.telegram_bot import bot
from sqlalchemy import *
from sql import SQL
from sqlalchemy.orm import declarative_base, sessionmaker
from models.peoples.worker import *
from models.migrate import session

if __name__ == '__main__':
    migrate()
    #
    # # bot.polling()
    #
    # worker = Worker('Vlad', 'Petryk', 327444916)
    # worker.createWorker()

    # print(session.query(Worker).all())
