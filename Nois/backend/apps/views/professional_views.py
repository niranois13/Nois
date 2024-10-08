from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from ..models import Professional, ProfessionalAddress
from ..serializers import ProfessionalSerializer
from ..serializers.address_serializers import ProfessionalAddressSerializer
from ..permissions import IsOwnerOrAdmin


class ProfessionalViewSet(viewsets.ModelViewSet):
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.IsAdminUser()]
        elif self.action in [
            'retrieve', 'update', 'partial_update', 'destroy'
            ]:
            return [IsOwnerOrAdmin()]
        return [permissions.AllowAny()]

    def get_object(self):
        slug = self.kwargs.get('slug')
        return Professional.objects.get(slug=slug)

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class ProfessionalAddressViewSet(viewsets.ModelViewSet):
    queryset = ProfessionalAddress.objects.all()
    serializer_class = ProfessionalAddressSerializer

    def get_permissions(self):
        if self.action in [
            'update', 'partial_update', 'destroy'
            ]:
            return [IsOwnerOrAdmin()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        professional_slug = self.kwargs.get('slug')
        professional = get_object_or_404(
            Professional, slug=professional_slug
            )
        return ProfessionalAddress.objects.filter(
            professional=professional
            )

    def perform_create(self, serializer):
        professional_slug = self.kwargs.get('slug')
        professional = get_object_or_404(
            Professional, slug=professional_slug
            )
        serializer.save(professional=professional)
