from django_filters import rest_framework as filters
#from rest_framework.filters import (
#    SearchFilter,
#    OrderingFilter,
#)
#from rest_framework import filters
from rest_framework import viewsets
from rest_framework import serializers

from .models import Frame, Picture
from .serializer import FrameSerializer, PictureSerializer

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
