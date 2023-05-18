import telebot as tb
from config.config import *
from models.base import session

APP_CONFIG_PATH = './config/config.ini'
app_config = Config(APP_CONFIG_PATH)
roles = {
    329518676: 'support',
    327444916: 'user'
}
COMMANDS = {
    1: [tb.types.BotCommand('/start', 'Start'),
        tb.types.BotCommand('/show_dick', 'Dick'),
        tb.types.BotCommand('/show_yurec', 'Yurec'),
        tb.types.BotCommand('/exchange', 'Exchange 1C7-SQL')
        ],
    2: [tb.types.BotCommand('/start', 'Start'),
        tb.types.BotCommand('/show_yurec', 'Yurec')]
}
bot = tb.TeleBot(app_config.get_setting('TelegramAPI', 'api_key'))


@bot.message_handler(commands=['start'])
def start(message):
    user_role = session.get()
    # if roles.get(message.chat.id) == 'support':
    #     bot.set_my_commands(COMMANDS.get('support'))
    #     bot.send_message(message.chat.id, f'Hello, bitch! What do you want?')
    # else:
    #     bot.set_my_commands(COMMANDS.get('user'))
    #     bot.send_message(message.chat.id, f'Do u want see my dick?')


@bot.message_handler(commands=['show_yurec'])
def show_yurec(message):
    with open('ph.jpg', 'rb') as ph:
        bot.send_photo(message.chat.id, ph)
