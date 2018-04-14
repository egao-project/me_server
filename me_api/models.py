from django.db import models
from django.conf import settings
import hashlib
import uuid
import os.path

def get_image_path(instance, filename):
    """カスタマイズした画像パスを取得する.

    :param self: インスタンス (models.Model)
    :param filename: 元ファイル名
    :return: カスタマイズしたファイル名を含む画像パス
    """
    prefix = 'images/'
    name = str(uuid.uuid4()).replace('-', '')
    extension = os.path.splitext(filename)[-1]
    return prefix + name + extension

# Create your models here.
class Frame(models.Model):
    username    = models.CharField(max_length=30, unique=True)
    position = models.IntegerField(default=0, unique=True)
    title = models.CharField(max_length=100, default="")
    frame_type = models.IntegerField(default=0)

#    class Meta:
#        unique_together = ('username', 'title')
#        ordering = ['position']

#    def __unicode__(self):
#        return '%s' % (self.picture.image.url)

class Picture(models.Model):
    frame = models.ForeignKey(Frame, related_name='pictures', on_delete=models.CASCADE)
    position = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_image_path,default="images/default.jpg")
    
    class Meta:
        unique_together = ('frame', 'position')
        ordering = ['position']

    def __unicode__(self):
        return "test" #'%d,%s' % (self.position, self.name)


class FrameType(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    type = models.IntegerField(default=0)
    max = models.IntegerField(default=0)

