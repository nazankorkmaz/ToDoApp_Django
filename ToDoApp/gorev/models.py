from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class Gorev(models.Model): #ORM -Object Relational Mapping
    kullanici =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # her gorev bir kullaniciya ait, kullanici isilinirse gorevleri de silinsin (cascade), bos birakilabilir bu alan, formlarda da bos kalabilir bu alan
    baslik = models.CharField(max_length=200)
    tanim = models.TextField(null= True, blank=True) #veritabaninda ve formda bu alan bos kalabilir
    tamamlandiMi = models.BooleanField(default=False)
    tarih = models.DateTimeField(auto_now_add=True) #gorev olusturuldugunda otomatik dolar

    def __str__(self):
        return self.baslik
    
    class Meta: #nodelin ek yapilandirilmalarinin yapildigi ic sinif
        ordering = ['tamamlandiMi'] #veritabaninda siralama yapildiginda sonuclar nasıl donsun