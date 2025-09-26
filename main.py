import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# -----------------
TOKEN = "8483349496:AAFnIRt6X_3M2B5l3uxvJM6IxxKVZw277mE"
ADMIN_ID = 1774596878
# -----------------

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def start(update, context):
    user = update.effective_user
    update.message.reply_text(
        f"سلام {user.first_name} 🌹\n"
        f"به ربات ویسار خوش آمدی 🤖\n\n"
        "اینجا میتونی:\n"
        "- اطلاعات VIP بگیری 💎\n"
        "- فایل و آموزش بخری 📂\n"
        "- لینک یوتیوب ببینی 🎥"
    )

def echo(update, context):
    update.message.reply_text(f"📩 گفتی: {update.message.text}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
