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
from django.http.response import JsonResponse

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

    @list_route(methods=["get"])
    def show(self, request):
        model = Frame.objects.filter(username=request.GET["username"]).order_by('position')
        output = []
        path = 'https://%s' % request.META['HTTP_HOST']
        for frame in model:
            item = {}
            item["id"] = frame.id
            item["username"] = frame.username
            item["title"] = frame.title
            pictures = Picture.objects.filter(frame_id = frame.id).order_by('position')
            url_list = ', '.join([path + q.image.url for q in pictures])
            id_list = ', '.join([str(q.id) for q in pictures])
            position_list = ', '.join([str(q.position) for q in pictures])
            item["path_list"] = url_list
            item["id_list"] = id_list
            item["position_list"] = position_list
            output.append(item)
        return JsonResponse({"list":output})
    
    @list_route(methods=["post"])
    def add(self, request):
        username = request.POST["username"]
        position = request.POST["position"]
        frame = Frame(position=position,username=username)
        frame.save()
        return JsonResponse({"id" : str(frame.id),"position" : str(frame.position)})
        #return JsonResponse(serializers.serialize("json", frame))

class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    @list_route(methods=["post"])
    def upload(self, request):
        img = request.FILES["image"]
        position = request.POST["position"]
        frame_id = request.POST["frame_id"]
        picture = Picture(position=position,frame_id=frame_id,image=img)
        picture.save()

        return JsonResponse({"id" : str(picture.id)})

