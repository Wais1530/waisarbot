import telebot

# توکن رباتت
TOKEN = "8483349496:AAFnIRt6X_3M2B5l3uxvJM6IxxKVZw277mE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام 🌹 به ربات درآمدزایی خوش آمدی!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "🎁 هدیه (دعوت دوستان)":
        bot.reply_to(message, "دوستاتو دعوت کن و VIP رایگان بگیر 🎁")
    elif message.text == "📢 تبلیغات":
        bot.reply_to(message, "اینجا می‌تونی تبلیغات ببینی یا سفارش بدی 📢")
    elif message.text == "⭐ خرید VIP":
        bot.reply_to(message, "برای VIP شدن باید پرداخت کنی.\nلینک پرداخت: https://example.com/pay")
    elif message.text == "📂 فایل‌های رایگان":
        bot.reply_to(message, "اینجا فایل‌های رایگان رو دریافت کن 📂")
    elif message.text == "💬 پشتیبانی":
        bot.reply_to(message, "برای پشتیبانی به ادمین پیام بده 💬")
    else:
        bot.reply_to(message, "گزینه نامعتبر ❌")

print("ربات روشن شد ✅")
bot.polling()
