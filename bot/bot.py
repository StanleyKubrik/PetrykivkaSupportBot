import telebot as tb


class Bot(tb.TeleBot):
    def __int__(self, api_key):
        self.api_key = api_key

