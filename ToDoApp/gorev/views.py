from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Gorev

def gorevListesi(request):
     
     gorevler = Gorev.objects.all()
    
     return render(request,'gorev/index.html',{
          'gorevler':gorevler
     })
    #return HttpResponse(" gorevlere başlayalım..")