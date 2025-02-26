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


from django.http import JsonResponse
from django.views.decorators.http import require_POST

@require_POST
def toggle_task(request):
    task_id = request.POST.get('task_id')
    # Checkbox'tan gelen değer genellikle string olarak gelir (örn. "true" veya "false")
    tamamlandiMi_str = request.POST.get('tamamlandiMi')
    tamamlandiMi = True if tamamlandiMi_str.lower() == 'true' else False

    try:
        gorev = Gorev.objects.get(id=task_id)
        gorev.tamamlandiMi = tamamlandiMi
        gorev.save()
        return JsonResponse({'status': 'ok', 'tamamlandiMi': gorev.tamamlandiMi})
    except Gorev.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Görev bulunamadı.'}, status=404)


def arama(request):
     print("fonkdayım")
     if "q" in request.GET and request.GET["q"] != "":
          q = request.GET["q"]
          gorevler = Gorev.objects.filter(baslik__contains=q).order_by("tarih")
          print(gorevler)
     
     else:
          print("nerdeyim")
          return redirect("gorevListesi")
     
     return render(request,'gorev/arama.html',
                   {
                        'gorevler':gorevler
                   }
                   )