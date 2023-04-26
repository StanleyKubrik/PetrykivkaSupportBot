import telebot as tb

API_KEY = '6060675197:AAEzZB1pKlZ0Tw26l9zZupgn5Nbbf9TK4dc'


class Bot(tb.TeleBot):
    def __int__(self, api_key):
        self.token = api_key

    def start(self, message):
        bot.send_message(message.chat.id, f'Hello, bitch! What do you want?')


bot = Bot(API_KEY)
