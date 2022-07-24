from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.

class VideoUpload(models.Model):
    file = models.FileField(null=True, 
                           blank=True, 
                           validators=[FileExtensionValidator( ['mp4','mkv'] ) ])
    name=models.CharField(max_length=100,null=True, blank=True)
    size=models.FloatField(null=True, blank=True)
    duration=models.FloatField(null=True,blank=True)
    type=models.CharField(max_length=40,null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.file}!!"
        



