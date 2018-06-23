from django.conf.urls import include, url 
from rest_framework import routers
from .views import FrameViewSet, PictureViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'frames', FrameViewSet)
router.register(r'pictures', PictureViewSet)
#router.register(r'view_frame', views.view_frame)

#from django.urls import path

#from . import views
#from django.views.generic import TemplateView
#from django.conf.urls import include, url

#urlpatterns = [
#        url(r'^view_frame/$', views.view_frame, name='view_frame'),
#]
