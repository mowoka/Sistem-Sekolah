from django.db import models

# Create your models here.

class Berita(models.Model):
    tanggal = models.DateField(auto_now_add=True)
    judul_berita = models.CharField(max_length=200, null=True)
    short_line = models.CharField(max_length=200, null=True)
    isi_berita = models.CharField(max_length=1500, null=True)
    note = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    #  file = forms.FileField()

    def __str__(self):
        return self.judul_berita

class Comment(models.Model):
    berita = models.ForeignKey(Berita, on_delete=models.SET_NULL, blank=True, null=True)
    nama = models.CharField(max_length=200, null=True)
    jurusan = models.CharField(max_length=200, null=True)
    commentar = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.berita.judul_berita


class Artikel(models.Model):
    tipe = models.CharField(max_length=200, null=True)
    judul_artikel = models.CharField(max_length=200, null=True)
    short_line = models.CharField(max_length=200, null=True)
    isi_artikel = models.CharField(max_length=2000, null=True)
    author = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.judul_artikel


class Contact(models.Model):
    JENIS = (
        ('Guru', 'Guru'),
        ('Ekstrakulikuler','Ekstrakulikuler'),
        ('Osis','Osis'),
    )
    jenis_contact = models.CharField(max_length=200, null=True, choices=JENIS)
    nama_jenis = models.CharField(max_length=200, null=True)
    nama = models.CharField(max_length=200, null=True)
    nomor_hp = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.nama