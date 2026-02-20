from django.contrib import admin
from .models import StockXPrice
from django.contrib.auth.models import User

class StockXPriceAdmin(admin.ModelAdmin):
    list_display = ("price", "size", "url", "created_at")

    search_fields = ("price", "size", "url", "user__username")

    list_filter = ("size", "created_at", "user__username")

admin.site.register(StockXPrice,StockXPriceAdmin)