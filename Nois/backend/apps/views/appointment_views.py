from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from ..models import Appointment
from ..serializers import AppointmentSerializer
from ..permissions import IsClient, IsProfessional, IsAdmin, IsAppointmentParticipantOrAdmin

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'slug'

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAdmin]
        elif self.action == 'create':
            permission_classes = [IsClient | IsAdmin]
        elif self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAppointmentParticipantOrAdmin]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        if request.user.role == 'ADMIN':
            return super().list(request, *args, **kwargs)
        return Response(
            {"detail": "You do not have permission to perform this action."},
            status=status.HTTP_403_FORBIDDEN
            )

    def create(self, request, *args, **kwargs):
        if request.user.role in ['CLIENT', 'ADMIN']:
            return super().create(request, *args, **kwargs)
        return Response({
            "detail": "You do not have permission to perform this action."},
            status=status.HTTP_403_FORBIDDEN
            )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.role == 'ADMIN':
            return super().update(request, *args, **kwargs)
        elif request.user.role in ['CLIENT', 'PROFESSIONAL']:
            allowed_fields = [
                'start',
                'end',
                'description',
                'appntmnt_status',
                'appntmnt_location',
                'custom_location'
                ]

            update_data = {k: v for k, v in request.data.items() if k in allowed_fields}
            if not update_data:
                return Response(
                    {"detail": "No valid fields to update."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            for key, value in update_data.items():
                setattr(instance, key, value)

            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

        return Response(
            {"detail": "You do not have permission to perform this action."},
            status=status.HTTP_403_FORBIDDEN
        )

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.role == 'ADMIN':
            return super().destroy(request, *args, **kwargs)
        elif request.user.role in ['CLIENT', 'PROFESSIONAL']:
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

