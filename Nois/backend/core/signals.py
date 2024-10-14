from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .email_handler import send_account_activation_email

User = get_user_model()

@receiver(post_save, sender=User)
def send_confirmation_email(sender, instance, created, **kwargs):
    if created:
        send_account_activation_email(instance)
