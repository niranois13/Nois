from django.shortcuts import redirect
from django.http import JsonResponse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model

User = get_user_model()

def activate_account(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return JsonResponse({'status': 'fail', 'message': 'Invalid token or user'}, status=400)

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.email_verified = True
        user.save()

        return JsonResponse({'status': 'success', 'message': 'Account activated successfully'})

    return JsonResponse({'status': 'fail', 'message': 'Invalid token or token expired'}, status=400)
