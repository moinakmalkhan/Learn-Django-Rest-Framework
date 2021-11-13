from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework import authentication
from .custom_permission import MyPermission
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes  = [MyPermission]
    


