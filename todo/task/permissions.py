from rest_framework import permissions


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only allow authenticated users to access the endpoint
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow authenticated users to access tasks that they own
        return obj.user == request.user
