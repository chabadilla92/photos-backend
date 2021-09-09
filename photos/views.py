from .models import Photo
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Photo.objects.all()
    # The serializer class for serializing output
    serializer_class = PhotoSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] 