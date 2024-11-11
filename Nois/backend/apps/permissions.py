from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsClient(BasePermission):
    def has_permission(self, request, view):
        """
        Custom permission to only allow authenticated users with the 'CLIENT' role
        to access an endpoint.
        """
        if not request.user.is_authenticated:
            return False
        return request.user.role == 'CLIENT'


class IsProfessional(BasePermission):
    def has_permission(self, request, view):
        """
        Custom permission to only allow authenticated professionals with the 'PROFESSIONAL' role
        to access an endpoint.
        """
        if not request.user.is_authenticated:
            return False
        return request.user.role == 'PROFESSIONAL'


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        """
        Custom permission to only allow authenticated admins with the 'ADMIN' role
        to access an endpoint.
        """
        if not request.user.is_authenticated:
            return False
        return request.user.role == 'ADMIN'


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow the owner or admin to access an endpoint.
    """
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated:
            return False
        if request.user.is_staff or request.user.role == 'ADMIN':
            return True

        return obj.slug == request.user.slug


class IsAppointmentParticipantOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow participants of an appointment (client, professional),
    or admins to edit it.
    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.role == 'ADMIN':
            return True
        elif request.user.is_authenticated and request.user.role == 'CLIENT':
            return obj.appntmnt_link.client == request.user.client
        elif request.user.is_authenticated and request.user.role == 'PROFESSIONAL':
            return obj.appntmnt_link.professional == request.user.professional
        else:
            return False
