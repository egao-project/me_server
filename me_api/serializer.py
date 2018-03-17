from rest_framework import serializers

from .models import Frame, Picture

class FrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frame
        fields = ('username','title','frame_type')

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('frame','name','position')
