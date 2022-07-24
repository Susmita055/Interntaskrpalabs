from django.urls import path
from .views import *
app_name = "app"

urlpatterns = [
    
    path("upload-video", UploadVideoView.as_view()),
    path("get", GetVideo.as_view()),
    path("get/<int:pk>", GetVideo.as_view()),
    path("charge_on_video", CalculateChargeOfUploadedVideo.as_view()),

]
