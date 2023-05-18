import telebot as tb
from config.config import *
from models.people.users import *

APP_CONFIG_PATH = './config/config.ini'
app_config = Config(APP_CONFIG_PATH)
COMMANDS = {
    1: [tb.types.BotCommand('/start', 'Start'),
        tb.types.BotCommand('/show_dick', 'Dick'),
        tb.types.BotCommand('/show_yurec', 'Yurec'),
        tb.types.BotCommand('/exchange', 'Exchange 1C7-SQL')
        ],
    3: [tb.types.BotCommand('/start', 'Start'),
        tb.types.BotCommand('/show_yurec', 'Yurec')]
}
bot = tb.TeleBot(app_config.get_setting('TelegramAPI', 'api_key'))


@bot.message_handler(commands=['start'])
def start(message):
    user_role = get_user_role_by_telegram_id(message.chat.id)
    set_bot_command(user_role, message.chat.id)


@bot.message_handler(commands=['show_yurec'])
def show_yurec(message):
    with open('yurec.jpg', 'rb') as ph:
        bot.send_photo(message.chat.id, ph)


@bot.message_handler(commands=['show_dick'])
def show_dick(message):
    with open('dick.jpg', 'rb') as ph:
        bot.send_photo(message.chat.id, ph)


def set_bot_command(user_role, chat_id):
    if user_role == 1:
        bot.set_my_commands(COMMANDS.get(1))
        bot.send_message(chat_id, f'Hello, bitch! What do you want?')
    elif user_role == 3:
        bot.set_my_commands(COMMANDS.get(3))
        markup = tb.types.ReplyKeyboardMarkup()
        markup.add(tb.types.KeyboardButton('Подати звернення'))
        bot.send_message(chat_id, f'Hello, Galya! What do you want?')
    else:
        bot.send_message(chat_id, f'Who are u?')
