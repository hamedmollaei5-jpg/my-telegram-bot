import telebot
import time

TOKEN = "8761796906:AAEWLFMWSMEBYaBu-GPAiMCeBoDKAW8MN7Y"
OWNER_ID = 8268872728

bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        user = message.from_user
        text = message.text or ""

        # ارسال پیام کاربر به صاحب ربات
        bot.send_message(
            OWNER_ID,
            f"📨 پیام جدید\n\nاز: {user.first_name} (@{user.username})\nآیدی: {user.id}\n\nمتن:\n{text}"
        )

        reply = "پیامت رو دریافت کردم.\nبه زودی به هوش مصنوعی بدون محدودیت وصل می‌شم."

        bot.reply_to(message, reply)

        bot.send_message(
            OWNER_ID,
            f"🤖 جواب ربات به {user.first_name}:\n{reply}"
        )
    except Exception as e:
        print("خطا در پردازش پیام:", e)

print("ربات با موفقیت روشن شد...")

while True:
    try:
        bot.infinity_polling(timeout=60, long_polling_timeout=60)
    except Exception as e:
        print("خطا در اتصال، ۵ ثانیه بعد دوباره تلاش می‌کنم...", e)
        time.sleep(5)
        
