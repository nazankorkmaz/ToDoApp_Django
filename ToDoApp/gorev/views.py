from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Gorev
from .forms import GorevCreateForm, GorevDuzenleForm
from django.contrib import messages

from django.shortcuts import  render ,redirect,get_object_or_404

def gorevListesi(request):
     
     gorevler = Gorev.objects.all()
    
     return render(request,'gorev/index.html',{
          'gorevler':gorevler
     })
    #return HttpResponse(" gorevlere başlayalım..")

def gorevOlustur(request):

     if request.method == "POST":
           form = GorevCreateForm(request.POST)
           if form.is_valid():
                form.save()
                return redirect("gorevListesi")
     else:
          form = GorevCreateForm()
     
     return render(request,"gorev/gorevOlustur.html",{"form":form})

def gorevDuzenle(request,id):
     gorev = get_object_or_404(Gorev,pk=id)

     if request.method == "POST":
          gorev = GorevDuzenleForm(request.POST, instance=gorev)
          gorev.save()
          return redirect("gorevListesi")
     else:
          gorev = GorevDuzenleForm(instance=gorev)
     return render(request,"gorev/gorevDuzenle.html",{"form": gorev})

def gorevSil(request,id):
     gorev = get_object_or_404(Gorev, pk= id)

     if request.method == "POST":
          gorev.delete()
          messages.success(request, f"'{gorev.baslik}' adlı görev silindi.")
          return redirect("gorevListesi")
     return render(request,"gorev/gorevSil.html",{"gorev":gorev})