from telegram.ext import Updater, CommandHandler
from config.settings import TOKEN
from handlers.join_group import join_group

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    join_handler = CommandHandler('join', join_group)
    dispatcher.add_handler(join_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
