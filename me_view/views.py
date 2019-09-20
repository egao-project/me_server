from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from me_api.models import Picture
from django.db.models import Func, F, CharField

def index(request):

  max_position = 5
  scheme = "https" if request.is_secure() else "http"
  path = "%s://%s" % (scheme, request.META['HTTP_HOST'])
  # path = "%s://%s" %(scheme, "ec2-13-230-96-6.ap-northeast-1.compute.amazonaws.com")
  frame_id = request.GET["frame_id"]

  # SHA2(frame_id, 512)
  func = Func(
    F('frame_id'),
    function='SHA2',
    template="%(function)s(%(expressions)s, 512)",
    output_field=CharField()
  )

  # SELECT *, SHA2(`frame_id`, 512) as `hash` WHERE `hash` = 'hash' AND `position` < 5 ORDER BY `position` ASC
  pictures = Picture.objects\
    .annotate(hash=func)\
    .filter(hash=frame_id, position__lt=max_position)\
    .order_by('position')

  list = [""] * max_position
  for picture in pictures:
    list[picture.position] = path + picture.image.url

  return render(request, 'index.html', {'list': list, })
# Create your views here.
