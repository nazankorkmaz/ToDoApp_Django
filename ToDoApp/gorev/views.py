from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def gorevListesi(request):
    return HttpResponse(" gorevlere başlayalım..")