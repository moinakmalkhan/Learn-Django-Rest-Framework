from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework import authentication
from rest_framework import permissions

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [authentication.SessionAuthentication]
    # permission_classes  = [permissions.AllowAny]
    # permission_classes  = [permissions.IsAuthenticated]
    # permission_classes  = [permissions.IsAdminUser]
    # permission_classes  = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes  = [permissions.DjangoModelPermissions]
    permission_classes  = [permissions.DjangoModelPermissionsOrAnonReadOnly]


