from rest_framework import permissions
from user_token.views import TokenValidation


class IsOwnerOrIsAdminOrHasToken(permissions.BasePermission):
    def has_permission(self, request, view):
        token = request.META.get("HTTP_DETECTIVE_TOKEN")
        is_token_valid = bool(TokenValidation.check_token(token))
        return (
            is_token_valid | request.user.is_superuser | request.user.is_authenticated
        )
