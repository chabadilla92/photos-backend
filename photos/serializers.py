from .models import Photo
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our PhotoSerializer
class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Photo
        # the fields that should be included in the serialized output
        fields = ['id', 'image', 'name']