from django.db import models
from django.utils import timezone
from datetime import datetime

class Hewan(models.Model):
    nama = models.CharField(max_length=50)
    species = models.TextField(max_length=50)
    berat = models.CharField(max_length=10)
    umur = models.CharField(max_length=10)

    def __str__(self):
        return self.nama

class Kandang(models.Model):
    nama = models.CharField(max_length=50)
    isi_kandang = models.CharField(max_length=100)
    luas_kandang = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Penjaga(models.Model):
    nama = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)
    jadwal_jaga = models.CharField(max_length=150)

    def __str__(self):
        return self.nama

class Pengunjung(models.Model):
    nama = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)
    hari_berkunjung = models.CharField(max_length=150)

    def __str__(self):
        return self.nama

# Create your models here.
