from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer

# Create your views here.
class ListVideo(APIView):
    # video lists (endpoint)
    def get(self, request):
        videos = Video.objects.all()
        video_json = VideoSerializer(videos, many=True) # many Videos
        return Response(video_json.data)

    # creating videos
    def post(self, request):
        video_json = VideoSerializer(data=request.data) # Unmarshall -> video Model
        if video_json.is_valid():
            video_json.save() # Django ORM method
            return Response(video_json.data, status = 201) #
        return Response(video_json.errors, status = 400)
