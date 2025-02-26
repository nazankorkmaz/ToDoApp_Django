from django.urls import path
from . import views

urlpatterns = [
    path('',views.gorevListesi, name="gorevListesi"),
    path('arama',views.arama,name="arama"),
    path('toggle/', views.toggle_task, name='toggle_task'),
    path('gorevOlustur',views.gorevOlustur,name="gorevOlustur"),
    path('gorevDuzenle/<int:id>',views.gorevDuzenle,name="gorevDuzenle"),
    path('gorevSil/<int:id>',views.gorevSil,name="gorevSil"),
]
#aaa