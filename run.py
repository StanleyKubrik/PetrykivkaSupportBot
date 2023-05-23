from bot.telegram_bot import *
from models.appeals.processed_messages import *
from models.base import *


if __name__ == '__main__':
    bot.polling()

    # print(get_new_msgs_by_user(28))
