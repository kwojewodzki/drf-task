from rest_framework.permissions import BasePermission


class CanGetExpiringLink(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser or (
                    request.user.is_authenticated and request.user.tier.is_expiring_link)
