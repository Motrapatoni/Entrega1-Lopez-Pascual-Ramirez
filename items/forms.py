from django import forms

class NewsForms(forms.Form):
    tittle = forms.CharField(max_length=20)
    body = forms.CharField(max_length=120)
    creation_date = forms.DateField()
    owner_first_name = forms.CharField(max_length=16)
    owner_last_name = forms.CharField(max_length=16)
    collaborators = forms.IntegerField()
    
class SearchNewsForms(forms.Form):
    tittle = forms.CharField(max_length=20)
    
class Contacts(forms.Form):
    name=forms.CharField(max_length=20)
    mail=forms.EmailField()
    message=forms.CharField(max_length=200)