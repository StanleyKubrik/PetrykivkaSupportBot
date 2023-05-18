from bot.telegram_bot import bot
# from models.base import sql_engine
from models.base import session
from models.people.users import *


if __name__ == '__main__':
    # bot.polling()

    print(session.query(Users.Name).filter(Users.TelegramChatID == 329518676).scalar())
