==ВСТУП==

StockX Price Parcer - це веб додаток за допомогою якого ви можете дізнаватися актуальну ціну товару із ретейл площадки StockX або встановити оповіщання на кожні 2 години через сайт проєкту або telegtam бота.

StockX Price Parcer сам визначає ваш регіон через вашу IP адрессу та шукає справржню ціну вашого розміру у вашому регіоні не вважаючи індивідуальні cookies за допомогою Playwright
та видає результат, історію пошуку з можливістю фільтрування по різним аспектам та данні профілю використовуючи структуру Django.

==БІЛЬШЕ ПРО ЧАСТИНИ ПРОЄКТУ==

📦 StockX Price Tracker

парсингу цін через Playwright

збереження історії цін
отримання сповіщень у Telegram
автоматичної перевірки цін через Celery

ПАРСИНГ ЦІН

Користувач може вставити StockX URL і розмір.

Система автоматичновідкриває сторінку через Playwright,знаходить ціну для конкретного розміру і
зберігає її в базу даних.

ІСТОРІЯ ЦІН

У додатку доступна сторінка Price History, де користувач може:

переглядати історію цін
сортувати ціни
фільтрувати по розміру 
бачити мінімальну та максимальну ціну.

ПРОФІЛЬ КОРИСТУВАЧА

На сторінці профілю відображається:

username
email
регіон
кількість запитів
персональний Telegram token для підключення Telegram-бота


TELEGRAM BOT

Користувач може отримувати ціни прямо у Telegram.

Функціонал бота:

/start

отримання URL товару
введення розміру
повернення актуальної ціни
автоматична перевірка цін

Система використовує Celery + Redis, щоб:

автоматично перевіряти ціни
надсилати повідомлення у Telegram якщо ціна змінилась

==ТЕХНОЛОГІЇ==

Python 3
Django
Playwright
Celery
Redis
Telegram Bot API
Tailwind CSS

==ВСТАНОВЛЕННЯ==

1. Клонувати репозиторій
   
git clone https://github.com/username/stockx-tracker.git
cd stockx-tracker

2. Створити virtual environment
python -m venv venv

Активувати:

Windows - venv\Scripts\activate

Linux / Mac - source venv/bin/activate

3. Встановити залежності
   
pip install -r requirements.txt

4. Встановити Playwright
   
playwright install

5. Міграції бази даних
   
python manage.py makemigrations
python manage.py migrate

6. Запустити сервер
python manage.py runserver

7. Запуск Telegram бота

python telegram_bot.py

8.Запуск Celery

Worker - celery -A src worker -l info

Scheduler - celery -A src beat -l info
