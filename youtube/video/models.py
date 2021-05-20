import os
import uuid
import random
from django.db import models
from django.dispatch import receiver
# from django.contrib.auth.models import User
from authentication.models import User

DEFAULT_THUMBNAIL = '/thumbnail/default.jpg'

# Create your models here.
class Video(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  author = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
  file = models.FileField('Video', upload_to="video/")
  thumbnail = models.ImageField(upload_to ='thumbnail/', default=DEFAULT_THUMBNAIL)
  title = models.CharField('Title', max_length=80)
  description = models.TextField('Description', max_length=1000)
  views = models.IntegerField('Views count', default=0)
  likes = models.ManyToManyField(User, blank=True, related_name='+', verbose_name='Likes')
  dislikes = models.ManyToManyField(User, blank=True, related_name='+', verbose_name='Dislikes')
  created_at = models.DateTimeField(auto_now_add=True, blank=True)
  updated_at = models.DateTimeField(auto_now=True, blank=True)

  def __str__(self):
    return self.title

@receiver(models.signals.post_delete, sender=Video)
def auto_delete_file_on_delete(sender, instance, **kwargs):
  if instance.file:
    if os.path.isfile(instance.file.path):
      os.remove(instance.file.path)
  if instance.thumbnail and instance.thumbnail.name != DEFAULT_THUMBNAIL:
    if os.path.isfile(instance.thumbnail.path):
      os.remove(instance.thumbnail.path)