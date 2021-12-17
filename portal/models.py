from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

Pilihan = (
    ('trending','Trending'),
    ('biasa', 'Biasa'),
)

class Kategori(models.Model):
    judul = models.CharField(max_length=100, verbose_name='Judul')
    slug = models.SlugField(max_length=150, unique=True)
    
    def __str__(self):
        return str(self.judul)

class Komentar(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    komen = models.TextField()

class Posting(models.Model):
    judul = models.CharField(max_length=255, verbose_name='Judul')
    status = models.CharField(choices=Pilihan, default='draft', max_length=10, verbose_name='Status')
    waktu_publish = models.DateTimeField(verbose_name='Created')
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, verbose_name='Kategori')
    gambar = models.ImageField(upload_to="uploads/%Y/%m/%d", blank=True, null=True)
    konten = RichTextField(blank=True, null=True)
    author = models.CharField(max_length=60, default='Anonymous', verbose_name='Created by')
    komens = models.ForeignKey(Komentar, on_delete=models.CASCADE, null=True, blank=True)
    
    def gambarnya(self):
        try:
            url = self.gambar.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.judul)

    
    

    


