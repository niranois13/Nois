from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken


class LogoutView(APIView):
    def post(self, request):
        try:
            refresh_token = request.COOKIES.get(settings.JWT_AUTH_REFRESH_COOKIE)
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            pass

        response = Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)
        response.delete_cookie(settings.JWT_AUTH_COOKIE)
        response.delete_cookie(settings.JWT_AUTH_REFRESH_COOKIE)

        return response
