import telebot as tb
from config.config import *

# from sql import SQL

APP_CONFIG_PATH = './config/config.ini'
app_config = Config(APP_CONFIG_PATH)
roles = {
    329518676: 'support',
    327444916: 'user'
}
COMMANDS = {
    'support': [tb.types.BotCommand('/start', 'Start'),
                tb.types.BotCommand('/exchange', 'Exchange 1C7-SQL'),
                tb.types.BotCommand('/show_yurec', 'Yurec')
                ],
    'user': [tb.types.BotCommand('/show_dick', 'Dick'),
             tb.types.BotCommand('/show_yurec', 'Yurec')]
}
bot = tb.TeleBot(app_config.get_setting('TelegramAPI', 'api_key'))


# connect = SQL()


@bot.message_handler(commands=['start'])
def start(message):
    if roles.get(message.chat.id) == 'support':
        bot.set_my_commands(COMMANDS.get('support'))
        bot.send_message(message.chat.id, f'Hello, bitch! What do you want?')
    else:
        bot.set_my_commands(COMMANDS.get('user'))
        bot.send_message(message.chat.id, f'Do u want see my dick?')


@bot.message_handler(commands=['show_yurec'])
def show_yurec(message):
    with open('ph.jpg', 'rb') as ph:
        bot.send_photo(message.chat.id, ph)
