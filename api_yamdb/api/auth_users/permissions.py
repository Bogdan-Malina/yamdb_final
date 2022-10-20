from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    """Permission for superuser and user with admin role"""

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.is_admin
        )
