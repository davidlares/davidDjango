# generating endpoints
from django.urls import path
from .views import ListVideo

urlpatterns = [
    path('list/', ListVideo.as_view(), name = 'list-video'),
]
