from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from me_api.models import Picture

def index(request):

    path = "https://%s" % request.META['HTTP_HOST']
    if (request.is_secure() == False):
      path = 'http://%s' % request.META['HTTP_HOST']
    frame_id = request.GET["frame_id"]
    pictures = Picture.objects.filter(frame_id = frame_id).order_by('position')
    template = loader.get_template('index.html')
    list = [""] * 5
    for picture in pictures:
        if(picture.position-1 < 5):
          list[picture.position-1] = path + picture.image.url
    context = {}
    context["list"] = list 
    #return HttpResponse(template.render(context, request))
    return render(request, 'index.html', {'url0': list[0],'url1': list[1],'url2': list[2],'url3': list[3],'url4': list[4],}) 
# Create your views here.
