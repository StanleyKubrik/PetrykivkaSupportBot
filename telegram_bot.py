import telebot as tb
import exchange as e
from sql import SQL

API_KEY = '6060675197:AAEzZB1pKlZ0Tw26l9zZupgn5Nbbf9TK4dc'
COMMANDS = [tb.types.BotCommand('/start', 'Start'),
            tb.types.BotCommand('/exchange', 'Exchange 1C7-SQL')
            ]
bot = tb.TeleBot(API_KEY)
bot.set_my_commands(COMMANDS)
connect = SQL()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hello, bitch! What do you want?')


@bot.message_handler(commands=['exchange'])
def choose_base_for_exchange(message):
    # bases = ['Petrykivka', 'Peremoga']
    markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True)
    petrykivka = tb.types.KeyboardButton('Petrykivka')
    peremoga = tb.types.KeyboardButton('Peremoga')
    markup.row(petrykivka, peremoga)
    # for command in bases:
    #     markup.add(tb.types.KeyboardButton(command))
    #     markup.row(command)
    bot.send_message(message.chat.id, "*Choose a base:*", reply_markup=markup, parse_mode='markdown')
    bot.register_next_step_handler(message, exchange)


def exchange(message):
    bot.send_message(message.chat.id, "Exchange run, wait for complete...", reply_markup=tb.types.ReplyKeyboardRemove())
    result = e.exchangeRun(message.text)
    bot.send_message(message.chat.id, result)


@bot.message_handler(commands=['getusererp'])
def getUserERP(message):
    user_adin_s = connect.get_people_by_telegram_id(message.chat.id)
    bot.send_message(message.chat.id, f'You are {user_adin_s}')
