# your_app/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from .models import Media 

@receiver(post_save, sender=Media)
def update_media_url(sender, instance, **kwargs):
    try:
        # Update the URL to use 'https' instead of 'http'
        instance.media_data = instance.media_data.replace('http://', 'https://')
        instance.save()
    except ObjectDoesNotExist:
        # Handle the case where the Media object does not exist
        pass
