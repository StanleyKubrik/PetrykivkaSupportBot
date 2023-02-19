import exchange as e
from telegram_bot import bot
import time


if __name__ == '__main__':
    # bot.polling()
    result = e.exchangeRun('Petrykivka')
    print(result)
    # e.runTask('ExchangeSQL-Petrykivka', None, 'current')
