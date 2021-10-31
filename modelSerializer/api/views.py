from django.shortcuts import render
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student
from django.utils.decorators import method_decorator
from django.views import View
@method_decorator(csrf_exempt,name="dispatch")
class StudentApiClassBased(View):
    def get(self,request,*args, **kwargs):
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
        response = JSONRenderer().render(serializer.data)
        return HttpResponse(response,content_type="application/json")
    def post(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pydata)
        if serializer.is_valid():
            serializer.save()
            response = {"msg":"Data has been saved"}
            response = JSONRenderer().render(response)
            return HttpResponse(response,content_type="application/json")
        
        response = JSONRenderer().render(serializer.errors)
        return HttpResponse(response,content_type="application/json")
    def put(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        id = pydata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=pydata,partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {"msg":"Data has been Updated"}
            response = JSONRenderer().render(response)
            return HttpResponse(response,content_type="application/json")
        response = JSONRenderer().render(serializer.errors)
        return HttpResponse(response,content_type="application/json")

    def delete(self,request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        id = pydata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        response = {"msg":"Data has been Deleted"}
        response = JSONRenderer().render(response)
        return HttpResponse(response,content_type="application/json")


@csrf_exempt
def StudentApiFunctionBased(request):
    if request.method=='GET':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
        response = JSONRenderer().render(serializer.data)
        return HttpResponse(response,content_type="application/json")

        # return JsonResponse(serializer.data,safe=False)
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pydata)
        if serializer.is_valid():
            serializer.save()
            response = {"msg":"Data has been saved"}
            response = JSONRenderer().render(response)
            return HttpResponse(response,content_type="application/json")
        response = JSONRenderer().render(serializer.errors)
        return HttpResponse(response,content_type="application/json")
    if request.method=='PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        id = pydata.get('id')
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu,data=pydata,partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {"msg":"Data has been Updated"}
            response = JSONRenderer().render(response)
            return HttpResponse(response,content_type="application/json")
        response = JSONRenderer().render(serializer.errors)
        return HttpResponse(response,content_type="application/json")
    if request.method=='DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        id = pydata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        response = {"msg":"Data has been Deleted"}
        response = JSONRenderer().render(response)
        return HttpResponse(response,content_type="application/json")
            
            