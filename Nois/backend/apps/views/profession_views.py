from rest_framework import viewsets, permissions
from rest_framework.permissions import *
from ..models import Profession, Professional
from rest_framework.exceptions import PermissionDenied
from ..serializers import ProfessionSerializer
from ..permissions import IsProfessional, IsOwnerOrAdmin, IsAdmin

class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action == 'list' or self.action == 'create':
            permission_classes = [permissions.AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(proposed_by=self.request.user, approved=False)

    def get_queryset(self):
        professional_slug = self.kwargs.get('slug')
        if professional_slug:
            professional = Professional.objects.get(slug=professional_slug)
            if professional.profession == None:
                return "This professional has no profession"
            return professional.profession.all()
        elif self.request.user.is_staff or self.request.user.role == 'ADMIN':
            return Profession.objects.all()
        return Profession.objects.filter(approved=True)
