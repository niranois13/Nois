from rest_framework import viewsets, permissions
from ..models import Availability
from ..serializers import AvailabilitySerializer
from ..permissions import IsOwnerOrAdmin, IsAdmin, IsProfessional, IsClient

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdmin]
        elif self.action == 'create':
            permission_classes = [IsProfessional | IsAdmin]
        elif self.action == 'retrieve':
            permission_classes = [ IsClient | IsOwnerOrAdmin]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]


