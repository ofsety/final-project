from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import StockXPrice

User = get_user_model