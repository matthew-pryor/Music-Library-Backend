from django.forms import CharField, DateField
from django.db import models

# Create your models here.

class Music(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    album = models.CharField(max_length=250)
    release_date = models.DateField()
    genre = models.CharField(max_length=250)