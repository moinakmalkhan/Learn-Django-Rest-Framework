from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User
class MyAuth(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get("username",None)
        if username is None:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise AuthenticationFailed("User not found",404)
        return user,None
