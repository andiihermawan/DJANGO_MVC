from django.db import models
from django.utils import timezone
from datetime import datetime

class Direksi(models.Model):
    nama_lengkap = models.CharField(max_length=50)
    no_telepon = models.CharField(max_length=15)
    jabatan = models.CharField(max_length=25)

    def __str__(self):
        return self.nama_lengkap

class Mentee(models.Model):
    nama_lengkap = models.CharField(max_length=50)
    no_telepon = models.CharField(max_length=15)
    no_absen = models.CharField(max_length=3)
    nilai_rata_rata = models.FloatField(max_length=50)

    def __str__(self):
        return self.nama_lengkap

class Mata_pelajaran(models.Model):
    nama_pelajaran = models.CharField(max_length=50)
    jadwal_dimulai = models.CharField(max_length=50)
    adwal_berakhir = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_pelajaran

class Mentor(models.Model):
    nama_lengkap = models.CharField(max_length=50)
    no_telepon = models.CharField(max_length=15)
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete=models.CASCADE)


    def __str__(self):
        return self.nama_lengkap

class Challenge(models.Model):
    nama_challenge = models.CharField(max_length=50)
    banyak_soal = models.CharField(max_length=3)
    bobot_nilai = models.CharField(max_length=3)
    mata_pelajaran = models.ForeignKey(Mata_pelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_challenge

class Live_Code(models.Model):
    nama_Live_Code = models.CharField(max_length=50)
    banyak_soal = models.CharField(max_length=3)
    bobot_nilai = models.CharField(max_length=3)
    tangal_pelaksanaan = models.ForeignKey(Mata_pelajaran, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_Live_Code



# Create your models here.
