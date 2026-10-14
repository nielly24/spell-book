from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
  from rest_framework.permissions import BasePermission

from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role.name == 'admin'