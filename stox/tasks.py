from celery import shared_task
from .models import StockXPrice
from .Playwright_file import get_stockx_price
from final_project.accounts.utils import send_telegram
from telegram_bot import bot
from accounts.models import Profile


@shared_task
def update_prices():
    items=StockXPrice.objects.filter(user__profile__telegram_chat_id__isnull=False)


    for item in items:
        new_price = get_stockx_price(
            item.url,
            item.size,
            #region=item.region
        )

        item.price = new_price
        item.save()

        if item.user.profile.telegram_chat_id:
                send_telegram(
                    item.user.profile.telegram_chat_id,
                    f"Нова ціна для розміру {item.size} - {new_price}"
                )

    return "Prices updated"