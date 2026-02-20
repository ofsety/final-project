from django.db import models
from django.contrib.auth.models import User

class StockXPrice(models.Model):
    price = models.CharField(max_length=10000)
    size = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)
    url = models.URLField()

    def __str__(self):
        return f"{self.size} - {self.price}"