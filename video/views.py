from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video
from .serializers import VideoSerializer
from django.http import Http404

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

class DetailVideo(APIView):

    def get_object(self, pk):
        try:
            return Video.objects.get(pk=pk)
        except Video.DoesNotExist as e:
            raise Http404

    # getting one video
    def get(self, request, pk):
        video = self.get_object(pk)
        video_json = VideoSerializer(video)
        return Response(video_json.data)

    # updating one video
    def put(self, request, pk):
        video = self.get_object(pk)
        video_json = VideoSerializer(video, data=request.data)
        if video_json.is_valid():
            video_json.save()
            return Response(video_json.data)
        return Response(video_json.errors, status = 400)

    # delete a video
    def delete(self, request, pk):
        video = self.get_object(pk)
        video.delete()
        return Response('',status=204)
