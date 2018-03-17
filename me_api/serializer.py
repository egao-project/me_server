from rest_framework import serializers

from .models import Frame, Picture

class FrameSerializer(serializers.ModelSerializer):
    pictures = serializers.StringRelatedField(many=True)
    class Meta:
        model = Frame
        fields = ('username','title','frame_type','pictures')

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('name','position')
