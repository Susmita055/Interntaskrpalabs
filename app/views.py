
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from .serializers import *
from moviepy.editor import *

# Create your views here.4


class UploadVideoView(APIView):
    def post(self, request):
        file=request.FILES.get('file',None)
        if not file:
            return Response({'file':'file is not provided to upload'})
        file=request.FILES.get("file",None)
        type = file.content_type.split('/')[0]
        size=file.size/(1024*1024) # video size in mb
        if size>1024:
            return Response({'file_size':'file should be smaller than 1 GB'})
        print(type)
        if type != 'video':
            return Response({'file_type':'file type must be video'})
        VideoUpload.objects.create(file=file)
        files=VideoUpload.objects.last()
        id=files.id
        video = VideoFileClip(settings.MEDIA_ROOT+ files.file.name)
        duration=video.duration/60  # this will return the length of the video in min
        name=files.file.name[:30]
        if duration>10:
            files.delete()
            return Response({"file_duration":"video duration shouldn't exceed 10 min"})
    
        files.name=name
        files.duration=duration
        files.size=size
        files.save()
        return Response({"status_msg":"SuccessFully Uploaded", "status_type":'Success', "status_code":201})    
        

class GetVideo(APIView):
    def get(self, request, pk=None):
        if pk == None:
            data = VideoUpload.objects.all()
            serialized_data=VideoUploadGetSerializer(data,many=True).data
        else:
            data=VideoUpload.objects.get(id=pk)
            serialized_data=VideoUploadGetSerializer(data).data
        return Response({"data":serialized_data, "status_msg":"Data Fetch Sucessfully", "status_type":'Success', "status_code":200})
        
    

class CalculateChargeOfUploadedVideo(APIView):
    def get(self,request):
        serializer=ChargeOnVideoSerializer(data=request.data)
        if serializer.is_valid():
            length=request.data.get('length',None)
            size=float(request.data.get('size',None))
            type=request.data.get('type',None)
            charge=0
            if size<500.0 and length<6.18:
                charge=5,
            elif size>500.0 and length<6.18:
                charge=12.5
            elif size>500.0 and length>6.18:
                charge=20
            return Response({'charge':charge, "status_type":'Success', "status_code":200}) 
        return Response({"status_msg":serializer.errors, "status_type":'Error', "status_code":400}) 


