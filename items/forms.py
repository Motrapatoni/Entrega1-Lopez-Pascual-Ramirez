from django import forms
from ckeditor.fields import RichTextFormField
from items.models import New

class NewsForms(forms.ModelForm):
    tittle = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control form-control-user'}), required=True)
    body = RichTextFormField()
    image = forms.ImageField(required=True, widget=forms.FileInput(attrs={'class': 'form-control form-control-user'}))
    
    class Meta:
        model = New
        fields = '__all__'
    
    
class SearchNewsForms(forms.Form):
    tittle = forms.CharField(max_length=20, label="")


class Contacts(forms.Form):
    name=forms.CharField(label='Nombre', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control form-control-user mb-2'}))
    mail=forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control form-control-user mb-2'}))
    message=RichTextFormField(label='Mensaje', max_length=200, widget=forms.TextInput(attrs={'class': 'form-control form-control-user mb-2'}))