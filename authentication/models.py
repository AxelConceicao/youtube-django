from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
  subscribers = models.ManyToManyField('self', blank=True, related_name='+', verbose_name='Subscibers')