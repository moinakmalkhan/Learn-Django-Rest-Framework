from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
# to create token type python manage.py drf_create_token <username>
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes  = [permissions.IsAdminUser]
    
class CustomAuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user':{
                'id':user.id,
                'email':user.email,
                'first_name':user.first_name,
                'last_name':user.last_name,
                },
            })
    


