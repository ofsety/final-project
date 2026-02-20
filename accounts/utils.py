import requests
from ipware import get_client_ip
import telebot
from django.conf import settings


bot = telebot.TeleBot(settings.TOKEN)


def detect_region(request):
    ip, _ = get_client_ip(request)

    if not ip:
        return "en-US"

    try:
        r = requests.get(f"https://ipapi.co/{ip}/json/")
        data = r.json()

        country = data.get("country_code", "US")

        return f"{country.lower()}-{country.upper()}"

    except:
        return "en-US"
    

def send_telegram(chat_id, text):
    bot.send_message(chat_id, text)