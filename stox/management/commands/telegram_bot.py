import os
import django
import sys
import uuid
import re

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")
django.setup()

import telebot
from stox.Playwright_file import get_stockx_price
from django.contrib.auth.models import User
from accounts.models import Profile
from django.conf import settings

TOKEN = "7940393197:AAElyiaIfDBNjU3J6R8sWQ71GiC2H4ZhYVw"

bot = telebot.TeleBot(TOKEN)
user_states = {}

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Запуск Telegram бота'

    def handle(self, *args, **kwargs):
        bot.polling(none_stop=True)
    @bot.message_handler(commands=['link'])
    def link_account(message):

        raw_token = message.text.replace('/link', '', 1)

    
        token = re.sub(r'\s+', '', raw_token)
        token = re.sub(r'-', '', token)
        

        print("RAW:", raw_token)
        print("CLEAN:", token)

        try:
            token = uuid.UUID(token)
        except ValueError:
            bot.send_message(message.chat.id, "Токен пошкодженно при копіюванні!")
            return

        try:
            profile = Profile.objects.get(telegram_token=token)

            profile.telegram_chat_id = message.chat.id
            profile.save()

            bot.send_message(message.chat.id, "Telegram підключен!")

        except Profile.DoesNotExist:
            bot.send_message(message.chat.id, "Токен не знайден")


    @bot.message_handler(func=lambda m: m.text.startswith("http"))
    def get_url(message):
        user_states[message.chat.id] = {"url": message.text}

        bot.send_message(
            message.chat.id,
            "Тепер введи розмір (наприклад 42)"
        )

    @bot.message_handler(func=lambda m: m.chat.id in user_states and not m.text.startswith("/"))
    def get_size(message):
        size = message.text
        url = user_states[message.chat.id]["url"]

        bot.send_message(message.chat.id, "Шукаю ціну...")

        try:
            price = get_stockx_price(url, size)

            bot.send_message(
                message.chat.id,
                f"Ціна для розміру {size}:\n\n{price}"
            )

        except Exception as e:
            bot.send_message(message.chat.id, f"Помилка: {e}")

        user_states.pop(message.chat.id, None)

    @bot.message_handler(func=lambda m: True)
    def debug(message):
        print("MESSAGE:", message.text)


    print("Bot started")
    bot.remove_webhook()
    bot.infinity_polling()