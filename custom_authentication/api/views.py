from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework import permissions
from .customauth import MyAuth
class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [MyAuth]
    permission_classes  = [permissions.IsAuthenticated]
 