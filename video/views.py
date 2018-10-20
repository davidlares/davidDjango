from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Video

# Create your views here.
class ListVideo(APIView):
    # video lists (endpoint)
    def get(self, request):
        videos = Video.objects.all()
        return Response(videos)
