from django.db import models
from django.utils import timezone
from datetime import datetime


class Mentee(models.Model):
    name = models.CharField(max_length=255)
    full_name = models.TextField(max_length=255)
    gender = models.CharField(max_length=255)
    telephone = models.TextField(max_length=255)
    mobile = models.TextField(max_length=255)
    nickname = models.CharField(max_length=255)
    addres = models.TextField(max_length=255)

class BlogPost(models.Model):
    created = models.DateTimeField(default=timezone.now)
    update = models.DateTimeField(default=timezone.now)
    Title = models.CharField(max_length=50)
    Content = models.CharField(max_length=1000)
    Created_by = models.CharField(max_length=100)
    postedby = models.ForeignKey(Mentee, on_delete=models.CASCADE)

# Create your models here.
