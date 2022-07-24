from rest_framework import serializers
from .models import *
from django.conf import settings


class ChargeOnVideoSerializer(serializers.ModelSerializer):
    type=serializers.CharField(max_length=40)
    size=serializers.IntegerField(max_value=1024, min_value=1)  # size of video is asssume as MB
    length=serializers.DecimalField(max_value=10,max_digits=2,decimal_places=1)
    class Meta:
        fields=['type','size','length']

class VideoUploadGetSerializer(serializers.ModelSerializer):
    class Meta:
        model=VideoUpload
        fields="__all__"
       
