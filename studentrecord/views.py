from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import sys
#from django.http import JsonResponse

from .serializers import StudentrecordsSerializer
from .models import Studentrecord

@api_view(['GET'])
def apiInfo(request):
    api_urls = {
        'View':'/student-records/view-all/',
        'Create':'/student-records/view/<str:rollno>',
        'Update':'/student-records/update/<str:pk>',
        'Delete':'/student-records/delete/<str:pk>',
    } 
    return Response(api_urls)


@api_view(['GET'])
def viewallrecords(request):
    students = Studentrecord.objects.all().order_by('-Percentage')
    serializer = StudentrecordsSerializer(students, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def viewStudentrecord(request, rollno):
    students = Studentrecord.objects.get(RollNo=rollno)
    serializer = StudentrecordsSerializer(students, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def viewsortbystudentrecord(request, field):
    students = Studentrecord.objects.all().order_by(field)
    serializer = StudentrecordsSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createnewrecord(request):
    serializer = StudentrecordsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        error={"Error":"NOT VALID"}
        return Response(error)

@api_view(['POST'])
def updatestudentrecord(request, pk):
    record = Studentrecord.objects.get(Id=pk)
    serializer = StudentrecordsSerializer(instance=record, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        error={"Error":"Some Error Occurred"}
        return Response(error)

@api_view(['POST'])
def deletestudentrecord(request, pk):
    obj = Studentrecord.objects.get(Id=pk)
    obj.delete()
    return Response('Item succsesfully delete!')