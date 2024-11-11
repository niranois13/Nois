from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from ..models import User
from ..serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['get_my_slug', 'check_auth_status']:
            return [permissions.IsAuthenticated()]
        else:
            return [permissions.IsAdminUser()]

    @action(detail=False, methods=['GET'])
    def get_my_slug(self, request):
        print("Requête reçue pour get_my_slug")
        print(f"Utilisateur authentifié : {request.user.is_authenticated}")
        print(f"Utilisateur : {request.user}")
        try:
            user = User.objects.get(email=request.user.email)
            print(f"User trouvé : {user}")
            return Response({"slug": user.slug})
        except User.DoesNotExist:
            return Response({"error": "User non trouvé"}, status=404)


    @action(detail=False, methods=['GET'])
    def check_auth_status(self, request):
        if not request.user.is_authenticated:
            return Response({'error': 'User not authenticated'}, status=401)

        user_type = request.user.role

        try:
            user = User.objects.get(email=request.user.email)
            print(f"Utilisateur trouvé : {user}")
            return Response({'isAuthenticated': True, 'slug': user.slug, 'userType': user_type})
        except User.DoesNotExist:
            return Response({"error": "Utilisateur non trouvé"}, status=404)
