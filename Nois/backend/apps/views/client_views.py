from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from ..models import Client
from ..serializers import ClientSerializer
from ..permissions import IsOwnerOrAdmin


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdminUser]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrAdmin]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

'''
class ClientRegistrationView(APIView):
    @transaction.atomic
    def post(self, request):
        serializer = ClientRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            client = serializer.save()
            return Response({
                'message': 'Client enregistré avec succes',
                'client_id': client.id
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientListView(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientListSerializer(clients, many=True)
        return Response(serializer.data)

class UserUpdateView(generics.UpdateAPIView):
    serializer_class = ClientUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdmin]

    def get_object(self):
        return self.request.user
'''
