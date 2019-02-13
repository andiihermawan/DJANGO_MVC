from django.db import models
from django.utils import timezone
from datetime import datetime

class Mentor(models.Model):
    nama = models.CharField(max_length=100)
    specialis = models.CharField(max_length=100)
    quote = models.CharField(max_length=1000)
    image = models.CharField(max_length=100)
# Create your models here.
