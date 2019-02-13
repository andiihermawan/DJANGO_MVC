from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db import models as models

class Blog(models.Model):
    judul = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    image = models.CharField(max_length=100)
    created_at = models.CharField(max_length=50)
# Create your models here.
