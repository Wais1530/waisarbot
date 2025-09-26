import telebot

# توکن ربات
TOKEN = "8483349496:AAFnIRt6X_3M2B5l3uxvJM6IxxKVZw277mE"
bot = telebot.TeleBot(TOKEN)

# وقتی کسی استارت بزنه
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام ✋ به ربات ویسار جان خوش آمدی 🌹")

# وقتی کسی متن بفرسته
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"تو نوشتی: {message.text}")

# اجرای ربات
if __name__ == "__main__":
    bot.polling(none_stop=True)
