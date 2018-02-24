from django.urls import path

from . import views
from django.views.generic import TemplateView
from django.conf.urls import include, url

urlpatterns = [
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', TemplateView.as_view(template_name='me_api/index.html'))
    #path('', views.index, name='index'),
]
