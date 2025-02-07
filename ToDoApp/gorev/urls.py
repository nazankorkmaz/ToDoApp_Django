from django.urls import path
from . import views

urlpatterns = {
    path('',views.gorevListesi, name="gorevListesi"),
}
#aaa