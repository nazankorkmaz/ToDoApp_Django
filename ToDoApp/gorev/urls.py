from django.urls import path
from . import views

urlpatterns = [
    path('',views.gorevListesi, name="gorevListesi"),
    path('gorevOlustur',views.gorevOlustur,name="gorevOlustur"),
    path('gorevDuzenle/<int:id>',views.gorevDuzenle,name="gorevDuzenle"),
    path('gorevSil/<int:id>',views.gorevSil,name="gorevSil"),
]
#aaa