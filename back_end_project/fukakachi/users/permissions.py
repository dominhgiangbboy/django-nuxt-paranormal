from rest_framework import permissions

class CustomerAccessPermission(permissions.BasePermission):
    message = 'Adding customers not allowed.'

    def has_permission(self, request, view):
        return request.user and request.user.is_dev