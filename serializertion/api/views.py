from django.http.response import JsonResponse
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
def student_detail(request,pk):
    stu=Student.objects.filter(pk=pk)
    serializer = StudentSerializer(stu,many=True)
    jsondata = JSONRenderer().render(serializer.data)
    return HttpResponse(jsondata,content_type='application/json') 
def student_list(request):
    stu=Student.objects.all()
    serializer = StudentSerializer(stu,many=True)
    jsondata = JSONRenderer().render(serializer.data)
    return HttpResponse(jsondata,content_type='application/json')    
    
