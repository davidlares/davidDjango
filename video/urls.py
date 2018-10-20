# generating endpoints
from django.urls import path
from .views import ListVideo, DetailVideo

urlpatterns = [
    # path('list/', ListVideo.as_view(), name = 'list-video'),
    path('', ListVideo.as_view(), name = 'list-video'),
    path('<int:pk>/', DetailVideo.as_view(), name = 'list-video'), #params
]
