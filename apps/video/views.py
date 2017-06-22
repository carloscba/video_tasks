from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from serializers import VideoSerializer
from models import Video

from moviepy.editor import *

@csrf_exempt

def video_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        clip = VideoFileClip("video1.mp4").subclip(0,8)
        
        video = CompositeVideoClip([clip])
        video.write_videofile("result.mp4")

        print(clip)
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VideoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

def video_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        video = Video.objects.get(pk=pk)
    except Video.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VideoSerializer(video)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VideoSerializer(video, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        video.delete()
        return HttpResponse(status=204)

