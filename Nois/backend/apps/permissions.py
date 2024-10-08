from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'CLIENT'

class IsProfessional(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'PROFESSIONAL'

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'ADMIN'

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or request.user.role == 'ADMIN':
            return True
        return obj.slug == request.user.slug
