from rest_framework import viewsets, permissions
from ..permissions import IsProfessional, IsAdmin, IsOwnerOrAdmin
from ..models import Service, ProfessionalService
from ..serializers import ServiceSerializer, ProfessionalServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(is_verified=True)
    serializer_class = ServiceSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        elif self.action == 'create':
            permission_classes = [IsProfessional | IsAdmin]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(is_verified=False)


class ProfessionalServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ProfessionalServiceSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsProfessional]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        professional = self.request.user.professional
        serializer.save(professional=professional)

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return ProfessionalService.objects.all()
        return ProfessionalService.objects.filter(professional=self.request.user.professional)
