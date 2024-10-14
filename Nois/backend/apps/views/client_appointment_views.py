from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import Appointment, Client
from ..serializers import AppointmentSerializer
from ..permissions import IsOwnerOrAdmin
from django.shortcuts import get_object_or_404

class ClientAppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsOwnerOrAdmin]
    lookup_field = 'slug'
    lookup_url_kwarg = 'appointment_slug'

    def get_queryset(self):
        client_slug = self.kwargs.get('slug')
        client = get_object_or_404(Client, slug=client_slug)
        return Appointment.objects.filter(client=client)

    def perform_create(self, serializer):
        client_slug = self.kwargs.get('slug')
        client = get_object_or_404(Client, slug=client_slug)
        serializer.save(client=client)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.role == 'ADMIN':
            return super().destroy(request, *args, **kwargs)
        elif request.user.role == 'CLIENT':
            instance.appntmnt_status = 'CANCELED'
            instance.save()
            return Response(
                {"detail": "Appointment has been canceled."},
                status=status.HTTP_200_OK
                )
        return Response(
            {"detail": "You do not have permission to perform this action."},
            status=status.HTTP_403_FORBIDDEN
            )


