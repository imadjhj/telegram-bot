from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from keep_alive import keep_alive

def start(update, context):
    update.message.reply_text("✅ البوت شغال 24/7 على Render!")

import os
TOKEN = os.getenv("TOKEN")
keep_alive()

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
