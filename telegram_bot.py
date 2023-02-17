import exchange as e
import telebot

API_KEY = '6060675197:AAEzZB1pKlZ0Tw26l9zZupgn5Nbbf9TK4dc'
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Hello, bitch! What do you want?')


@bot.message_handler(commands=['exchange'])
def runExchangePetrykivka(message):
    base = message.text.split()[1]
    result = e.exchangeRun(base)
    bot.send_message(message.chat.id, result)


bot.polling()
