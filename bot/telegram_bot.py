import telebot as tb
from config.config import *
from models.people.users import *
from models.command_permissions import *

APP_CONFIG_PATH = './config/config.ini'
app_config = Config(APP_CONFIG_PATH)
bot = tb.TeleBot(app_config.get_setting('TelegramAPI', 'api_key'))


@bot.message_handler(commands=['start'])
def start(message):
    user_role = get_user_role_by_telegram_id(message.chat.id)
    user_authentication(user_role, message.chat.id)


# @bot.message_handler(func=lambda message: True)
# def echo(message):
#     bot.send_message(message.chat.id, message.text)


def user_authentication(user_role, chat_id):
    """
    Use this method when running a bot to validate user data and to determine user role.

    :param user_role: user role ID.
    :param chat_id: user Telegram chat ID.
    """
    is_user_banned(chat_id)

    if user_role is None:
        bot.send_message(chat_id, u'Не можемо зрозуміти, для чого Ви тут, зверніть до технічної підтримки! 😉')
    elif user_role == 1:
        bot.set_my_commands(generate_command_list(1))
        bot.send_message(chat_id, u'Вітаю, Володаре!')
    elif user_role == 2:
        bot.set_my_commands(generate_command_list(2))
        bot.send_message(chat_id, u'Вітаю в екіпажі, Кулєр!')
        bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEhS_9kZzn2f7zaEm7rank-Du1kjbUFRwACjS0AAkDyIUvYFQve9Itbti8E')
    elif user_role == 3:
        bot.set_my_commands(generate_command_list(3))
        markup = tb.types.ReplyKeyboardMarkup()
        markup.row_width = 1
        markup.resize_keyboard = True
        markup.add(tb.types.KeyboardButton(u'📨 Подати звернення'))
        bot.send_message(chat_id, "Вас вітає бот технічної підтримки ІТ-департамента! 👋"
                                  "\nПодати звернення можна двома способами:"
                                  "\n1️⃣ Опишіть проблему і натисніть кнопку 'Подати звернення'."
                                  "\n2️⃣ Перешліть повідомлення з проблемою (можна декілька повідомлень) у цей чат."
                                  "\nПісля цього натисніть кнопку 'Подати звернення'.",
                         reply_markup=markup)
    else:
        bot.send_message(chat_id, u'Вибачте, але ми з Вами не знайомі! Зверніться до технічної підтримки 😉')


def is_user_banned(user_chat_id):
    """
    The method checks if the user has banned the bot.

    :param user_chat_id: user Telegram chat ID.
    """

    try:
        # Attempt to send a test message to the user
        bot.send_message(user_chat_id, "Checking block status...")
        print("User has not blocked the bot.")
    except tb.apihelper.ApiException as e:
        if e.result.status_code == 403:
            for adm in get_admins_chat_id():
                bot.send_message(adm[0], f'⚠️⚠️⚠️ User {user_chat_id} has blocked the bot!')
            print("User has blocked the bot.")
        else:
            for adm in get_admins_chat_id():
                bot.send_message(adm[0], f'⚠️⚠️⚠️ An error occurred while checking user status!')
            print("An error occurred while checking user status.")
