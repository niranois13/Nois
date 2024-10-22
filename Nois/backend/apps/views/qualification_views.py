from rest_framework import viewsets, permissions
from ..models import Qualification
from ..serializers import QualificationSerializer
from ..permissions import IsAdmin, IsProfessional, IsOwnerOrAdmin

class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action == 'list':
            permissions_classes = [permissions.AllowAny]
        elif self.action == 'create':
            permissions_classes = [IsProfessional | IsAdmin]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions_classes = [IsOwnerOrAdmin]
        else:
            permissions_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permissions_classes]
