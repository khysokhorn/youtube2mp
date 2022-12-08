import os
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import telegram
import asyncio

from main import *


updater = Updater("5537216470:AAHGsiOsdIaxvsu6GaBVfbaXLu10lgwVnTs",
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome to the Bot.Please write\
        /help to see the commands available.")


def youtube2mp3(update: Update, context: CallbackContext):
    url = update.message.text
    update.message.reply_text(
        "We preparing to download this video and convert it into mp3.\nPlese give us a second.")
    chat_id = update.message.chat_id
    updater.bot.send_chat_action(
        chat_id, telegram.ChatAction.UPLOAD_DOCUMENT)
    file_name, title, des = youtube2m3download(url, is_remove=False)
    print("File name ", file_name)
    if len(file_name) != 0:
        update.message.reply_text(
            "We sending this mp3 to you right now ✅.😙")
        updater.bot.send_chat_action(
            chat_id, telegram.ChatAction.UPLOAD_DOCUMENT)
        updater.bot.send_document(
            chat_id, open(file_name, 'rb'), timeout=60000, caption=title)
        os.remove(file_name)
    print(url)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text, youtube2mp3))
print(updater.bot.getMe())
updater.start_polling()
