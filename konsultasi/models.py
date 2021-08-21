from django.db import models

# Create your models here.

class Asatid(models.Model):
 name = models.CharField(max_length=200, blank=True, null=True)
 phone = models.CharField(max_length=200, blank=True, null=True)
 email = models.CharField(max_length=200, blank=True, null=True)
 date_created= models.DateTimeField(auto_now_add=True, null=True)

 def __str__(self):
     return self.name

class Petugas(models.Model):

 nik = models.CharField(max_length=200, blank=True, null=True)
 nama_lengkap = models.CharField(max_length=200, blank=True, null=True)
 alamat = models.CharField(max_length=200, blank=True, null=True)
 Jenis_kelamin = models.CharField(max_length=100, blank=True, null=True)
 phone = models.CharField(max_length=200, blank=True, null=True)
 email = models.CharField(max_length=200, blank=True, null=True)
 date_created= models.DateTimeField(auto_now_add=True, null=True)

 def __str__(self):
     return self.nik

class Pakar(models.Model):
 JenisKelamin=(
 ('Laki-Laki', 'Laki-Laki'),
 ('Perempuan' , 'Perempuan'),
 )

 id_pengguna = models.CharField(max_length=200, blank=True, null=True)
 nama_lengkap = models.CharField(max_length=50, blank=True, null=True)
 Jenis_kelamin = models.CharField(max_length=100, blank=True, null=True, choices=JenisKelamin)
 alamat = models.CharField(max_length=200, blank=True, null=True)
 email = models.CharField(max_length=200, blank=True, null=True)
 username = models.CharField(max_length=200, blank=True, null=True)
 password = models.CharField(max_length=200, blank=True, null=True)
 date_created= models.DateTimeField(auto_now_add=True, null=True)

 def __str__(self):
     return self.nama_lengkap

class Masyarakat(models.Model):

 JenisKelamin=(
 ('Laki-Laki', 'Laki-Laki'),
 ('Perempuan' , 'Perempuan'),
 )

 id_pengguna = models.CharField(max_length=200, blank=True, null=True)
 nama_lengkap = models.CharField(max_length=50, blank=True, null=True)
 Jenis_kelamin = models.CharField(max_length=100, blank=True, null=True, choices=JenisKelamin)
 alamat = models.CharField(max_length=200, blank=True, null=True)
 email = models.CharField(max_length=200, blank=True, null=True)
 username = models.CharField(max_length=200, blank=True, null=True)
 password = models.CharField(max_length=200, blank=True, null=True)
 date_created= models.DateTimeField(auto_now_add=True, null=True)

 def __str__(self):
     return self.nama_lengkap

# konsultasi chat
class chat(models.Model):
 id_pesan = models.CharField(max_length=200, blank=True, null=True)
 id_konsultasi = models.CharField(max_length=50, blank=True, null=True) 
 id_pengguna = models.CharField(max_length=200, blank=True, null=True)
 petugas = models.CharField(max_length=200, blank=True, null=True)
 isi = models.CharField(max_length=2200, blank=True, null=True)
 created_at= models.DateTimeField(auto_now_add=True, null=True)

 def __str__(self):
     return self.id_pesan

# konsultasi
class religius(models.Model): 
 id_konsultasi = models.CharField(max_length=50, blank=True, null=True) 
 id_pengguna = models.CharField(max_length=200, blank=True, null=True)
 judul = models.CharField(max_length=200, blank=True, null=True) 
 tanggal = models.DateField(auto_now_add=True, null=True)
 jam = models.TimeField(auto_now_add=True, null=True)
 status = models.CharField(max_length=200, blank=True, null=True)

 def __str__(self):
     return self.id_konsultasi



