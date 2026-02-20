from django.urls import path
from .views import  tracking_price, history,register, login_view, home, logout_view, StockXPriceDeleteView
urlpatterns = [
    path("", home, name="home"),
    path("tracking_price/", tracking_price, name="tracking_price"),
    path("history/", history, name="history"),
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("delete/stockx_price/<int:pk>", StockXPriceDeleteView.as_view(), name="stockx-price-delete"),
    path("logout/", logout_view, name="logout"),
]