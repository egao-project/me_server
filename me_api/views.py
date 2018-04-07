from django_filters import rest_framework as filters
#from rest_framework.filters import (
#    SearchFilter,
#    OrderingFilter,
#)
#from rest_framework import filters
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.decorators import list_route

from .models import Frame, Picture
from .serializer import FrameSerializer, PictureSerializer

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
import json
# FilterSetを継承したフィルタセット(設定クラス)を作る
class FrameFilter(filters.FilterSet):
    username = filters.CharFilter(name="username", lookup_expr='iexact')
    # フィルタの定義

    class Meta:
        model = Frame
        # フィルタを列挙する。
        # デフォルトの検索方法でいいなら、モデルフィールド名のフィルタを直接定義できる。
        fields = ['username'] 

class FrameViewSet(viewsets.ModelViewSet):
    queryset = Frame.objects.all()
    serializer_class = FrameSerializer
    filter_class = FrameFilter
    #filter_backends = (filters.SearchFilter,)
    #search_fields = ['=username']

class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    @list_route(methods=["post"])
    def upload(self, request):
        img = request.FILES["image"]
        name = request.POST["name"]
        position = request.POST["position"]
        frame_id = request.POST["frame_id"]
        picture = Picture(name=name,position=position,frame_id=frame_id,image=img)
        picture.save()
        #ret = {'status': 'true'}
        #return HttpResponse(json.dumps(ret), content_type='application/json')
        serializer = PictureSerializer(data={"name": "image"})

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




