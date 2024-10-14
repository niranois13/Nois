from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils import timezone
from datetime import timedelta
from .utils import send_email


def send_account_activation_email(user):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = default_token_generator.make_token(user)

    activation_link = f"{settings.BACKEND_URL}/api/activate/{uid}/{token}/"

    subject = 'Activate your account'
    html_content = f"""
    <p>Hi {user.username},</p>
    <p>Please click the link below to activate your account:</p>
    <a href="{activation_link}">Activate Account</a>
    <p>This link will expire in 24 hours.</p>
    """

    send_email(user.email, subject, html_content)


def send_password_reset_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    reset_link = reverse('password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
    full_reset_link = f"{request.scheme}://{request.get_host()}{reset_link}"

    subject = "Réinitialisation de votre mot de passe"
    html_content = render_to_string('emails/password_reset_email.html', {
        'user': user,
        'reset_link': full_reset_link,
    })

    send_email(user.email, subject, html_content)
