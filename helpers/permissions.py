from rest_framework import permissions

class IsAuthorOrReadyOnly(permissions.BasePermission):
    """
        Adds permission so only author can modify
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user