from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_anonymous:
            return False

        return (
            obj.author == request.user
            or request.user.role == 'admin'
            or request.user.role == 'moderator'
        )
