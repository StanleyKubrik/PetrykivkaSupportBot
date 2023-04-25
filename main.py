from utils import exchange as e
from bot import telegram_bot
from sql import SQL

if __name__ == '__main__':
    telegram_bot.bot.polling()

    # print(SQL().get_people_by_telegram_id(329518676))
