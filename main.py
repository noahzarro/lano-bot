import json
from telegram.ext import Updater, MessageHandler, Filters

with open('token.json', 'r') as token_file:
    token_dict = json.load(token_file)


updater = Updater(token=token_dict["token"])
dispatcher = updater.dispatcher


def message_handler(bot, update):
    message = update.message.text.lower().split()
    if "lano" in message:
        bot.send_message(chat_id=update.message.chat_id, text="Was für ein schöner Name!")

    if "scio" in message:
        bot.send_sticker(chat_id=update.message.chat_id, sticker=open('photos/scio_scooter.gif', 'rb'))
        bot.send_message(chat_id=update.message.chat_id, text="Do isch de grüsig cheib")


dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
updater.start_polling()
