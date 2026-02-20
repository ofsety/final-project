from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=10, default="en-US")
    telegram_chat_id = models.BigIntegerField(null=True, blank=True)
    telegram_token = models.UUIDField(default=uuid.uuid4,editable=False, null=True, unique=True)

    def __str__(self):
        return (self.user)