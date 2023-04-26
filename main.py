from bot import tg_bot
from bot import telegram_bot


if __name__ == '__main__':
    telegram_bot.bot.polling()

    # roles = {
    #     '329518676': 'support',
    #     '327444916': 'user'
    # }
    # COMMANDS = {
    #     'support': ['Start',
    #                 'Exchange 1C7-SQL'
    #                 ],
    #     'user': ['Dick']
    # }
    #
    # print(roles.get('327444916'))
    # print(COMMANDS.get('user'))
