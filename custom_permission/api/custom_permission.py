from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Here we add our permission logic 
        return True if we wanna grant permission
        return False if we not wanna grant permission

        """
        # return False
        return True
