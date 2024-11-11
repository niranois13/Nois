from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from ..models import Appointment, Professional
from ..serializers import AppointmentSerializer
from ..permissions import IsOwnerOrAdmin
from django.shortcuts import get_object_or_404

class ProfessionalAppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsOwnerOrAdmin]
    lookup_field = 'slug'
    lookup_url_kwarg = 'appointment_slug'

    def get_queryset(self):
        professional_slug = self.kwargs.get('slug')
        professional = get_object_or_404(Professional, slug=professional_slug)
        return Appointment.objects.filter(professional=professional)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

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
        elif request.user.role == 'PROFESSIONAL':
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


