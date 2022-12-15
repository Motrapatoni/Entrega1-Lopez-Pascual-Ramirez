from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class CreationForm(UserCreationForm):
    first_name = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class': 'form-control form-control-user'}), required=True)
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'class': 'form-control form-control-user'}), required=True)
    username = forms.CharField(label='Nombre de usuario',widget=forms.TextInput(attrs={'class': 'form-control form-control-user'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-user', 'placeholder':'example@example.com'}))
    password1 = forms.CharField(max_length=12, label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder':'12 caracteres maximo'}), required=True) 
    password2 = forms.CharField(max_length=12, label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder':'12 caracteres maximo'}), required=True)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}
        
        
class EditProfileForm(forms.Form):
    avatar = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}), required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.CharField(required=False)
    birthday = forms.DateField(required=False)
    

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Contraseña vieja', widget=forms.PasswordInput(attrs={'class':'form-control form-control-user mb-2'})) 
    new_password1 = forms.CharField(label='Contraseña nueva', widget=forms.PasswordInput(attrs={'class':'form-control form-control-user mb-2'}))
    new_password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput(attrs={'class':'form-control form-control-user mb-2'}))
    
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {key: '' for key in fields}