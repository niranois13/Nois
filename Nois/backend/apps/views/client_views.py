from rest_framework import viewsets, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from ..models import Client, ClientAddress
from ..serializers import ClientSerializer
from ..serializers.address_serializers import ClientAddressSerializer
from ..permissions import IsOwnerOrAdmin


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action == 'list':
            return [permissions.IsAdminUser()]
        elif self.action in [
            'retrieve', 'update', 'partial_update', 'destroy'
            ]:
            return [IsOwnerOrAdmin()]
        elif self.action =='create':
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get(self.lookup_field)
        obj = get_object_or_404(queryset, slug=slug)
        self.check_object_permissions(self.request, obj)
        return obj

    def perform_create(self, serializer):
        return super().perform_create(serializer)

class ClientAddressViewSet(viewsets.ModelViewSet):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return [IsOwnerOrAdmin()]
        return [permissions.IsAuthenticated()]

    def get_queryset(self):
        client_slug = self.kwargs.get('slug')
        client = get_object_or_404(Client, slug=client_slug)
        return ClientAddress.objects.filter(client=client)

    def perform_create(self, serializer):
        client_slug = self.kwargs['slug']
        client = get_object_or_404(Client, slug=client_slug)
        serializer.save(client=client)
