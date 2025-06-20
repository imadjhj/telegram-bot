from telegram.ext import Updater, CommandHandler
from keep_alive import keep_alive

def start(update, context):
    update.message.reply_text("✅ البوت شغال 24/7 على Render!")

TOKEN = "7690828449:AAEOWQKcU20yxepvdBpw1PWOqkSMDVoTMYE"

keep_alive()

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
updater.start_polling()
updater.idle()
