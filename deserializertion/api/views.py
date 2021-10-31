from django.shortcuts import render
import io
from .serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def create_student(request):
    if request.method=='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        print(stream)
        pydata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pydata)
        if serializer.is_valid():
            serializer.save()
            response = {"msg":"Data has been saved"}
            response = JSONRenderer().render(response)
            return HttpResponse(response,content_type="application/json")
        
        response = JSONRenderer().render(serializer.errors)
        return HttpResponse(response,content_type="application/json")
            
            