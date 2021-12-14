# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
import logging

from bot.bot_settings import BOT_API_TOKEN
from user_messages.models import Chat

updater = Updater(token=BOT_API_TOKEN)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Please send your token here. URL: ')


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def receive_token(update: Update, context: CallbackContext):
    token = update.message.text
    user = User.objects.filter(auth_token=token).first()
    if user:
        chat = Chat()
        chat.chatid = update.effective_chat.id
        chat.user = user
        try:
            chat.save()
        except Exception as e:
            logging.exception(e)
        context.bot.send_message(chat_id=update.effective_chat.id, text='your token was saved')
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text='user with the provided token does not exist')
        logging.warning('user with the provided token does not exist')


token_handler = MessageHandler(Filters.text & (~Filters.command), receive_token)
dispatcher.add_handler(token_handler)

updater.start_polling()
