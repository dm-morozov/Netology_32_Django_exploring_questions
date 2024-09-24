from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            # GET, HEAD, OPTIONS
            return True
        # POST, PUT, PATCH, DELETE
        return obj.author == request.user
