from rest_framework import viewsets, permissions
from ..permissions import IsProfessional
from ..models import Service, ProfessionalService
from ..serializers import ServiceSerializer, ProfessionalServiceSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(is_verified=True)
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(is_verified=False)


class ProfessionalServiceViewSet(viewsets.ModelViewSet):
    queryset = ProfessionalService.objects.all()
    serializer_class = ProfessionalServiceSerializer
    permission_classes = [IsProfessional]

    def perform_create(self, serializer):
        professional = self.request.user.professional
        serializer.save(professional=professional)
