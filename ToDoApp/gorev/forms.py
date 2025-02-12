from django import forms

from .models import Gorev

class GorevCreateForm(forms.ModelForm):
    class Meta:
        model = Gorev
        fields = ('baslik','tanim','tamamlandiMi')
        labels = {
            "baslik":"Yapılacak iş başlığı",
            "tanim":"İş açıklaması",
            "tamamlandiMi":"Tamamlandıysa işaretleyin"
        }
        widgets ={
            "baslik":forms.TextInput(attrs={"class":"form-control"}),
            "tanim":forms.Textarea(attrs={"class":"form-control"}),
        }
        error_messages ={
        "baslik" :{
            "required" :"Görev başlığı girmelisiniz.",
            "max_length":"maksimum 100 karakter girmelisiniz"
        },
        "tanim":{
            "required":"Görev açıklaması girmelisiniz."
        }
    }

class GorevDuzenleForm(forms.ModelForm):
    class Meta:
        model = Gorev
        fields= ('baslik','tanim','tamamlandiMi')
        labels ={
            "baslik":"Yapılacak iş başlığı",
            "tanim":"İş açıklaması",
            "tamamlandiMi":"Tamamlandıysa işaretleyin",
          
        }
        widgets ={
                "baslik":forms.TextInput(attrs={"class":"form-control"}),
                "tanim":forms.Textarea(attrs={"class":"form-control"}),

            }
        error_messages ={
            "baslik" :{
                "required" :"Görev başlığı girmelisiniz.",
                "max_length":"maksimum 100 karakter girmelisiniz"
            },
            "tanim":{
                "required":"Görev açıklaması girmelisiniz."
            }}