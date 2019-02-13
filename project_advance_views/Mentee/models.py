from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db import models as models

class Mentee(models.Model):
    nama = models.CharField(max_length=100)
    opinion = models.CharField(max_length=1000)
    image = models.CharField(max_length=100)
# Create your models here.
