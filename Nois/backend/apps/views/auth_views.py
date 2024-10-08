from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from django.conf import settings

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        tokens = serializer.validated_data

        response = Response(tokens, status=200)
        response.set_cookie(
            key=settings.JWT_AUTH_COOKIE,
            value=tokens['access'],
            httponly=True,
            secure=settings.SECURE_COOKIE,
            samesite='lax',
            max_age=settings.JWT_COOKIE_LIFETIME.total_seconds()
        )
        return response