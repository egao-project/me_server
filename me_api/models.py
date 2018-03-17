from django.db import models

# Create your models here.
class Frame(models.Model):
    username    = models.CharField(max_length=30, unique=True)
    position = models.IntegerField(default=0, unique=True)
    title = models.CharField(max_length=100, default="")
    frame_type = models.IntegerField(default=0)

class Picture(models.Model):
    frame = models.ForeignKey(Frame, related_name='pictures', on_delete=models.CASCADE)
    position = models.IntegerField(default=0)
    name = models.CharField(max_length=100)
    
    class Meta:
        unique_together = ('frame', 'position')
        ordering = ['position']

    def __unicode__(self):
        return "test" #'%d,%s' % (self.position, self.name)


class FrameType(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    type = models.IntegerField(default=0)
    max = models.IntegerField(default=0)

