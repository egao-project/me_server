from rest_framework import serializers

from .models import Frame, Picture

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('id','position','image')

class FrameSerializer(serializers.ModelSerializer):
    pictures = PictureSerializer(many=True, read_only=True)
    #pictures = serializers.SlugRelatedField(
    #    many=True,
    ##    read_only=True,
    #    slug_field='name'
    # )
    class Meta:
        model = Frame
        fields = ('username','title','frame_type','pictures')
