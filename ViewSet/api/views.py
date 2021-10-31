from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status
class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk=None):
        if pk is not None:
            stu = Student.objects.get(pk=pk)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
    
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    def update(self,request,pk):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Complete Data updated"})
        return Response({serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    def partial_update(self,request,pk):
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Complete Data updated"})
        return Response({serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,requent,pk):
        stu = Student.objects.get(pk=pk)
        stu.delete()
        return Response({"msg":"Data deleted"})

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
