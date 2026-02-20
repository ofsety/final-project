from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

from .utils import detect_region


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        region=detect_region
        Profile.objects.create(user=instance,region=region)