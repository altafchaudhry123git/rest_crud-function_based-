from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from myapp.serializer import StudentSerializer
from .models import *
# Create your views here.

@api_view(['GET'])
def home(request):
    return Response('This is home page')

@api_view(['GET'])
def data(request):
    records=Student.objects.all()
    serializer=StudentSerializer(records, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def sdata(request, id):
    record=Student.objects.get(id=id)
    serializer=StudentSerializer(record, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializers=StudentSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
        return Response(serializers.data)

# @api_view(['PATCH'])  #partial update
@api_view(['PUT'])    #fully update
def UpdateData(request, id):
    record=Student.objects.get(id=id)
    serializer=StudentSerializer(instance=record, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

@api_view(['DELETE'])
def DeleteData(request, id):
    data=Student.objects.get(id=id)
    data.delete()
    return Response('DELETED')