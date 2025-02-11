from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def gorevListesi(request):
    
     return render(request,'gorev/index.html')
    #return HttpResponse(" gorevlere başlayalım..")