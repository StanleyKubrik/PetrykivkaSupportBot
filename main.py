import exchange as e
from telegram_bot import bot
from sql import SQL
from sqlalchemy import text

if __name__ == '__main__':
    bot.polling()
    # result = e.exchangeRun('Peremoga')
    # print(result)
    # e.runTask('ExchangeSQL-Petrykivka', None, 'current')

    # print(SQL().get_people_by_telegram_id(329518676))
