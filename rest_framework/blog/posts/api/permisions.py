from rest_framework.permissions import BasePermission


# Asi todos pueden leer pero solo los admins editar
class isAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        else:
            return request.user.is_staff         