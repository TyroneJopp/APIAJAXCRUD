from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view      #import function based views formula
from rest_framework.response import Response
from .serializers import TaskSerializer

from .models import Task

# Create your views here.


@api_view(['GET'])                                  #@api decorator passed in the GET request         
def apiOverview(request):                           #apiOverview function used in the passed request
    api_urls = {                                    #api_urls variable defined in JSON format
        'List':'/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',

    }

    return Response(api_urls)                       #the return of that function with the response of the api_urls variable

@api_view(['GET'])                                  #api_view decorator passed the request verb GET
def taskList(request):                  
    tasks = Task.objects.all().order_by('-id')                     #tasks variable calls on the task class to return task objects
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)

@api_view(['GET'])                                  #api_view decorator passed the request verb GET
def taskDetail(request, pk):                        
    tasks = Task.objects.get(id=pk)                 #tasks variable calls on the task class to return task object that match task id
    serializer = TaskSerializer(tasks, many=False)  #which then get passed to serializer
    return Response(serializer.data)                #return response with the serializer data

@api_view(['POST'])                                 #api_view decorator passed the request verb POST
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)   #This is posting to the serializers through the request.data

    if serializer.is_valid():                        #Checks if the it is valid
        serializer.save()                            #If it is valid save the file


    return Response(serializer.data)                #Respond with the entered data 

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()


    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()

    return Response("Item sucessfuly deleted!")