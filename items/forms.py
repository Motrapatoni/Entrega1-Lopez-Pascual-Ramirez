from django import forms
from ckeditor.fields import RichTextField
from items.models import New

class NewsForms(forms.ModelForm):
    tittle = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control form-control-user'}), required=True)
    body = RichTextField()
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control form-control-user'}))
    
    class Meta:
        model = New
        fields = '__all__'
    
    
class SearchNewsForms(forms.Form):
    tittle = forms.CharField(max_length=20, label="")


class Contacts(forms.Form):
    name=forms.CharField(max_length=20)
    mail=forms.EmailField()
    message=forms.CharField(max_length=200)