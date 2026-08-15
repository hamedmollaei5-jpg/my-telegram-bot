import telebot

TOKEN = "8761796906:AAEWLFMWSMEBYaBu-GPAiMCeBoDKAW8MN7Y"
OWNER_ID = 8268872728

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user = message.from_user
    text = message.text or ""

    # ارسال پیام کاربر به صاحب ربات
    try:
        bot.send_message(
            OWNER_ID,
            f"📨 پیام جدید\n\nاز: {user.first_name} (@{user.username})\nآیدی: {user.id}\n\nمتن:\n{text}"
        )
    except:
        pass

    # جواب تستی (بعداً به هوش مصنوعی وصل می‌کنیم)
    reply = "پیامت رو دریافت کردم.\nبه زودی به هوش مصنوعی بدون محدودیت وصل می‌شم."

    bot.reply_to(message, reply)

    # ارسال جواب ربات به صاحب ربات
    try:
        bot.send_message(
            OWNER_ID,
            f"🤖 جواب ربات به {user.first_name}:\n{reply}"
        )
    except:
        pass

print("ربات با موفقیت روشن شد...")
bot.infinity_polling()
