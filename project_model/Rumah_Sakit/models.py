from django.db import models
from django.utils import timezone
from datetime import datetime

class Dokter(models.Model):
    nama = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)
    bidang = models.TextField(max_length=50)
    jadwal_praktek = models.CharField(max_length=150)

    def __str__(self):
        return self.nama

class Pasien(models.Model):
    nama = models.CharField(max_length=50)
    telephone = models.CharField(max_length=15)
    alamat = models.TextField(max_length=150)
    keluhan = models.TextField(max_length=255)

    def __str__(self):
        return self.nama

class Resep(models.Model):
    nama = models.CharField(max_length=50)
    total_harga = models.CharField(max_length=100)
    kumpulan_obat = models.TextField(max_length=150)

    def __str__(self):
        return self.nama

class Obat(models.Model):
    nama = models.CharField(max_length=50)
    Kandungan = models.TextField(max_length=255)
    Khasiat = models.TextField(max_length=255)

    def __str__(self):
        return self.nama

# Create your models here.
