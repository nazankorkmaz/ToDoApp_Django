from django.contrib import admin

# Register your models here.

from .models import Gorev

#admin.site.register(Gorev)

@admin.register(Gorev)
class GorevAdmin(admin.ModelAdmin):
    list_display = ("baslik","tanim","tamamlandiMi","tarih") #hangileri gozuksun listelemede
    list_display_links = ("baslik",)#hangileri link olsun
    list_filter =("baslik","tamamlandiMi")#sag taradfa filtreleme kısmı cıktı
    list_editable = ("tamamlandiMi",) #checkbox oldu
    search_fields = ("baslik","tanim","tarih") # ustte arama cubugu cıktı
