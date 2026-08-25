import os
import telebot
import requests

TOKEN = os.environ.get("BOT_TOKEN")
ADMIN_ID_STR = os.environ.get("ADMIN_CHAT_ID")
APPS_SCRIPT_URL = os.environ.get("APPS_SCRIPT_URL")

# Əgər dəyişənlərdən biri əksikdirsə, səbəbi açıq göstərsin
if not TOKEN or not ADMIN_ID_STR or not APPS_SCRIPT_URL:
    print("XƏTA: Environment variables (BOT_TOKEN, ADMIN_CHAT_ID və ya APPS_SCRIPT_URL) tam təyin olunmayıb!")
    exit(1)

ADMIN_ID = int(ADMIN_ID_STR)
bot = telebot.TeleBot(TOKEN)

# Qalan bot funksiyaları...
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salam! BazarStare çəkiliş botuna xoş gəlmisiniz.")

print("Bot uğurla işə düşdü, dinlənilir...")
bot.infinity_polling()
