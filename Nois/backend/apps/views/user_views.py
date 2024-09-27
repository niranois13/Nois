from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from ..models import User
from ..serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

'''
class UserListView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        users = User.objects.all()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

class UserUpdateView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_object(self):
        return self.request.user

class AdminUserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = AdminUserUpdateSerializer
    permission_clsses = [IsAdminUser]
'''
