from django.http import Http404
from rest_framework import viewsets, permissions
from ..models import Service
from ..serializers import ServiceSerializer
from ..permissions import IsAdmin, IsProfessional


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsProfessional | IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def queryset(self):
        professional_slug = self.kwargs.get('slug')
        return Service.objects.filter(professionals__slug=professional_slug)

    def get_object(self):
        professional_slug = self.kwargs.get('slug')
        service_slug = self.kwargs.get('service_slug')
        try:
            return Service.objects.get(professionals__slug=professional_slug, slug=service_slug)
        except Service.DoesNotExist:
            raise Http404("No Service matches the given query.")

    def perform_create(self, serializer):
        professional = self.request.user.professional
        serializer.save(professionals=[professional])
