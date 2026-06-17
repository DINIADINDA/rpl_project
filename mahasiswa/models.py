from django.db import models

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=15, unique=True)
    nama = models.CharField(max_length=100)
    programstudi = models.CharField(max_length=50)
    angkatan = models.IntegerField()

    def __str__(self):
        return f"{self.nim} - {self.nama}"


class Buku(models.Model):
    judul = models.CharField(max_length=200)
    penulis = models.CharField(max_length=100)
    penerbit = models.CharField(max_length=100)
    tahun_terbit = models.IntegerField()

    def __str__(self):
        return f"{self.judul} - {self.penulis}"